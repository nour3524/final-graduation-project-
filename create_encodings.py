import face_recognition
import pickle
import os

ENCODINGS_PATH = "encodings.pickle"
KNOWN_FACES_DIR = "images"

known_face_encodings = []
known_face_names = []

for filename in os.listdir(KNOWN_FACES_DIR):
    image_path = os.path.join(KNOWN_FACES_DIR, filename)
    image = face_recognition.load_image_file(image_path)
    
    encodings = face_recognition.face_encodings(image)
    if encodings:
        known_face_encodings.append(encodings[0])
        known_face_names.append(os.path.splitext(filename)[0])

data = {"encodings": known_face_encodings, "names": known_face_names}
with open(ENCODINGS_PATH, "wb") as f:
    pickle.dump(data, f)

print(f"Encodings saved to {ENCODINGS_PATH}")