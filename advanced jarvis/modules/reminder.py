from modules.speech import speak
import os

REMINDER_FILE = "reminders.txt"


def add_reminder(text):
    with open(REMINDER_FILE, "a") as f:
        f.write(text + "\n")
    speak("Reminder saved.")


def read_reminders():
    if not os.path.exists(REMINDER_FILE):
        speak("You have no reminders.")
        return
    with open(REMINDER_FILE, "r") as f:
        reminders = f.readlines()
    if reminders:
        speak("Here are your reminders.")
        for line in reminders:
            speak(line.strip())
    else:
        speak("You have no reminders.")
