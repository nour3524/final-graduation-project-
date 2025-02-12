import os
import pickle
import face_recognition

ENCODINGS_PATH = "encodings.pickle"

def load_encodings():
    if not os.path.exists(ENCODINGS_PATH):
        return {"encodings": [], "names": []}

    with open(ENCODINGS_PATH, "rb") as f:
        return pickle.load(f)

def save_encodings(data):
    with open(ENCODINGS_PATH, "wb") as f:
        pickle.dump(data, f)
