# modules/brain_booster.py

import random
from modules.speech import speak, listen

questions = [
    ("What is the capital of India?", "new delhi"),
    ("Who invented the light bulb?", "thomas edison"),
    ("What is the square root of 64?", "8"),
    ("What gas do plants absorb from the atmosphere?", "carbon dioxide"),
    ("Which planet is known as the Red Planet?", "mars"),
    ("What is H2O commonly known as?", "water"),
    ("Who is known as the father of computers?", "charles babbage"),
    ("How many continents are there?", "7"),
    ("What is 15 multiplied by 3?", "45"),
    ("Which language is used to build Android apps?", "java")
]

def start_brain_booster():
    speak("Let's begin your brain booster session.")
    score = 0

    for i in range(5):
        q, a = random.choice(questions)
        speak(f"Question {i+1}: {q}")
        answer = listen().lower()

        if a in answer:
            speak("Correct!")
            score += 1
        else:
            speak(f"Wrong. The correct answer is {a}.")

    speak(f"You got {score} out of 5 correct. Well done!")
