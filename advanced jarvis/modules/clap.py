import numpy as np
import sounddevice as sd
from modules.speech import speak

def clap_listener():
    def audio_callback(indata, frames, time, status):
        volume_norm = np.linalg.norm(indata) * 10
        if volume_norm > 8:  # Adjust sensitivity here
            print("👏 Clap detected!")
            speak("Yes? I heard a clap. What should I do?")
    with sd.InputStream(callback=audio_callback):
        print("Clap listener started.")
        sd.sleep(10000)  # Listens for 10 seconds
