from flask import Flask, request, jsonify
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
import logging
import json

app = Flask(__name__)
model = ChatOllama(model="llama3")

# Configure logging to save detections into a file
logging.basicConfig(filename="detection_results.log", level=logging.INFO, format="%(asctime)s - %(message)s")

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

@app.route('/detect', methods=['POST'])
def detect():
    log = request.json  # Receive log as JSON
    if not log:
        return jsonify({"error": "Invalid log received"}), 400

    try:
        # Convert the log dictionary into a formatted string
        log_text = json.dumps(log, indent=4)

        # 🛠 Apply the prompt and invoke the model
        formatted_prompt = prompt_template.invoke({"log": log_text})  
        response = model.invoke(formatted_prompt)  
        classification = response.content.strip()

        # 🛠 Modify classification based on the requirement
        if "normal" in classification.lower():
            log["classification"] = "normal"  # Keep only 'normal'
        else:
            log["classification"] = classification  # Keep full classification for malicious cases

        # Save the result in a file
        with open("detection_results.json", "a") as f:
            f.write(json.dumps(log, indent=4) + ",\n")

        # Log in terminal and file
        logging.info(f"Detected log: {json.dumps(log, indent=4)}")

        if "malicious" in log["classification"].lower():
            print("log:\n",log)
            print("ALERT! Malicious activity detected:", classification)

        return jsonify(log)

    except Exception as e:
        logging.error(f"Error processing log: {e}")
        return jsonify({"error": "Detection failed"}), 500


if __name__ == '__main__':  
    app.run(port=5001, debug=True)
