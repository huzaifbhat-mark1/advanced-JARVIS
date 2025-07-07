from modules.speech import speak
import os

HISTORY_FILE = "conversation_history.txt"

def save_to_history(text):
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")

def read_history():
    if not os.path.exists(HISTORY_FILE):
        speak("No conversation history found.")
        return
    speak("Here’s your previous conversation log.")
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        for line in f.readlines()[-10:]:  # Read last 10 lines
            speak(line.strip())
