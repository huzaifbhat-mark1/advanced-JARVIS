import smtplib
from modules.speech import speak

EMAIL = "suhaibabe964@gmail.com"       # 🔁 replace with your email
APP_PASSWORD = "bbfy oeve qpcz xxix"   # 🔁 replace with app password

def send_email(to, subject, body):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL, APP_PASSWORD)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(EMAIL, to, message)
        server.quit()
        speak("Email has been sent successfully.")
    except Exception as e:
        print("Email error:", e)
        speak("Sorry, I couldn't send the email.")
