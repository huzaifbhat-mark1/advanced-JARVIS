from modules.speech import speak
import re

def calculate(expression):
    try:
        expression = expression.replace("x", "*").replace("X", "*").replace("÷", "/")
        expression = re.sub(r'[^\d\+\-\*/\.\(\) ]', '', expression)
        result = eval(expression)
        speak(f"The result is {result}")
    except Exception:
        speak("Sorry, I couldn't calculate that.")
