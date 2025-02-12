import cv2

for i in range(5):
    cap = cv2.VideoCapture(i)
    if cap.read()[0]:
        print(f"✅ Camera detected at index {i}")
        cap.release()
    else:
        print(f"❌ No camera found at index {i}")
