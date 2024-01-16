import string
import random


class functions():

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
        