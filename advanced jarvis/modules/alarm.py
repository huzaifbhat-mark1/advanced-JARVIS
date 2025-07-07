import datetime
import time
from modules.speech import speak


def set_alarm(alarm_time):
    try:
        speak(f"Alarm set for {alarm_time}")
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M")
            if current_time == alarm_time:
                speak("Wake up! Alarm time reached.")
                break
            time.sleep(10)
    except Exception as e:
        speak("Failed to set alarm.")
        print(e)
