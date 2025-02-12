import psutil
import socket
import json
import ssl
import wmi
import time
import logging
import getpass
import requests

# Logging setup
logging.basicConfig(level=logging.INFO)

DETECTION_API = "http://127.0.0.1:5001/detect"  # API endpoint of detection system

w = wmi.WMI()  # Initialize WMI for Windows logs
current_user = getpass.getuser()  # Get logged-in user

# Function to collect security event logs
def collect_event_logs():
    try:
        event_log = w.Win32_NTLogEvent(Logfile="Security")
        for event in event_log:
            if event.EventCode in ['4624', '4672', '4663']:  # Login, privilege escalation, file access
                yield {
                    "type": "os",
                    "event_id": event.EventCode,
                    "timestamp": event.TimeGenerated,
                    "source": event.SourceName,
                    "message": event.InsertionStrings,
                    "user": event.InsertionStrings[5] if len(event.InsertionStrings) > 5 else "Unknown"
                }
    except Exception as e:
        logging.error(f"Error collecting event logs: {e}")

# Function to send logs to detection system
def send_to_detection(log):
    try:
        response = requests.post(DETECTION_API, json=log)
        logging.info(f"Sent log to detection system: {response.json()}")
    except Exception as e:
        logging.error(f"Error sending log: {e}")

# Main loop
while True:
    for event_log in collect_event_logs():
        send_to_detection(event_log)

    time.sleep(5)  # Wait before next collection cycle
