import pywhatkit
import wikipedia
import datetime
import os
import webbrowser
from modules.speech import speak

def search_wikipedia(query):
    speak("Searching Wikipedia...")
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
    except Exception:
        speak("Sorry, I couldn't find anything on Wikipedia.")

def play_youtube(query):
    speak(f"Playing {query} on YouTube...")
    pywhatkit.playonyt(query)

def search_google(query):
    speak(f"Searching Google for {query}...")
    pywhatkit.search(query)

def tell_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {now}")

def open_app(app_name):
    speak(f"Opening {app_name}")
    if "chrome" in app_name:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    elif "notepad" in app_name:
        os.system("notepad")
    else:
        speak("I don't know how to open that app yet.")


import requests
from modules.config import OPENWEATHER_API_KEY
import datetime

def get_weather(city):
    try:
        speak(f"Getting weather for {city}")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            speak("City not found.")
            return

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        speak(f"It is currently {temp}°C with {desc} in {city}. Humidity is {humidity} percent and wind speed is {wind} kilometers per hour.")
    except Exception as e:
        speak("Sorry, I couldn't get the weather.")

def get_today_date():
    today = datetime.datetime.now()
    speak(f"Today is {today.strftime('%A, %d %B %Y')}.")

def get_current_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {now}")

    import webbrowser
import os
from modules.speech import speak

def open_app(app_name):
    app_name = app_name.lower()
    
    # === WEB APPS ===
    if "youtube" in app_name:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "google" in app_name:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif "gmail" in app_name:
        speak("Opening Gmail.")
        webbrowser.open("https://mail.google.com")

    # === WINDOWS APPS ===
    elif "notepad" in app_name:
        speak("Opening Notepad.")
        os.system("start notepad")

    elif "chrome" in app_name:
        speak("Opening Google Chrome.")
        os.system("start chrome")

    elif "command prompt" in app_name or "cmd" in app_name:
        speak("Opening Command Prompt.")
        os.system("start cmd")

    elif "calculator" in app_name:
        speak("Opening Calculator.")
        os.system("start calc")

    else:
        speak("Sorry, I don't know how to open that app.")


