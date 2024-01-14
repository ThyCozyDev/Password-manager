import random
import string
import PySimpleGUI as sg


def generate_password(length):
    """
    Generate a random password.

    Args:
        length (int): The length of the password.

    Returns:
        str: The generated password.
    """
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    all_chars = uppercase_letters + lowercase_letters + digits + special_chars

    length = max(8, length)

    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password


layout = [
    [sg.Text("Password Length:"), sg.InputText(key="length")],
    [sg.Text("What are you using this for:"), sg.InputText(key="Website")],
    [sg.Button("Generate", key="button")],
    [sg.InputText(readonly=True, key="Password")]
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
        # password generation
        generated_password = generate_password(length)
        with open("password.txt", "a", encoding="utf-8") as file:
            file.writelines(f"Website: {website}, Password: {generated_password}\n")
        window["Password"].update(f"Your password is: {generated_password}")


window.close()
