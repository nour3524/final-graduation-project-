import csv
import random
import datetime

def generate_event_logs(num_records):
    event_log_types = {
        "normal": [
            {"event_id": "4624", "source": "Security", "description": "Successful login"},
            {"event_id": "4634", "source": "Security", "description": "User logoff"},
            {"event_id": "4688", "source": "Process", "description": "New process created"}
        ],
        "malicious": [
            {"event_id": "4625", "source": "Security", "description": "Failed login attempt (brute force)"},
            {"event_id": "4672", "source": "Security", "description": "Privilege escalation detected"},
            {"event_id": "4648", "source": "Security", "description": "Explicit credential use detected"}
        ],
        "suspicious": [
            {"event_id": "4768", "source": "Security", "description": "TGT request from unusual location"},
            {"event_id": "4776", "source": "Security", "description": "Attempt to authenticate with clear text credentials"},
            {"event_id": "5145", "source": "Security", "description": "Suspicious file access"}
        ]
    }
    
    records = []
    
    for i in range(num_records):
        log_type = random.choices(["normal", "malicious", "suspicious"], weights=[85, 10, 5])[0]
        event = random.choice(event_log_types[log_type])
        timestamp = (datetime.datetime.now() - datetime.timedelta(seconds=i)).isoformat()
        
        records.append([timestamp, event["event_id"], event["source"], event["description"], log_type])
    
    return records

def generate_process_logs(num_records):
    process_log_types = {
        "normal": [
            {"process": "explorer.exe", "status": "running"},
            {"process": "chrome.exe", "status": "running"},
            {"process": "notepad.exe", "status": "running"}
        ],
        "malicious": [
            {"process": "mimikatz.exe", "status": "executed - credential dumping"},
            {"process": "keylogger.exe", "status": "executed - monitoring keystrokes"},
            {"process": "ransomware.exe", "status": "executed - encrypting files"}
        ],
        "suspicious": [
            {"process": "powershell.exe", "status": "executed unusual script"},
            {"process": "cmd.exe", "status": "executed unexpected netstat scan"},
            {"process": "remote_access.exe", "status": "executed unauthorized connection"}
        ]
    }
    
    records = []
    
    for i in range(num_records):
        log_type = random.choices(["normal", "malicious", "suspicious"], weights=[85, 10, 5])[0]
        process = random.choice(process_log_types[log_type])
        timestamp = (datetime.datetime.now() - datetime.timedelta(seconds=i)).isoformat()
        
        records.append([timestamp, process["process"], process["status"], log_type])
    
    return records

def generate_file_logs(num_records):
    file_log_types = {
        "normal": [
            {"file": "C:\\Users\\Admin\\Documents\\report.docx", "action": "opened"},
            {"file": "C:\\Users\\Employee\\Desktop\\notes.txt", "action": "edited"},
            {"file": "C:\\Users\\Guest\\Downloads\\image.png", "action": "viewed"}
        ],
        "malicious": [
            {"file": "C:\\Users\\Admin\\Documents\\passwords.txt", "action": "copied to USB"},
            {"file": "C:\\Users\\Employee\\Desktop\\sensitive_data.csv", "action": "sent via email"},
            {"file": "C:\\Users\\HR\\Payroll\\payroll.xlsx", "action": "accessed by unauthorized user"}
        ],
        "suspicious": [
            {"file": "C:\\Users\\Admin\\Desktop\\backup.zip", "action": "unexpected large file transfer"},
            {"file": "C:\\Users\\Employee\\Documents\\research.pdf", "action": "modified with external editor"},
            {"file": "C:\\Users\\Public\\Shared\\info.log", "action": "deleted unexpectedly"}
        ]
    }
    
    records = []
    
    for i in range(num_records):
        log_type = random.choices(["normal", "malicious", "suspicious"], weights=[85, 10, 5])[0]
        file_log = random.choice(file_log_types[log_type])
        timestamp = (datetime.datetime.now() - datetime.timedelta(seconds=i)).isoformat()
        
        records.append([timestamp, file_log["file"], file_log["action"], log_type])
    
    return records

def save_logs_to_csv(filename, headers, records):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(records)

# Generate logs
num_records = 100000

# Event Logs
event_logs = generate_event_logs(num_records)
save_logs_to_csv("event_logs.csv", ["timestamp", "event_id", "source", "description", "log_type"], event_logs)

# Process Logs
process_logs = generate_process_logs(num_records)
save_logs_to_csv("process_logs.csv", ["timestamp", "process", "status", "log_type"], process_logs)

# File Logs
file_logs = generate_file_logs(num_records)
save_logs_to_csv("file_logs.csv", ["timestamp", "file", "action", "log_type"], file_logs)

print("Logs generated and saved successfully!")
