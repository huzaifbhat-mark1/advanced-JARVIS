import pyttsx3
import speech_recognition as sr

# === SETUP FOR TEXT-TO-SPEECH ===
engine = pyttsx3.init()
engine.setProperty('rate', 180)  # Speed of speaking
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Default system voice

def speak(text):
    """Speaks the given text aloud and prints it."""
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

# === SETUP FOR SPEECH-TO-TEXT ===
def listen():
    """Listens from the microphone and returns recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1

        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=6)
            command = recognizer.recognize_google(audio)
            print("You:", command)
            return command.lower()

        except sr.WaitTimeoutError:
            speak("I didn't hear anything.")
            return ""

        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""

        except sr.RequestError:
            speak("Google speech service is not available.")
            return ""
