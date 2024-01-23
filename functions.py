import string
import random
import json


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
        
    def delete_password(self, selected_password, passwords):
        """
        Delete a selected password from the list and update the passwords file.
        """
        # Remove the selected password from the list
        if selected_password in passwords:
            passwords.remove(selected_password)

        # Update the passwords file
        with open("passwords.txt", "w", encoding="utf-8") as password_file:
            for password in passwords:
                password_file.write(password + "\n")      
                
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