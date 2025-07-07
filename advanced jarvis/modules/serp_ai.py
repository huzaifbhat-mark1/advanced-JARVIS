import requests

SERP_API_KEY = "0b0e877e6dccee6dd9f76d6db1faea8bd830f55b627ca960ef9a6055113d93a6"

def answer_question(question):
    url = "https://serpapi.com/search"
    params = {
        "engine": "google",
        "q": question,
        "api_key": SERP_API_KEY
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        answer = None

        if "answer_box" in data:
            box = data["answer_box"]
            if "answer" in box:
                answer = box["answer"]
            elif "snippet" in box:
                answer = box["snippet"]
            elif "definition" in box:
                answer = box["definition"]

        if not answer and "snippet" in data.get("organic_results", [{}])[0]:
            answer = data["organic_results"][0]["snippet"]

        return answer or "Sorry, I couldn't find a clear answer."
    except Exception as e:
        print("AI Error:", e)
        return "Sorry, I couldn't process that."
