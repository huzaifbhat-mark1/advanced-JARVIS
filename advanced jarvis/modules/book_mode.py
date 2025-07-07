import time
from modules.speech import speak

def book_mode(text):
    chunks = text.split('. ')
    speak("Starting book mode.")
    for i, sentence in enumerate(chunks):
        speak(sentence.strip())
        time.sleep(1.5)  # pause between lines
