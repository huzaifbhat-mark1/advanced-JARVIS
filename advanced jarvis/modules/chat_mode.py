
from modules.speech import speak, listen
from modules.serp_ai import answer_question
import time

def chat_with_ai():
    speak("Chat mode activated. You can now talk with me like a conversation. Say 'exit chat' to stop.")
    while True:
        speak("What's your question?")
        question = listen()
        if "exit chat" in question or "stop chat" in question:
            speak("Exiting chat mode.")
            break
        elif question.strip() == "":
            speak("I didn't hear any question. Please ask again.")
            continue
        else:
            answer = answer_question(question)
            if answer:
                speak(answer)
            else:
                speak("Sorry, I couldn't process that.")
            time.sleep(1)
