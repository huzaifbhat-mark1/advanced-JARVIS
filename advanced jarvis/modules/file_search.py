import os
from modules.speech import speak

def search_files(filename, search_path="C:\\Users\\Admin\\Documents"):
    found = []
    for root, dirs, files in os.walk(search_path):
        for file in files:
            if filename.lower() in file.lower():
                found.append(os.path.join(root, file))
    
    if found:
        speak(f"I found {len(found)} file(s).")
        for path in found[:3]:
            speak(f"Found: {path}")
    else:
        speak("No file found with that name.")
