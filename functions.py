import string
import random
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import os


class PasswordFunctions:

    def generate_password(self, password_length):
        """
        Generate a random password of the specified length.
        """
        uppercase_letters = string.ascii_uppercase
        lowercase_letters = string.ascii_lowercase
        digits = string.digits
        special_chars = string.punctuation

        all_chars = uppercase_letters + lowercase_letters + digits + special_chars

        password = ''.join(random.choice(all_chars) for _ in range(password_length))

        return password

    def load_passwords_from_file(self, filename="passwords.txt"):
        """
        Load passwords from a file.
        """
        try:
            with open(filename, "r", encoding="utf-8") as password_file:
                return [line.strip() for line in password_file.readlines()]
        except FileNotFoundError:
            return []
        
    def encrypt_passwords(self, passwords, key):
        cipher = AES.new(key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(passwords.encode('utf-8'), AES.block_size))
        iv = cipher.iv
        return iv + ct_bytes

    def decrypt_passwords(self, encrypted_data, key):
        iv = encrypted_data[:16]
        ct = encrypted_data[16:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return pt.decode('utf-8')

    def save_passwords_to_file(self, passwords, filename="passwords.aes"):
        key = self.load_encryption_key()
        # Join the passwords list into a single string separated by newlines
        passwords_str = "\n".join(passwords)
        encrypted_data = self.encrypt_passwords(passwords_str, key)
        with open(filename, "wb") as password_file:
            password_file.write(encrypted_data)

    def load_passwords_from_file(self, filename="passwords.aes"):
        key = self.load_encryption_key()
        try:
            with open(filename, "rb") as password_file:
                encrypted_data = password_file.read()
            passwords_str = self.decrypt_passwords(encrypted_data, key)
            return passwords_str.split("\n")
        except FileNotFoundError:
            return []

    def load_encryption_key(self, key_file=".encryption_key"):
        try:
            with open(key_file, "rb") as key_file:
                key = key_file.read()
        except FileNotFoundError:
            key = get_random_bytes(16)
            with open(key_file, "wb") as key_file:
                key_file.write(key)
                # Hide the key file if on Windows
                if os.name == 'nt':
                    os.system(f"attrib +h {key_file.name}")
        return key
    
    def delete_password(self, selected_password, passwords):
        """
        Delete a selected password from the list and update the passwords file.
        """
        # Remove the selected password from the list
        if selected_password in passwords:
            passwords.remove(selected_password)
            # Update the passwords file
            self.save_passwords_to_file(passwords, "passwords.aes")
    CONFIG_FILE = "config.json"

    def save_theme(self, theme_name):
        with open('config.json', 'w', encoding='utf-8') as config_file:
            json.dump({'theme': theme_name}, config_file)

    def load_theme(self):
        try:
            with open('config.json', 'r', encoding='utf-8') as config_file:
                config = json.load(config_file)
                return config.get('theme', 'Fusion')  # Default to 'Fusion' if not set
        except FileNotFoundError:
            return 'Fusion'  # Default to 'Fusion' if config file does not exist