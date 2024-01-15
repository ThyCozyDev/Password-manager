import random
import string
import PySimpleGUI as sg
import pyperclip
def generate_password(length):
    """
    Generate a random password of the specified length.
    """
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    all_chars = uppercase_letters + lowercase_letters + digits + special_chars

    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

def load_passwords_from_file(filename="passwords.txt"):
    """
    Load passwords from a file.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

PASSWORDS_FILE = "passwords.txt"

passwords = load_passwords_from_file(PASSWORDS_FILE)

layout = [
    [sg.Text("Password Length:"), sg.InputText(key="length")],
    [sg.Text("What are you using this for:"), sg.InputText(key="Website")],
    [sg.Button("Generate", key="button")],
    [sg.InputText(readonly=True, key="Password")],
    [sg.Text(text="Passwords")],
    [sg.Listbox(values=passwords, size=(50, 10), key="PASSWORDLIST")],
    [sg.Button(button_text="Copy password", key="copy_button")],
]

window = sg.Window("Password Generator", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "button":
        length = values["length"]
        website = values["Website"]
        length = int(length)
        
        # Check if length is a positive integer
        if length <= 0:
            sg.popup_error("Please enter a positive integer for password length.")
            continue
        
        # password generation
        generated_password = generate_password(length)
        with open(PASSWORDS_FILE, "a", encoding="utf-8") as file:
            file.writelines(f"Website: {website}, Password: {generated_password}\n")
        window["Password"].update(f"Your password is: {generated_password}")
        # Update the passwords list and refresh the Listbox
        passwords.append(f"Website: {website}, Password: {generated_password}")
        window["PASSWORDLIST"].update(values=passwords)
    
    if event == "copy_button":
        selected_password = values["PASSWORDLIST"][0]
        password = selected_password.split(": ")[-1]
        pyperclip.copy(password)

window.close()
