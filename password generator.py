import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QListWidget, QMessageBox, QComboBox, QStyleFactory
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QClipboard, QIcon
from functions import PasswordFunctions

PASSWORDS_FILE = "passwords.txt"
function_instance = PasswordFunctions()
passwords = function_instance.load_passwords_from_file(PASSWORDS_FILE)

class PasswordManager(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Password Generator")
        self.setWindowIcon(QIcon('icon.png'))


        # Layouts
        main_layout = QVBoxLayout()
        form_layout = QHBoxLayout()
        buttons_layout = QHBoxLayout()
        list_layout = QHBoxLayout()

        # Widgets
        self.length_label = QLabel("Password Length:")
        self.length_input = QLineEdit()
        self.website_label = QLabel("What are you using this for:")
        self.website_input = QLineEdit()
        self.generate_button = QPushButton("Generate")
        self.password_output = QLineEdit()
        self.password_output.setReadOnly(True)
        self.password_list = QListWidget()
        self.delete_button = QPushButton("Delete")
        self.copy_button = QPushButton("Copy password")
        self.theme_combobox = QComboBox()

        # Populate the theme combobox
        self.theme_combobox.addItems(self.available_themes())

        # Set up the form layout
        form_layout.addWidget(self.length_label)
        form_layout.addWidget(self.length_input)
        form_layout.addWidget(self.website_label)
        form_layout.addWidget(self.website_input)

        # Set up the buttons layout
        buttons_layout.addWidget(self.generate_button)
        buttons_layout.addWidget(self.copy_button)
        buttons_layout.addWidget(self.theme_combobox)

        # Set up the list layout
        list_layout.addWidget(self.password_list)
        list_layout.addWidget(self.delete_button)

        # Add widgets to the main layout
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.password_output)
        main_layout.addLayout(buttons_layout)
        main_layout.addLayout(list_layout)

        # Set the main layout
        self.setLayout(main_layout)

        # Signals
        self.generate_button.clicked.connect(self.generate_password)
        self.copy_button.clicked.connect(self.copy_password)
        self.delete_button.clicked.connect(self.delete_password)
        self.theme_combobox.currentTextChanged.connect(self.change_theme)

        # Load passwords into the list
        self.update_password_list()

    def available_themes(self):
        # This function should return the list of available themes
        # For now, we'll just return a placeholder list
        return QStyleFactory.keys()

    def generate_password(self):
        password_length = self.length_input.text()
        website = self.website_input.text()

        # Check if password_length is a valid number
        if not password_length.isdigit():
            QMessageBox.critical(self, "Error", "Please enter a valid number for password length.")
            return

        password_length = int(password_length)

        # Check if password_length is a positive integer
        if password_length <= 0:
            QMessageBox.critical(self, "Error", "Please enter a positive integer for password length.")
            return

        # Generate the password
        generated_password = function_instance.generate_password(password_length=password_length)
        self.password_output.setText(f"Your password is: {generated_password}")

        # Save the password
        with open(PASSWORDS_FILE, "a", encoding="utf-8") as password_file:
            password_file.write(f"Website: {website}, Password: {generated_password}\n")

        # Update the password list
        passwords.append(f"Website: {website}, Password: {generated_password}")
        self.update_password_list()

    def copy_password(self):
        selected_items = self.password_list.selectedItems()
        if selected_items:
            password = selected_items[0].text().split(": ")[-1]
            clipboard = QApplication.clipboard()
            clipboard.setText(password)
            QMessageBox.information(self, "Copied", "Password has been copied to clipboard.")

    def delete_password(self):
        selected_items = self.password_list.selectedItems()
        if selected_items:
            selected_password = selected_items[0].text()
            function_instance.delete_password(selected_password=selected_password, passwords=passwords)
            self.update_password_list()

    def change_theme(self, theme_name):
        # This method should change the theme of the application
        QApplication.setStyle(QStyleFactory.create(theme_name))
        function_instance.save_theme(theme_name)  # Save the selected theme

    def update_password_list(self):
        self.password_list.clear()
        self.password_list.addItems(passwords)

# Main application code
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Load the saved theme or default to 'Fusion'
    saved_theme = function_instance.load_theme()
    app.setStyle(QStyleFactory.create(saved_theme))
    
    password_manager = PasswordManager()
    password_manager.show()
    sys.exit(app.exec())