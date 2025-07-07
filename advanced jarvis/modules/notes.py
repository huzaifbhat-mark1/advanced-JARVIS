from modules.speech import speak
import os

NOTES_FILE = "notes.txt"

def add_note(text):
    with open(NOTES_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")
    speak("Note saved.")

def read_notes():
    if not os.path.exists(NOTES_FILE):
        speak("You have no notes.")
        return
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        notes = f.readlines()
    if notes:
        speak("Here are your notes.")
        for line in notes:
            speak(line.strip())
    else:
        speak("You have no notes.")

def delete_notes():
    if os.path.exists(NOTES_FILE):
        os.remove(NOTES_FILE)
        speak("All notes deleted.")
    else:
        speak("There are no notes to delete.")
