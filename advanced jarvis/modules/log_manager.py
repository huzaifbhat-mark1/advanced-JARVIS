from datetime import datetime
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def log_interaction(speaker, message):
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = os.path.join(LOG_DIR, f"{today}.txt")
    with open(log_file, "a", encoding="utf-8") as f:
        time_stamp = datetime.now().strftime("[%H:%M:%S]")
        f.write(f"{time_stamp} {speaker}: {message}\n")

def retrieve_logs():
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = os.path.join(LOG_DIR, f"{today}.txt")
    if os.path.exists(log_file):
        with open(log_file, "r", encoding="utf-8") as f:
            return f.read()
    return "No logs found."

def find_similar_question(query):
    from difflib import get_close_matches

    today = datetime.now().strftime("%Y-%m-%d")
    log_file = os.path.join(LOG_DIR, f"{today}.txt")
    if not os.path.exists(log_file):
        return "No logs found."

    with open(log_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    questions = [line.split("User: ")[-1].strip() for line in lines if "User: " in line]
    matches = get_close_matches(query, questions, n=1, cutoff=0.6)
    return matches[0] if matches else "I couldn't find a similar question."
