# modules/photo_capture.py

import cv2
import os
from datetime import datetime


def capture_and_save_photo():
    try:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            return "Could not open webcam."

        ret, frame = cap.read()
        cap.release()

        if not ret:
            return "Failed to capture image."

        # Create the photos directory if it doesn't exist
        folder = "photos"
        os.makedirs(folder, exist_ok=True)

        # Save image with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{folder}/photo_{timestamp}.jpg"
        cv2.imwrite(filename, frame)

        return f"Photo saved as {filename}"

    except Exception as e:
        return f"Error: {str(e)}"
