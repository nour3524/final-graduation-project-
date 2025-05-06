#==================== email_approval_server.py ====================
from flask import Flask, request
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return "Approval Server is running."

@app.route('/approve')
def approve():
    intruder_id = request.args.get('id', 'unknown')
    with open("approval_log.txt", "a") as f:
        f.write(f"[{datetime.now()}] APPROVED access for: {intruder_id}\n")
    return f"✅ Access approved for: {intruder_id}"

@app.route('/deny')
def deny():
    intruder_id = request.args.get('id', 'unknown')
    with open("approval_log.txt", "a") as f:
        f.write(f"[{datetime.now()}] DENIED access for: {intruder_id}\n")
    os.system("shutdown /s /t 1")  # 🔒 Shuts down the laptop immediately
    return f"❌ Access denied. System shutting down for: {intruder_id}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
