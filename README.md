## Password Manager

A robust password manager built with Python.

## Description

This password manager application provides a graphical user interface to generate strong, random passwords based on user-defined length and character sets, including uppercase and lowercase letters, digits, and special characters. It allows users to save generated passwords with associated usage (e.g., website or application) to a .aes encrypted file and manage them through the interface.

## Features

- Generate strong random passwords with a customizable length.
- Save generated passwords with associated usage to a text file.
- Copy passwords to the clipboard.
- Delete passwords from the list.
- Change the application theme.

## Requirements

- Python 3.x
- PyQt6
- pycryptodome

## Installation

Before running the application, you need to install the required Python package if you haven't already:

(If the `py` command doesn't work try `python` or `python3`)

PyQt6:

```bash
py -m pip install PyQt6
```

pycryptodome:

```bash
py -m pip install pycryptodome
```

## Usage

To use the password manager, run the `password generator.py` script:

```bash
python "PATH_TO_SCRIPT\password generator.py"
```

or:

```bash
python3 "PATH_TO_SCRIPT\password generator.py"
```

The GUI will prompt you to enter the desired password length and the purpose for which the password is being generated (e.g., the name of a website or application). After clicking the "Generate" button, the password will be displayed and saved to an encrypted file named `passwords.aes`. You can access the passwords from the list, copy them to the clipboard, and delete them as needed.

## Updates

2.1:

* Made the passwords encrypt with AES encryption.

2.0:

* Changed the entire GUI library from PySimpleGui to PyQt6.
* Added the save_theme and load_theme function so it remembers the selected theme.

1.3:

* Added a Themes dropdown to change the application's theme.
* Implemented theme persistence across sessions.

1.2:

* Added a delete button to remove unwanted or mistakenly generated passwords.
* Improved the readability of the code.
* Improved error handling.

1.1:

* Added a list to display generated passwords.
* Added a Copy button to copy the selected password from the list.

## Disclaimer

This application is for educational purposes only. Please ensure that you store and manage your passwords securely.
