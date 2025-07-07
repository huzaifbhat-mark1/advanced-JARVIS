import cv2
import os
import numpy as np

def train():
    cam = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    data_path = "face_data"
    os.makedirs(data_path, exist_ok=True)
    count = 0

    print("Capturing your face. Look at the camera...")

    while count < 50:
        ret, frame = cam.read()
        if not ret:
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            count += 1
            face = gray[y:y+h, x:x+w]
            cv2.imwrite(f"{data_path}/user.{count}.jpg", face)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow("Capturing...", frame)
        if cv2.waitKey(1) == 27:
            break

    cam.release()
    cv2.destroyAllWindows()

    # Train model
    faces = []
    labels = []
    files = os.listdir(data_path)
    for file in files:
        img = cv2.imread(f"{data_path}/{file}", cv2.IMREAD_GRAYSCALE)
        faces.append(img)
        labels.append(1)  # 1 for authorized user

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(faces, np.array(labels))
    recognizer.save("face_model.yml")

    print("Face training complete.")

if __name__ == "__main__":
    train()
