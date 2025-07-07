# modules/photo_tools.py

import cv2
import os
from datetime import datetime

PHOTO_DIR = "photos"
os.makedirs(PHOTO_DIR, exist_ok=True)

def capture_photo():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return "Webcam not accessible."

    ret, frame = cap.read()
    cap.release()

    if ret:
        filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"
        filepath = os.path.join(PHOTO_DIR, filename)
        cv2.imwrite(filepath, frame)
        return f"Photo captured and saved as {filename}"
    else:
        return "Failed to capture photo."
