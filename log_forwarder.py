import socket
import win32evtlog
import win32evtlogutil
from datetime import datetime

def collect_event_logs(log_type="Security"):
    """Collect logs from Windows Event Log."""
    logs = []
    try:
        handle = win32evtlog.OpenEventLog('localhost', log_type)
        flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
        events = win32evtlog.ReadEventLog(handle, flags, 0)
        for event in events:
            log_entry = {
                "EventID": event.EventID,
                "Source": event.SourceName,
                "TimeGenerated": event.TimeGenerated.strftime('%Y-%m-%d %H:%M:%S'),
                "Description": win32evtlogutil.SafeFormatMessage(event, event.SourceName)
            }
            logs.append(log_entry)
        win32evtlog.CloseEventLog(handle)
    except Exception as e:
        print(f"Error collecting logs: {e}")
    return logs

def forward_logs(logs, receiver_ip, port):
    """Send collected logs to the receiver laptop."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((receiver_ip, port))
            for log in logs:
                s.sendall((str(log) + "\n").encode())
            print("Logs sent successfully!")
        except Exception as e:
            print(f"Error sending logs: {e}")

if __name__ == "__main__":
    receiver_ip = "RECEIVER_IP_ADDRESS"  # Replace with the receiver's IP address
    port = 5000  # Replace with the receiver's listening port
    logs = collect_event_logs("Security")  # You can change the log type here
    forward_logs(logs, receiver_ip, port)
