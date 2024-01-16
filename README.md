## Password Generator

A simple password Generator built with Python and PySimpleGUI.

## Description

This password generator script provides a graphical user interface to generate strong, random passwords based on user-defined length and character sets, including uppercase and lowercase letters, digits, and special characters.

## Features

- Generate strong random passwords.
- Customize password length.
- Save generated passwords with associated usage (e.g., website or application) to a text file.

## Requirements

- Python 3.x
- PySimpleGUI
- pyperclip

## Installation

Before running the script, you need to install the required Python package if you haven't already:

PySimpleGui

```bash
pip install PySimpleGUI
```

pyperclip

```bash
pip install pyperclip
```

## Usage

To use the password generator, run the `pass manager.py` script:

```bash
python "PATH_TO_SCRIPT\password generator.py"
```

or:

```bash
python3 "PATH_TO_SCRIPT\password generator.py"
```

The GUI will prompt you to enter the desired password length and the purpose for which the password is being generated (e.g., the name of a website or application). After clicking the "Generate" button, the password will be displayed and saved to a file named `password.txt`. You can access the passwords from the list and copy them by clicking on the Copy button (You need to select a password first!). You cna delete a password by selecting the desired one in the list and then pressing on the delete button.

## Updates

1.2:

* Added a delete button to delete unwanted or mistakenly generated passwords
* Improved the redability of the code
* Improved Error Handling

1.1:

* Added a list that shows the generated passwords.
* Added a Copy button to copy the selected password from the list.

## Disclaimer

This script is for educational purposes only. Please ensure that you store and manage your passwords securely.
