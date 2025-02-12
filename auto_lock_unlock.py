import os
import time
import cv2
import face_recognition
import pickle

ENCODINGS_PATH = "encodings.pickle"



# Load known encodings
with open(ENCODINGS_PATH, "rb") as f:
    data = pickle.load(f)

known_face_encodings = data["encodings"]

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Ensure proper camera access
user_present = False  # Track if the user is recognized
last_seen_time = None  # Track last time the user was seen
status_printed = None  # Track last printed status

print("🔍 Face Recognition Running...")

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ Camera error: Unable to grab frame.")
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_encodings = face_recognition.face_encodings(rgb_frame)

    if face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encodings[0])
        if True in matches:
            if not user_present:  # Only unlock once
                print("✅ User Recognized → 🔓 Unlocking PC")
                user_present = True
                status_printed = "recognized"
            last_seen_time = time.time()  # Reset last seen time
        else:
            last_seen_time = time.time()  # Reset timer if unknown user appears
            if status_printed != "unknown":
                print("❌ Unknown User Detected")
                status_printed = "unknown"
    else:
        if user_present and last_seen_time and (time.time() - last_seen_time > 5):
            # Only lock if user has been gone for 5 seconds
            print("🔒 Locking PC... (User not detected for 5 seconds)")
            os.system("rundll32.exe user32.dll,LockWorkStation")  # Locks PC
            user_present = False  # Reset user state
            status_printed = "locked"

    time.sleep(3)  # ⏳ Add delay to prevent repeated outputs