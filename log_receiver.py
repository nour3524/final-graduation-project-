import socket
import json
import requests

HOST = '0.0.0.0'
PORT = 6060

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"📡 Listening for logs on port {PORT}...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"🔗 Connection from {addr}")

    try:
        data = client_socket.recv(4096).decode('utf-8')
        print("🪵 Raw data received:", repr(data))  # ✅ Debug line to see exact data

        if not data.strip():
            print("⚠ Received empty data!")
            client_socket.close()
            continue

        try:
            log = json.loads(data)
        except json.JSONDecodeError as json_err:
            print("❌ Received invalid JSON:", json_err)
            client_socket.close()
            continue

        print("📄 Log received:", log)

        # 🧠 Send to detection.py via HTTP
        response = requests.post("http://127.0.0.1:5001/detect", json=log)
        result = response.json()
        print("🧠 Detection Result:", result)

        if "malicious" in result.get("classification", "").lower():
            with open("malicious_logs.json", "a") as f:
                f.write(json.dumps(result) + "\n")
            print("🚨 Malicious log saved.")

    except Exception as e:
        print(f"❗ General Error: {e}")

    client_socket.close()