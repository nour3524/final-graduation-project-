import subprocess
import os
import signal
import sys

# Path to your virtual environment Python
PYTHON_PATH = r"d:\GRAD\FaceDetectionProject\env\Scripts\python.exe"

process = None

def start_system():
    global process
    print("🚀 Starting Face Recognition System...")

    process = subprocess.Popen([PYTHON_PATH, "auto_lock_unlock.py"], creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)

    print("✅ System Activated! (Type 'stop' to deactivate)")
    while True:
        user_input = input("> ").strip().lower()
        if user_input == "stop":
            stop_system()
            break

def stop_system():
    global process
    print("🛑 Stopping Face Recognition System...")
    try:
        if os.name == "nt":
            subprocess.call(["taskkill", "/F", "/T", "/PID", str(process.pid)])
        else:
            os.killpg(os.getpgid(process.pid), signal.SIGTERM)
    except Exception as e:
        print(f"⚠️ Error stopping process: {e}")
    print("✅ System Deactivated!")
    sys.exit()

if __name__ == "__main__":
    start_system()
