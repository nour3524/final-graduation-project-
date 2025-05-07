from flask import Flask, request, jsonify
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
import logging
import json
import os  # For handling log file path
import pyodbc

app = Flask(__name__)
model = ChatOllama(model="llama3")

# 🔄 Set up custom log directory
LOG_DIR = os.path.join(os.path.dirname(__file__), "../../logs")
os.makedirs(LOG_DIR, exist_ok=True)

log_file_path = os.path.join(LOG_DIR, "detection_results.log")
json_file_path = os.path.join(LOG_DIR, "detection_results.json")

# 🔄 Updated to use full log path
logging.basicConfig(filename=log_file_path, level=logging.INFO, format="%(asctime)s - %(message)s")

# Define prompt with enhanced detection criteria
prompt_template = ChatPromptTemplate.from_messages([
    ("system", """You are an expert at detecting malicious behavior from OS and network logs. 
    Classify each log as 'normal' or 'malicious' based on these rules:

    1️ **Unauthorized Access & Login Anomalies**
    - Detect logins **outside 9 AM - 5 PM**.
    - Identify logins from **non-corporate IP ranges** (e.g., outside `192.168.x.x`).
    - Alert when there are **more than 5 failed login attempts within 10 minutes**.
    - Detect **simultaneous logins** from the same user on **2+ devices within 5 minutes**.
    - Identify unauthorized admin access based on Windows Event IDs:
      - `4625` (failed login)
      - `4672` (special privileges assigned)
      - `4720` (admin account created)
      - `4728` (privileged group modification)

    2️ **Network & Communication Anomalies**
    - Detect connections to **TOR exit nodes, known malicious IPs, or dark web servers**.
    - Flag **high-volume outbound traffic (>10GB per hour)** for possible data exfiltration.
    - Identify **C2 (Command & Control) communication patterns**:
      - Repetitive **beaconing traffic** (e.g., periodic connections).
      - Suspicious **DNS tunneling** (e.g., excessive queries with encoded payloads).

    3️ **File & Data Access Anomalies**
    - Alert on downloads of **suspicious file types** (`.exe`, `.zip`, `.7z`, `.bat`, `.ps1`).
    - Trigger an alert when **>5GB of sensitive data is accessed within 3 minutes**.
    - Detect **log deletion attempts**:
      - Linux: `rm -rf /var/logs`
      - Windows: `wevtutil cl *`
    - Monitor file transfers to **USB, personal email, or cloud storage**.

    4️ **Software & Process Execution Anomalies**
    - Detect **execution of hacking tools** (`Mimikatz`, `Metasploit`, `Empire`, `Cobalt Strike`).
    - Monitor privilege escalation attempts:
      - Linux: `sudo su`, `chmod 777`, `chown root`
      - Windows: `runas /savecred`, UAC bypass attempts
    - Identify unauthorized **remote access tools** (`AnyDesk`, `TeamViewer`, RDP outside work hours).

    5️ **Endpoint & Peripheral Device Anomalies**
    - Block unauthorized **USB devices** (only allow company-issued devices).
    - Detect security setting modifications:
      - Disabling Windows Defender: Registry `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender`
      - Firewall modifications: Running `netsh advfirewall set allprofiles state off`

    6️ **Behavioral & Workflow Anomalies**
    - Detect **inactive login sessions >2 hours without keyboard/mouse activity**.
    - Flag users **forwarding >10 emails to external domains in 5 minutes**.
    - Identify **unusual email patterns**, such as sending large attachments to unknown recipients.

    Provide your response as: normal OR malicious [reason]."""),
    ("human", "{log}")
])

# 🔄 Moved save_to_database() out of detect() for clarity and reuse
def save_to_database(log):
    try:
        print("📥 TRYING TO INSERT INTO DB:", log)
        conn = pyodbc.connect(
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=DESKTOP-6P94OPL;"  # Replace if your server is named
            "Database=UEBA_Analytics;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO dbo.malicious_logs (timestamp, log_type, details, classification)
            VALUES (?, ?, ?, ?)
        """, (
            log.get("timestamp").replace("T", " ").split(".")[0],
            log.get("type"),
            json.dumps(log),
            log.get("classification")
        ))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as db_err:
        # 🔄 Add this block right here:
        print("❌ DB Insert Failed:", db_err)
        logging.error(f"DB Insert Failed: {db_err}")

@app.route('/detect', methods=['POST'])
def detect():
    data = request.json

    logs = data if isinstance(data, list) else [data]
    results = []

    for log in logs:
        try:
            log_text = json.dumps(log, indent=4)
            formatted_prompt = prompt_template.invoke({"log": log_text})
            response = model.invoke(formatted_prompt)
            classification = response.content.strip()

            log["classification"] = "normal" if "normal" in classification.lower() else classification

            with open(json_file_path, "a") as f:
                f.write(json.dumps(log, indent=4) + ",\n")

            logging.info(f"Detected log: {json.dumps(log, indent=4)}")

            if "malicious" in log["classification"].lower():
                save_to_database(log)
                print("log:\n", log)
                print("ALERT! Malicious activity detected:", classification)

            results.append(log)

        except Exception as e:
            logging.error(f"Error processing log: {e}")
            results.append({"error": "Detection failed", "log": log})

    return jsonify(results)


if __name__ == '__main__':
    app.run(port=5001, debug=True)
