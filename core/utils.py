import secrets
import string

def temp_password_generator(length=10):
    chars = string.ascii_letters + string.digits

    return "".join(secrets.choice(chars) for _ in range(length))