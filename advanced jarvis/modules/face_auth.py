import cv2
import os

def face_authenticate():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("face_model.yml")
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    cam = cv2.VideoCapture(0)
    authorized = False

    print("Scanning face. Please look at the camera...")

    for _ in range(100):
        ret, frame = cam.read()
        if not ret:
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            id_, confidence = recognizer.predict(gray[y:y+h, x:x+w])
            if confidence < 60:  # lower confidence = more accurate
                authorized = True
                break

        if authorized:
            break

    cam.release()
    cv2.destroyAllWindows()
    return authorized
