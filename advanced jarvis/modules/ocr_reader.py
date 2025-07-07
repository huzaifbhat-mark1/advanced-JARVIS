import pytesseract
from PIL import Image
from modules.speech import speak

def read_text_from_image(image_path="screenshot.png"):
    try:
        text = pytesseract.image_to_string(Image.open(image_path))
        if text:
            speak("Here's the text I found.")
            speak(text)
        else:
            speak("No readable text found in the image.")
    except Exception as e:
        speak("Failed to read the image.")
        print("OCR Error:", e)
