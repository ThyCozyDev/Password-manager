import PySimpleGUI as sg
import pyperclip
from functions import functions


function_instance = functions()

PASSWORDS_FILE = "passwords.txt"

passwords = functions.load_passwords_from_file(PASSWORDS_FILE)

layout = [
    [sg.Text("Password Length:"), sg.InputText(key="length")],
    [sg.Text("What are you using this for:"), sg.InputText(key="Website")],
    [sg.Button("Generate", key="button")],
    [sg.InputText(readonly=True, key="Password")],
    [sg.Text(text="Passwords")],
    [sg.Listbox(values=passwords, size=(50, 10), key="PASSWORDLIST"),
      sg.Button(button_text="Delete", key="DeleteButton")],
    [sg.Button(button_text="Copy password", key="copy_button")],
]

window = sg.Window("Password Generator", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    
    if event == "button":
        password_length = values["length"]
        website = values["Website"]
        
        # Check if password_length is a valid number
        if not password_length.isdigit():
            sg.popup_error("Please enter a valid number for password length.")
            continue
        
        password_length = int(password_length)
        
        # Check if password_length is a positive integer
        if password_length <= 0:
            sg.popup_error("Please enter a positive integer for password length.")
            continue
    
        # password generation
        GENERATED_PASSWORD = function_instance.generate_password(password_length=password_length)
        with open(PASSWORDS_FILE, "a", encoding="utf-8") as password_file:
            password_file.writelines(f"Website: {website}, Password: {GENERATED_PASSWORD}\n")
        window["Password"].update(f"Your password is: {GENERATED_PASSWORD}")
        # Update the passwords list and refresh the Listbox
        passwords.append(f"Website: {website}, Password: {GENERATED_PASSWORD}")
        window["PASSWORDLIST"].update(values=passwords)
    
    if event == "copy_button":
        selected_password = values["PASSWORDLIST"][0]
        password = selected_password.split(": ")[-1]
        pyperclip.copy(password)

    if event == "DeleteButton":
        selected_password = values["PASSWORDLIST"][0]
        function_instance.delete_password(selected_password=selected_password, passwords=passwords)
        # Update the Listbox with the new passwords list
        window["PASSWORDLIST"].update(values=passwords)

window.close()