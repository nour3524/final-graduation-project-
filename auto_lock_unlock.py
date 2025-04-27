import pyodbc
import face_recognition
import cv2
import os
import time
import socket  # To get PC name automatically
# from logger import log_event

# 🔹 Step 1: Get PC Name Automatically
PC_NAME = socket.gethostname()  # Auto-detect PC name

# 🔹 Step 2: Connect to SQL Server and Fetch User Data
def get_user_info(user_name):
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
          "SERVER=DESKTOP-6P94OPL;"  
          "DATABASE=UEBA_Analytics;"
          "Trusted_Connection=yes;"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT device_id, photo_path FROM dbo.employees_profile WHERE full_name = ?", (user_name,))
    result = cursor.fetchone()
    conn.close()
    return result if result else None  # Returns (device_id, photo_path)

# 🔹 Step 3: Load Face Encodings from Database
def load_encodings_from_db():
    conn = pyodbc.connect(
         "DRIVER={ODBC Driver 17 for SQL Server};"
           "SERVER=DESKTOP-6P94OPL;"  
            "DATABASE=UEBA_Analytics;"
            "Trusted_Connection=yes;"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT full_name, photo_path FROM dbo.employees_profile")
    users = cursor.fetchall()

    known_face_encodings = []
    known_face_names = []

    for name, photo_path in users:
        if photo_path and os.path.exists(photo_path):
            image = face_recognition.load_image_file(photo_path)
            encodings = face_recognition.face_encodings(image)

            if encodings:
                known_face_encodings.append(encodings[0])
                known_face_names.append(name)
        else:
            print(f"⚠️ Warning: Photo not found for {name} at {photo_path}")

    conn.close()
    return known_face_encodings, known_face_names

# 🔹 Start recognition
known_face_encodings, known_face_names = load_encodings_from_db()

# Start camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
user_present = False
last_seen_time = None

print("🔍 Face Recognition Running...")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ Camera error: Unable to grab frame.")
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_encodings = face_recognition.face_encodings(rgb_frame)

        if face_encodings:
            if known_face_encodings:
                face_distances = face_recognition.face_distance(known_face_encodings, face_encodings[0])
            
                if len(face_distances) > 0:
                 best_match_index = face_distances.argmin()
                 if face_distances[best_match_index] < 0.6:  
                    recognized_name = known_face_names[best_match_index]
                    user_info = get_user_info(recognized_name)
                    
                    if user_info and user_info[0] == PC_NAME:
                        if not user_present:
                            print(f"✅ Welcome, {recognized_name}! Access granted for {PC_NAME}.")
                            log_event("unlock", recognized_name, f"Face recognized and PC unlocked on {PC_NAME}")

                        user_present = True
                        last_seen_time = time.time()
                        no_face_printed = False  # Reset silent no-face state

                else:
                    print(f"❌ {recognized_name} is not authorized for {PC_NAME}!")
                    log_event("unauthorized", recognized_name, f"User tried to unlock unauthorized PC: {PC_NAME}")

            else:
                print("❌ Unknown User Detected")
                log_event("unknown", "Unknown", "Unregistered face appeared at PC")

        else:
             # 🔒 Auto-lock if user is gone for 5 seconds
             if user_present and last_seen_time and (time.time() - last_seen_time > 5):
                print("🔒 Locking PC... (User not detected for 5 seconds)")
                os.system("rundll32.exe user32.dll,LockWorkStation")
                log_event("lock", recognized_name, "PC auto-locked due to no face detected")

                user_present = False
                last_seen_time = None
                no_face_printed = False  # Reset after locking
             elif not user_present:
                if 'no_face_printed' not in locals() or not no_face_printed:
                    print("👤 No face detected...")
                    no_face_printed = True    

        time.sleep(3)

except KeyboardInterrupt:
    print("\n🛑 Stopping Face Recognition...")
    cap.release()
    cv2.destroyAllWindows()

