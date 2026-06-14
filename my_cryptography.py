from cryptography.fernet import Fernet
import os

def log_pin_decypt(PWD):
    return Fernet(bytes(os.environ.get('LOGIN_PIN'))).decrypt(PWD).decode()
def log_pin_encrypt(PWD):
    return Fernet(bytes(os.environ.get('LOGIN_PIN'))).encrypt(PWD.encode()).decode()
def admin_log_pass():
    return os.environ.get('ADMIN_PASSWORD')






