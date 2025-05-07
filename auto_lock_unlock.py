import pyodbc
import face_recognition
import cv2
import os
import time
import socket
import numpy as np  # ✅ Added for face distance handling
from logger import log_event
from email_alert import send_intruder_alert
from reply_checker import wait_for_owner_reply



#  Get PC name
PC_NAME = socket.gethostname()

#  Store eye geometry of verified user
user_geometry_profile = None
printed_no_face = False

# Track if email has been sent already
email_sent = False 

awaiting_email_reply = False


# DB fetch: Get user data
def get_user_info(user_name):

    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=UEBA_Analytics;"
        "Trusted_Connection=yes;"
    )
    cursor = conn.cursor()
    cursor.execute(
        "SELECT device_id, photo_path FROM dbo.employees_profile WHERE full_name = ?",
        (user_name,),
    )
    result = cursor.fetchone()
    conn.close()
    return result if result else None


# Load known face encodings from DB


def load_encodings_from_db():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
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

    conn.close()
    return known_face_encodings, known_face_names


# ==================== INIT ====================

known_face_encodings, known_face_names = load_encodings_from_db()
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

user_present = False
verified_encoding = None
recognized_name = None
last_seen_time = None
LOCK_TIMEOUT = 15
last_presence_log = 0
PRESENCE_LOG_INTERVAL = 10
email_sent = False  # ✅ Initialize email_sent variable

print(f"🔍 Face Recognition Running on PC: {PC_NAME}")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠ Camera error.")
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)

        if not user_present:
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
            if face_encodings:
                encoding = face_encodings[0]
                face_distances = np.array(
                    face_recognition.face_distance(known_face_encodings, encoding)
                )  # ✅ Wrapped with np.array
                if face_distances.size > 0:
                    best_index = face_distances.argmin()

                    if face_distances[best_index] < 0.5:
                        recognized_name = known_face_names[best_index]
                        user_info = get_user_info(recognized_name)
                        if user_info and user_info[0] == PC_NAME:
                            print(f"✅ {recognized_name} verified for this PC.")
                            log_event(
                                "unlock", recognized_name, f"Unlocked on {PC_NAME}"
                            )
                            user_present = True
                            verified_encoding = encoding
                            last_seen_time = time.time()
                            last_presence_log = time.time()

                            # ✅ Capture user geometry once
                            landmarks = face_recognition.face_landmarks(rgb_frame)
                            if landmarks:
                                eyes = landmarks[0].get("left_eye", []) + landmarks[
                                    0
                                ].get("right_eye", [])
                                if len(eyes) >= 4:
                                    eye_x = [pt[0] for pt in eyes]
                                    eye_y = [pt[1] for pt in eyes]
                                    eye_width = max(eye_x) - min(eye_x)
                                    eye_height = max(eye_y) - min(eye_y)
                                    face_width = (
                                        face_locations[0][1] - face_locations[0][3]
                                    )
                                    face_height = (
                                        face_locations[0][2] - face_locations[0][0]
                                    )

                                    user_geometry_profile = {
                                        "eye_width": eye_width,
                                        "eye_height": eye_height,
                                        "face_width": face_width,
                                        "face_height": face_height,
                                    }
                                    print(
                                        f"📐 Geometry profile captured: {user_geometry_profile}"
                                    )
                        else:
                            print(f"❌ {recognized_name} is NOT authorized on this PC.")

                            log_event("unauthorized", recognized_name, f"Tried access on {PC_NAME}")
                            cv2.imwrite("intruder.jpg", frame)

                            if not is_alert_pending():
                                print("🚨 Unauthorized access detected. Sending email alert...")
                                send_intruder_alert("intruder.jpg", recognized_name)
                                set_alert_pending()
                                 
                           
                                decision = wait_for_owner_reply()
                                if decision=="approve":
                                     print("✅ Owner approved from email. Access allowed.")
                                     user_present = True
                                     verified_encoding = encoding
                                     last_seen_time = time.time()
                                     last_presence_log = time.time()
                                    
                                     continue
                                elif decision == "deny":
                                    print("❌ Access denied. Locking again.")
                                    os.system("rundll32.exe user32.dll,LockWorkStation")
                                    
                                    
                                else:
                                     print("⏳ No reply yet or timeout.")
                                    
                               
                                    
                    else:
                        print("❌ Unknown face.")
                        cv2.imwrite("intruder.jpg", frame)
                        send_intruder_alert("intruder.jpg", "Unknown")
            else:
                print("👤 No face detected for login.")
        else:
            current_time = time.time()

            if face_locations:
                face_ok = False
                for top, right, bottom, left in face_locations:
                    face_height = bottom - top
                    face_width = right - left
                    face_area = face_height * face_width
                    if face_area > 10000:
                        face_ok = True
                        break

                if face_ok:
                    if current_time - last_presence_log > PRESENCE_LOG_INTERVAL:
                        print("📏 User still present at expected distance.")
                        last_presence_log = current_time

                    face_encodings = face_recognition.face_encodings(
                        rgb_frame, face_locations
                    )
                    if face_encodings:
                        distance = face_recognition.face_distance(
                            [verified_encoding], face_encodings[0]
                        )[0]
                        if distance < 0.55:
                            last_seen_time = current_time
                        else:
                            print("🚨 MISMATCH: Different user! Locking immediately.")
                            log_event(
                                "intruder", recognized_name, "Face mismatch - intruder"
                            )
                            os.system("rundll32.exe user32.dll,LockWorkStation")
                            user_present = False
                            verified_encoding = None
                            recognized_name = None
                            last_seen_time = None
                            last_presence_log = 0
                            user_geometry_profile = None
                else:
                    # ❗ Try geometry fallback
                    if user_geometry_profile:
                        landmarks = face_recognition.face_landmarks(rgb_frame)
                        if landmarks:
                            eyes = landmarks[0].get("left_eye", []) + landmarks[0].get(
                                "right_eye", []
                            )
                            if len(eyes) >= 4:
                                eye_x = [pt[0] for pt in eyes]
                                eye_y = [pt[1] for pt in eyes]
                                eye_width = max(eye_x) - min(eye_x)
                                eye_height = max(eye_y) - min(eye_y)

                                match_eye_width = (abs(eye_width - user_geometry_profile["eye_width"]) < 15)
                                match_eye_height = (abs(eye_height - user_geometry_profile["eye_height"]) < 10)

                                if match_eye_width and match_eye_height:
                                    print("👁 Eye geometry matched. User still present.")
                                    last_seen_time = time.time()
                                    printed_no_face = False
                                else:
                                    if not printed_no_face:
                                        print(
                                            "👤 No face match... geometry mismatch. (waiting)"
                                        )
                                        printed_no_face = True
                            else:
                                if not printed_no_face:
                                    print("👤 No eyes visible... (waiting)")
                                    printed_no_face = True
                        else:
                            if not printed_no_face:
                                print("👤 No face landmarks detected... (waiting)")
                                printed_no_face = True

            # Check timeout regardless of face/geometry
            if last_seen_time and (time.time() - last_seen_time > LOCK_TIMEOUT):
                print("⏱ No valid presence detected. Locking...")
                log_event("lock", recognized_name, "Timeout - no presence")
                os.system("rundll32.exe user32.dll,LockWorkStation")
                user_present = False
                verified_encoding = None
                recognized_name = None
                last_seen_time = None
                last_presence_log = 0
                user_geometry_profile = None
                printed_no_face = False

        time.sleep(2)

except KeyboardInterrupt:
    print("\n🛑 Stopping system...")

finally:
    cap.release()
    cv2.destroyAllWindows()