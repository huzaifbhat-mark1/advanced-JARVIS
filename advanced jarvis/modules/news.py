import requests
from modules.speech import speak

API_KEY = "b2e85b5686724532b9c749094bad7cb7"  # 🔁 Get from https://newsapi.org

def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        articles = data.get("articles", [])[:5]
        speak("Here are the top headlines.")
        for i, article in enumerate(articles):
            speak(f"Headline {i+1}: {article['title']}")
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't fetch the news.")
