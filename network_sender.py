import psutil
import socket
import json
import time
from datetime import datetime
from scapy.all import sniff, IP, TCP, UDP, DNS

# Server details for log forwarding
SERVER_HOST = 'server_ip'  # Replace with your server's IP
SERVER_PORT = 5000         # Port to send logs

# List of blacklisted IPs (example, can be expanded)
BLACKLISTED_IPS = ["192.0.2.1", "203.0.113.5"]

# Function to get active network connections
def collect_network_connections():
    connections = []
    for conn in psutil.net_connections(kind='inet'):
        if conn.status == "ESTABLISHED":
            connections.append({
                "timestamp": datetime.now().isoformat(),
                "local_ip": conn.laddr.ip,
                "local_port": conn.laddr.port,
                "remote_ip": conn.raddr.ip if conn.raddr else None,
                "remote_port": conn.raddr.port if conn.raddr else None,
                "protocol": "TCP" if conn.type == socket.SOCK_STREAM else "UDP",
                "blacklisted": conn.raddr.ip in BLACKLISTED_IPS if conn.raddr else False
            })
    return connections

# Function to monitor total network traffic
def collect_network_usage():
    net_io = psutil.net_io_counters()
    return {
        "timestamp": datetime.now().isoformat(),
        "bytes_sent": net_io.bytes_sent,
        "bytes_received": net_io.bytes_recv
    }

# Function to collect DNS requests (Requires admin privileges)
def collect_dns_requests(packet):
    if packet.haslayer(DNS) and packet.haslayer(IP):
        dns_logs.append({
            "timestamp": datetime.now().isoformat(),
            "source_ip": packet[IP].src,
            "destination_ip": packet[IP].dst,
            "queried_domain": packet[DNS].qd.qname.decode() if packet[DNS].qd else None
        })

# Function to forward logs to the server
def forward_logs(logs):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((SERVER_HOST, SERVER_PORT))
            client_socket.send(json.dumps(logs).encode())
    except Exception as e:
        print(f"Error forwarding logs: {e}")

# Start DNS sniffing in a separate thread (non-blocking)
dns_logs = []
sniff(filter="udp port 53", prn=collect_dns_requests, store=0, count=100, timeout=10)

# Main loop
while True:
    logs = {
        "network_connections": collect_network_connections(),
        "network_usage": collect_network_usage(),
        "dns_requests": dns_logs
    }
    forward_logs(logs)

    # Wait before next collection cycle
    time.sleep(60)
