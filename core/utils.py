import secrets
import string
from django.core.mail import EmailMessage
from django.conf import settings

def temp_password_generator(length=10):
    chars = string.ascii_letters + string.digits

    return "".join(secrets.choice(chars) for _ in range(length))

def send_notification(subject, message, to_email):
    email = EmailMessage (
            subject = subject,
            body= message,
            from_email= settings.EMAIL_DISPLAY,
            to=to_email,
        )
    
    email.send()