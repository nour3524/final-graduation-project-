import cv2
import face_recognition
import pickle
import os

ENCODINGS_PATH = "encodings.pickle"

# Load known encodings
with open(ENCODINGS_PATH, "rb") as f:
    data = pickle.load(f)

known_face_encodings = data["encodings"]
known_face_names = data["names"]

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Use DirectShow to access the camera



while True:
    ret, frame = cap.read()
    if not ret:
        continue
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        if True in matches:
            print("✅ User Recognized")
        else:
            print("❌ Unknown User")

cap.release()
cv2.destroyAllWindows()
