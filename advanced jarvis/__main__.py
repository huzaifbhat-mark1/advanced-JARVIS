from getpass import getpass
from datetime import datetime
from modules.speech import speak, listen
from modules.tasks import (
    search_wikipedia, play_youtube, search_google,
    tell_time, get_today_date, get_weather, open_app
)
from modules.clap import clap_listener
from modules.day5_tools import (
    take_screenshot, write_to_file, read_file,
    open_folder, show_webcam
)
from modules.email_bot import send_email
from modules.alarm import set_alarm
from modules.reminder import add_reminder, read_reminders
from modules.news import get_news
from modules.battery import get_battery_status
from modules.history import save_to_history, read_history
from modules.calculator import calculate
from modules.converter import convert_units
from modules.notes import add_note, read_notes, delete_notes
from modules.music import play_random_music
from modules.file_search import search_files
from modules.translate import translate_text
from modules.ocr_reader import read_text_from_image
from modules.pdf_reader import read_pdf
from modules.book_mode import book_mode
from modules.serp_ai import answer_question  # Day 13: SerpAPI Answer
from modules.chat_mode import chat_with_ai  # Day 15: Chat Mode
from modules.memory import save_memory, read_memory, clear_memory  # Day 16
from modules.log_manager import (
    log_interaction, retrieve_logs, find_similar_question  # Day 17
)
from modules.photo_capture import capture_and_save_photo  # Day 18
from modules.brain_booster import start_brain_booster  # Day 19

# ========== SETTINGS ==========
USE_CLAP_WAKE = False
WAKE_WORD = "jarvis"

# ========== AUTHENTICATION ==========


def authenticate():
    password = "jarvis123"
    for _ in range(3):
        entered = getpass("Enter password to activate JARVIS: ")
        if entered == password:
            print("Access granted.")
            return True
        else:
            print("Access denied.")
    return False

# ========== WAKE WORD ==========


def is_wake_word(text):
    return WAKE_WORD in text.lower()


# ========== MAIN ==========
if __name__ == "__main__":
    if not authenticate():
        exit()

    speak("JARVIS is online. Say 'Hey Jarvis' to activate.")

    while True:
        try:
            if USE_CLAP_WAKE:
                clap_listener()
                speak("Yes? I heard a clap. What should I do?")
            else:
                command = listen()
                if not is_wake_word(command):
                    continue
                speak("Yes Huzaif, I am listening...")

            command = listen()
            print("Command received:", command)
            save_to_history("You: " + command)
            log_interaction("User", command)

            if not command.strip():
                continue

            # === Day 1–2 ===
            if "stop" in command or "exit" in command:
                speak("Goodbye.")
                log_interaction("JARVIS", "Goodbye.")
                break

            elif "wikipedia" in command:
                query = command.replace("wikipedia", "").strip()
                result = search_wikipedia(query)
                log_interaction("JARVIS", result)

            elif "play" in command:
                query = command.replace("play", "").strip()
                play_youtube(query)

            elif "search" in command:
                query = command.replace("search", "").strip()
                search_google(query)

            elif "time" in command:
                tell_time()

            elif "date" in command:
                get_today_date()

            elif "weather" in command:
                speak("Which city?")
                city = listen()
                get_weather(city)

            # === Day 5: Tools ===
            elif "webcam" in command:
                show_webcam()

            elif "screenshot" in command:
                take_screenshot()

            elif "write to file" in command:
                speak("What should I write?")
                content = listen()
                speak("What filename should I save it as?")
                filename = listen().replace(" ", "_") + ".txt"
                write_to_file(filename, content)

            elif "read file" in command:
                speak("What file should I read?")
                filename = listen().replace(" ", "_") + ".txt"
                read_file(filename)

            elif "open folder" in command:
                open_folder()

            elif "open" in command:
                app_name = command.replace("open", "").strip()
                open_app(app_name)

            # === Day 6 ===
            elif "send email" in command:
                speak("Who is the receiver's email?")
                to = listen()
                speak("What should the subject be?")
                subject = listen()
                speak("What should I say in the email?")
                body = listen()
                send_email(to, subject, body)

            elif "set alarm" in command:
                speak("At what time should I set the alarm? Say like 14:30")
                alarm_time = listen()
                set_alarm(alarm_time)

            elif "add reminder" in command:
                speak("What should I remind you about?")
                text = listen()
                add_reminder(text)

            elif "read reminders" in command:
                read_reminders()

            elif "news" in command or "headlines" in command:
                get_news()

            # === Day 7 ===
            elif "battery" in command:
                get_battery_status()

            elif "read history" in command or "conversation history" in command:
                read_history()

            # === Day 8 ===
            elif "calculate" in command:
                speak("What do you want to calculate?")
                expression = listen()
                calculate(expression)

            elif "convert" in command or "conversion" in command:
                speak("What do you want to convert?")
                conversion = listen()
                convert_units(conversion)

            elif "add note" in command:
                speak("What should I note down?")
                note = listen()
                add_note(note)

            elif "read notes" in command:
                read_notes()

            elif "delete notes" in command:
                delete_notes()

            # === Day 9 ===
            elif "play music" in command:
                play_random_music()

            elif "find file" in command or "search file" in command:
                speak("What is the filename?")
                filename = listen()
                search_files(filename)

            elif "translate" in command:
                speak("What do you want to translate?")
                text = listen()
                speak("Which language? Say 'Hindi' or 'English'.")
                lang = listen()
                if "hindi" in lang:
                    translate_text(text, dest_lang="hi")
                elif "english" in lang:
                    translate_text(text, dest_lang="en")
                else:
                    speak("I only support Hindi and English for now.")

            # === Day 10 ===
            elif "read screenshot" in command or "read image" in command:
                speak("Reading the latest screenshot or image...")
                read_text_from_image()

            elif "read pdf" in command:
                speak("Please say the filename of the PDF in your folder.")
                filename = listen().replace(" ", "_") + ".pdf"
                read_pdf(filename)

            elif "book mode" in command:
                speak("What text should I read like a book?")
                long_text = listen()
                book_mode(long_text)

            # === Day 13: SerpAPI Answer ===
            elif "answer me" in command or "ask ai" in command:
                speak("What's your question?")
                question = listen()
                if question:
                    answer = answer_question(question)
                    speak(answer)
                    save_memory(question, answer)
                    log_interaction("JARVIS", answer)

            # === Day 15: Chat Mode ===
            elif "let's chat" in command or "chat mode" in command:
                speak("Entering chat mode. Say 'exit chat' to quit.")
                chat_with_ai()

            # === Day 16: Memory Commands ===
            elif "recall memory" in command or "show memory" in command:
                memory = read_memory()
                speak("Here is what I remember.")
                print(memory)

            elif "clear memory" in command:
                response = clear_memory()
                speak(response)

            # === Day 17: Smart Recall ===
            elif "old question" in command or "previous question" in command:
                speak("What was the old question?")
                query = listen()
                result = find_similar_question(query)
                speak(result)

            elif "show logs" in command:
                logs = retrieve_logs()
                speak("Showing today's conversation logs.")
                print(logs)

            # === Day 18: Photo Capture ===
            elif "click photo" in command or "take photo" in command:
                capture_and_save_photo()

            # === Day 19: Brain Booster ===
            elif "brain booster" in command:
                start_brain_booster()

            else:
                speak("I didn't understand that. Can you repeat?")
                log_interaction("JARVIS", "I didn't understand that.")
        except Exception as e:
            print("Error:", e)
            speak("Something went wrong.")
