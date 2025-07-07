import psutil
from modules.speech import speak


def get_battery_status():
    battery = psutil.sensors_battery()
    if battery is None:
        speak("Sorry, I couldn't get battery information.")
        return

    percent = battery.percent
    is_plugged = battery.power_plugged

    status = f"Battery is at {percent} percent."
    if is_plugged:
        status += " It is charging."
    else:
        status += " It is not charging."

    speak(status)
