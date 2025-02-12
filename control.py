import subprocess
import os
import signal
import sys
import time

# Store process IDs
processes = []

def start_system():
    """Start the face recognition system."""
    print("🚀 Starting Face Recognition System...")

    # Start authentication & auto-lock
    p1 = subprocess.Popen(["python", "face_authenticator.py"], creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
    p2 = subprocess.Popen(["python", "auto_lock_unlock.py"], creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
    
    processes.extend([p1, p2])

    print("✅ System Activated! (Type 'stop' to deactivate)")

    while True:
        user_input = input("> ").strip().lower()
        if user_input == "stop":
            stop_system()
            break

def stop_system():
    """Stop all running processes properly."""
    print("🛑 Stopping Face Recognition System...")

    for process in processes:
        try:
            if os.name == "nt":  # Windows
                subprocess.call(["taskkill", "/F", "/T", "/PID", str(process.pid)])
            else:  # Linux/Mac
                os.killpg(os.getpgid(process.pid), signal.SIGTERM)
        except Exception as e:
            print(f"⚠️ Error stopping process: {e}")

    print("✅ System Deactivated!")
    sys.exit()

if __name__ == "__main__":
    start_system()
