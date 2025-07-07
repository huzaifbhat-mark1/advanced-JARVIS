import PyPDF2
from modules.speech import speak

def read_pdf(file_path):
    try:
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        speak("Reading the PDF content.")
        speak(text[:1000])  # Limit to first part
    except Exception as e:
        speak("Failed to read PDF.")
        print("PDF Error:", e)
