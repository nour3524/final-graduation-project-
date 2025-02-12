import subprocess

print("Starting Face Recognition System...")

# Start authentication & auto-lock system
subprocess.Popen(["python", "face_authenticator.py"])
subprocess.Popen(["python", "auto_lock_unlock.py"])
