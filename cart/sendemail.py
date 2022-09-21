import smtplib
import os
from config import settings


def send_email():
    sender = settings.EMAIL_USER
    password = settings.EMAIL_PASSWORD

    server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, sender, f"Subject{sender}")
        return "Message sent"
    except Exception as _ex:
        return f"{_ex}\nCheck your data {sender}"


print(send_email())
