import psutil
import json
import time
import requests
from datetime import datetime
from scapy.all import sniff, IP, DNS

# API endpoint
DETECTION_API = "http://127.0.0.1:5001/detect"

# Sample blacklist
BLACKLISTED_IPS = ["192.0.2.1", "203.0.113.5"]

# DNS log buffer
dns_logs = []

# Function to collect active network connections
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

# 🔁 Smart Batching Setup
log_batch = []
BATCH_SIZE = 10
BATCH_INTERVAL = 15
last_batch_time = time.time()

def send_batch():
    global log_batch
    if log_batch:
        try:
            response = requests.post(DETECTION_API, json=log_batch)
            print(f"✅ Sent batch of {len(log_batch)} logs at {datetime.now().isoformat()}")
        except Exception as e:
            print("❌ Error sending batch:", e)
        log_batch = []

# Start sniffing DNS traffic in the background
from threading import Thread
Thread(target=lambda: sniff(filter="udp port 53", prn=collect_dns_requests, store=False), daemon=True).start()

# 🚀 Main Collection Loop
while True:
    for conn_log in collect_network_connections():
        log_batch.append(conn_log)

    # Add DNS logs if any were captured
    while dns_logs:
        log_batch.append(dns_logs.pop(0))

    now = time.time()
    if len(log_batch) >= BATCH_SIZE or (now - last_batch_time) >= BATCH_INTERVAL:
        send_batch()
        last_batch_time = now

    time.sleep(3)
