import csv
import random
import datetime

class NetworkLogGenerator:
    def __init__(self, total_logs=300000):
        self.total_logs = total_logs
        self.normal_ratio = 0.85
        self.malicious_ratio = 0.10
        self.suspicious_ratio = 0.05
        self.start_time = datetime.datetime(2025, 1, 1, 0, 0, 0)
        self.time_increment = datetime.timedelta(seconds=10)  # Adjusted for realism
        self.current_time = self.start_time

    def generate_ip(self, blacklisted=False):
        if blacklisted:
            return random.choice(["203.0.113.5", "185.220.101.5", "45.33.32.156"])  # Malicious IPs
        return f"192.168.1.{random.randint(2, 254)}"

    def generate_log(self, label):
        self.current_time += self.time_increment
        log = {
            "timestamp": self.current_time.strftime("%Y-%m-%dT%H:%M:%S"),
            "local_ip": self.generate_ip(),
            "local_port": random.randint(1024, 65535),
            "remote_ip": self.generate_ip(blacklisted=(label == "malicious")),
            "remote_port": random.choice([80, 443, 22, 3389, 53, 8080]),
            "protocol": random.choice(["TCP", "UDP"]),
            "blacklisted": label == "malicious",
            "label": label,
            "reason": self.get_reason(label)
        }
        return log

    def get_reason(self, label):
        if label == "malicious":
            return random.choice([
                "Communication with known C2 server",
                "High-volume outbound traffic suggesting data exfiltration",
                "Remote access from unauthorized location",
                "Frequent access to TOR network",
                "Multiple connections to blacklisted IPs",
                "Unusual encrypted traffic spikes detected",
                "Malware command-and-control communication detected"
            ])
        elif label == "suspicious":
            return random.choice([
                "Unusual number of connections to cloud storage services",
                "Accessing external IPs outside normal working hours",
                "High number of DNS requests to untrusted domains",
                "Repeated failed connection attempts",
                "Unusual outbound traffic volume"
            ])
        return "Normal network activity"

    def generate_logs(self):
        logs = []
        normal_count = int(self.total_logs * self.normal_ratio)
        malicious_count = int(self.total_logs * self.malicious_ratio)
        suspicious_count = int(self.total_logs * self.suspicious_ratio)
        
        for _ in range(normal_count):
            logs.append(self.generate_log("benign"))
        for _ in range(malicious_count):
            logs.append(self.generate_log("malicious"))
        for _ in range(suspicious_count):
            logs.append(self.generate_log("suspicious"))
        
        return sorted(logs, key=lambda x: x["timestamp"])  # Ensuring chronological order

    def save_to_csv(self, filename="network_logs.csv"):
        logs = self.generate_logs()
        with open(filename, "w", newline="") as csvfile:
            fieldnames = ["timestamp", "local_ip", "local_port", "remote_ip", "remote_port", "protocol", "blacklisted", "label", "reason"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(logs)

if __name__ == "__main__":
    generator = NetworkLogGenerator()
    generator.save_to_csv()
