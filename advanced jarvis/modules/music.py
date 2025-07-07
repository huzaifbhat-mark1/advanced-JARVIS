import os
import random
from modules.speech import speak

MUSIC_DIR = "C:\\Users\\Admin\\Music"  # 🔁 Change to your music folder


def play_random_music():
    try:
        songs = [f for f in os.listdir(
            MUSIC_DIR) if f.endswith((".mp3", ".wav"))]
        if not songs:
            speak("No songs found in your music folder.")
            return
        song = random.choice(songs)
        os.startfile(os.path.join(MUSIC_DIR, song))
        speak(f"Playing {song}")
    except Exception as e:
        speak("I couldn't play music.")
        print("Music Error:", e)
