import smtplib
from config import settings
from email.mime.text import MIMEText


def send(user_email, user_name, choosen_cars):
    sender = settings.EMAIL_USER
    password = settings.EMAIL_PASSWORD
    message = message_generator(user_name, choosen_cars)

    server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg['Subject'] = 'YOUR RESERVED CARS'
        server.sendmail(sender, user_email, msg.as_string())
        return "Message sent"
    except Exception as _ex:
        return f"{_ex}\nCheck your data {sender}"


#  Герерация текста сообщения
def message_generator(user_name, choosen_cars):
    cars = ''
    for car in choosen_cars:
        cars += car + '\n'
    message = f"Hi, {user_name}!\nThis is your cars:\n{cars}\nWe'll contact you soon for terms and conditions!"
    return message

