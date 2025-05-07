from flask import Flask, request, jsonify
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
import logging
import json
import pyodbc

app = Flask(__name__)
model = ChatOllama(model="llama3")

# Configure logging to file
logging.basicConfig(filename="detection_results.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# SQL Server connection string
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-6P94OPL;"
    "DATABASE=UEBA_Analytics;"
    "Trusted_Connection=yes;"
)

# ✅ Enhanced LangChain detection prompt
prompt_template = ChatPromptTemplate.from_messages([
    ("system", """You are an expert at detecting malicious behavior from OS and network logs. 
    Classify each log as 'normal' or 'malicious' based on these rules:

    1️ Unauthorized Access & Login Anomalies
    - Detect logins outside 9 AM - 5 PM.
    - Identify logins from non-corporate IPs (outside 192.168.x.x).
    - Alert on >5 failed login attempts in 10 minutes.
    - Detect same-user logins from 2+ devices in 5 minutes.
    - Flag Event IDs 4625, 4672, 4720, 4728.

    2️ Network & Communication Anomalies
    - Connections to TOR, dark web, or known bad IPs.
    - >10GB outbound traffic/hour.
    - Beaconing or DNS tunneling patterns.

    3️ File & Data Access Anomalies
    - Suspicious files: .exe, .zip, .ps1
    - >5GB accessed in 3 mins.
    - Commands like 'rm -rf /var/logs' or 'wevtutil cl *'
    - Transfers to USB, Gmail, or cloud.

    4️ Software & Process Execution Anomalies
    - Tools like Mimikatz, Metasploit.
    - Privilege escalation: sudo, chmod 777, runas.
    - RDP/AnyDesk access after hours.

    5️ Endpoint & Device Anomalies
    - Block unauthorized USBs.
    - Windows Defender or firewall disabled.

    6️ Behavior & Workflow Anomalies
    - Inactive logins >2h.
    - 10+ emails to external domains in 5 mins.
    - Strange email attachments to unknown people.

    Respond ONLY with: normal OR malicious [with reason].
    """),
    ("human", "{log}")
])

@app.route('/detect', methods=['POST'])
def detect():
    log = request.json
    if not log:
        return jsonify({"error": "Invalid log received"}), 400

    try:
        # Format the log for the LLM
        log_text = json.dumps(log, indent=4)
        formatted_prompt = prompt_template.invoke({"log": log_text})
        response = model.invoke(formatted_prompt)
        classification = response.content.strip()

        # Add classification field to log
        log["classification"] = "normal" if "normal" in classification.lower() else "malicious"

        # Save result to local file
        with open("detection_results.json", "a") as f:
            f.write(json.dumps(log, indent=4) + ",\n")

        logging.info(f"Detected log: {json.dumps(log, indent=4)}")

        # Save to DB if malicious
        if "malicious" in log["classification"].lower():
            print("🚨 ALERT! Malicious activity detected:", classification)
            try:
                with pyodbc.connect(conn_str) as conn:
                    cursor = conn.cursor()
                    cursor.execute("""
                        INSERT INTO malicious_logs (timestamp, log_type, details, classification, user_id)
                        VALUES (?, ?, ?, ?, ?)
                    """,
                    log.get("EventTime", None),  # timestamp
                    "network" if "SourceIp" in log else "os",  # log_type
                    json.dumps(log),  # details
                    "High" if "high" in log.get("classification", "").lower() else "Medium",  # classification level
                    log.get("user_id", None)  # FK from employees_profile
                    )
                    conn.commit()
                    print("✅ Malicious log saved to database.")
            except Exception as db_err:
                logging.error(f"❌ Failed to insert log into DB: {db_err}")
                print("❌ DB insertion error:", db_err)

        return jsonify(log)

    except Exception as e:
        logging.error(f"❌ Detection error: {e}")
        return jsonify({"error": "Detection failed"}), 500

if __name__ == '__main__':
    app.run(port=5001, debug=True)
