import os
import pyautogui
import datetime
import cv2
from modules.speech import speak

# === TAKE SCREENSHOT ===
def take_screenshot():
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshot_{now}.png"
    filepath = os.path.join(os.getcwd(), filename)
    image = pyautogui.screenshot()
    image.save(filepath)
    speak(f"Screenshot saved as {filename}")

# === WRITE TO FILE ===
def write_to_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)
    speak(f"I've written the content to {filename}")

# === READ FROM FILE ===
def read_file(filename):
    if not os.path.exists(filename):
        speak("That file does not exist.")
        return
    with open(filename, 'r') as f:
        content = f.read()
    print("File content:\n", content)
    speak("Here's what I found in the file.")
    speak(content)

# === OPEN FOLDER EXPLORER ===
def open_folder(path=None):
    if path is None:
        path = os.getcwd()
    speak(f"Opening folder {path}")
    os.startfile(path)

# === SHOW WEBCAM ===
def show_webcam():
    speak("Opening webcam. Press Q to quit.")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        speak("Sorry, I couldn't access the webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("JARVIS Webcam", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    speak("Webcam closed.")
