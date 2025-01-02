import hashlib
import hmac
import os
import threading
from typing import Tuple
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import getpass
import argparse

Define a class for encryption and decryption
class Crypto:
    def __init__(self, password: str, salt: str):
        self.password = password
        self.salt = salt
        self.key = self.generate_key()

    def generate_key(self) -> bytes:
        # Generate a key using PBKDF2HMAC
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt.encode(),
            iterations=100000,
        )
        return base64.urlsafe_b64encode(kdf.derive(self.password.encode()))

    def encrypt(self, text: str) -> Tuple[str, str]:
        # Encrypt the text using Fernet
        f = Fernet(self.key)
        encrypted_text = f.encrypt(text.encode())
        return encrypted_text.decode(), self.salt

    def decrypt(self, encrypted_text: str, salt: str) -> str:
        # Decrypt the text using Fernet
        f = Fernet(self.key)
        return f.decrypt(encrypted_text.encode()).decode()

def encrypt_text(text: str, password: str) -> Tuple[str, str]:
    # Generate a random salt
    salt = os.urandom(16).hex()
    crypto = Crypto(password, salt)
    return crypto.encrypt(text)

def decrypt_text(encrypted_text: str, password: str, salt: str) -> str:
    crypto = Crypto(password, salt)
    return crypto.decrypt(encrypted_text, salt)

def main():
    parser = argparse.ArgumentParser(description="Encrypt and decrypt text")
    parser.add_argument("-e", "--encrypt", help="Encrypt text", action="store_true")
    parser.add_argument("-d", "--decrypt", help="Decrypt text", action="store_true")
    parser.add_argument("-t", "--text", help="Text to encrypt or decrypt")
    parser.add_argument("-p", "--password", help="Password for encryption and decryption")
    parser.add_argument("-s", "--salt", help="Salt for decryption")
    args = parser.parse_args()

    if args.encrypt:
        if args.text and args.password:
            encrypted_text, salt = encrypt_text(args.text, args.password)
            print(f"Encrypted text: {encrypted_text}")
            print(f"Salt: {salt}")
        else:
            print("Please provide text and password for encryption")
    elif args.decrypt:
        if args.text and args.password and args.salt:
            decrypted_text = decrypt_text(args.text, args.password, args.salt)
            print(f"Decrypted text: {decrypted_text}")
        else:
            print("Please provide encrypted text, password, and salt for decryption")

if __name__ == "__main__":
    main()
