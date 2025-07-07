from modules.speech import speak

def convert_units(command):
    try:
        if "kilometer" in command and "meter" in command:
            km = float(command.split()[0])
            speak(f"{km} kilometers is {km * 1000} meters.")
        elif "meter" in command and "kilometer" in command:
            m = float(command.split()[0])
            speak(f"{m} meters is {m / 1000} kilometers.")
        elif "kilogram" in command and "gram" in command:
            kg = float(command.split()[0])
            speak(f"{kg} kilograms is {kg * 1000} grams.")
        elif "gram" in command and "kilogram" in command:
            g = float(command.split()[0])
            speak(f"{g} grams is {g / 1000} kilograms.")
        elif "celsius" in command and "fahrenheit" in command:
            c = float(command.split()[0])
            f = (c * 9/5) + 32
            speak(f"{c} degrees Celsius is {f:.2f} degrees Fahrenheit.")
        elif "fahrenheit" in command and "celsius" in command:
            f = float(command.split()[0])
            c = (f - 32) * 5/9
            speak(f"{f} degrees Fahrenheit is {c:.2f} degrees Celsius.")
        else:
            speak("Conversion not supported.")
    except:
        speak("Sorry, I couldn't convert that.")
