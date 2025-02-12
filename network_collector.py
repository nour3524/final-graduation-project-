import psutil
import json
import time
import requests
from datetime import datetime
from scapy.all import sniff, IP, DNS

DETECTION_API = "http://127.0.0.1:5001/detect"  # API endpoint of detection system

BLACKLISTED_IPS = ["192.0.2.1", "203.0.113.5"]  # Example blacklisted IPs
dns_logs = []

# Function to collect network connections
def collect_network_connections():
    for conn in psutil.net_connections(kind='inet'):
        if conn.status == "ESTABLISHED":
            yield {
                "type": "network",
                "timestamp": datetime.now().isoformat(),
                "local_ip": conn.laddr.ip,
                "remote_ip": conn.raddr.ip if conn.raddr else None,
                "protocol": "TCP" if conn.type == 1 else "UDP",
                "blacklisted": conn.raddr.ip in BLACKLISTED_IPS if conn.raddr else False
            }

# Function to collect DNS requests
def collect_dns_requests(packet):
    if packet.haslayer(DNS) and packet.haslayer(IP):
        dns_logs.append({
            "type": "network",
            "timestamp": datetime.now().isoformat(),
            "source_ip": packet[IP].src,
            "queried_domain": packet[DNS].qd.qname.decode() if packet[DNS].qd else None
        })

# Function to send logs to detection system
def send_to_detection(log):
    try:
        response = requests.post(DETECTION_API, json=log)
        print(f"Sent log to detection system: {response.json()}")
    except Exception as e:
        print(f"Error sending log: {e}")

# Start sniffing DNS in background
sniff(filter="udp port 53", prn=collect_dns_requests, store=0, count=100, timeout=10)

# Main loop
while True:
    for conn_log in collect_network_connections():
        send_to_detection(conn_log)

    for dns_log in dns_logs:
        send_to_detection(dns_log)

    dns_logs.clear()
    time.sleep(5)
