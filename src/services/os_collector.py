import os
import time
import json
import requests
from datetime import datetime
import platform

DETECTION_API = "http://127.0.0.1:5001/detect"

# 🔁 Smart Batching Setup
log_batch = []
BATCH_SIZE = 10
BATCH_INTERVAL = 15
last_batch_time = time.time()

def collect_os_logs():
    logs = []

    # Basic info: timestamp, platform, user
    logs.append({
        "type": "os",
        "timestamp": datetime.now().isoformat(),
        "os": platform.system(),
        "release": platform.release(),
        "user": os.getlogin()
    })

    # Example: Suspicious PowerShell script execution
    powershell_script_detected = os.path.exists("C:\\Windows\\Temp\\malicious.ps1")
    if powershell_script_detected:
        logs.append({
            "type": "os",
            "timestamp": datetime.now().isoformat(),
            "event": "Potential malicious script detected",
            "path": "C:\\Windows\\Temp\\malicious.ps1"
        })

    return logs

def send_batch():
    global log_batch
    if log_batch:
        try:
            response = requests.post(DETECTION_API, json=log_batch)
            print(f"✅ Sent batch of {len(log_batch)} logs at {datetime.now().isoformat()}")
        except Exception as e:
            print("❌ Error sending batch:", e)
        log_batch = []

# 🚀 Main Loop
while True:
    collected = collect_os_logs()
    log_batch.extend(collected)

    now = time.time()
    if len(log_batch) >= BATCH_SIZE or (now - last_batch_time) >= BATCH_INTERVAL:
        send_batch()
        last_batch_time = now

    time.sleep(5)  # Adjust based on how frequently you want to poll
