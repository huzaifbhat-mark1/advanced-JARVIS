from deep_translator import GoogleTranslator
from modules.speech import speak

def translate_text(text, dest_lang="en"):
    try:
        result = GoogleTranslator(source='auto', target=dest_lang).translate(text)
        print("Translated Text:", result)
        speak(result)
    except Exception as e:
        print("Translation error:", e)
        speak("Sorry, I couldn't translate that.")
