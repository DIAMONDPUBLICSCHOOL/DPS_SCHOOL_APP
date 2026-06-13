from cryptography.fernet import Fernet
import os

def log_pin_decypt(PWD):
    return Fernet(b'JxFCiezevkVZNmHWTFRztjSg8lREGJY5HGqtMar1Rq4=').decrypt(PWD).decode()
def log_pin_encrypt(PWD):
    return Fernet(b'JxFCiezevkVZNmHWTFRztjSg8lREGJY5HGqtMar1Rq4=').encrypt(PWD.encode()).decode()
def admin_log_pass():
    return os.environ.get('ADMIN_PASSWORD')






