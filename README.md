# Automation with pywinauto and pyautogui

This project demonstrates how to use `pywinauto` and `pyautogui` for automating Windows applications using Python. The combination of these libraries allows for robust GUI automation, including window interactions and GUI element manipulations.

## Introduction
`pywinauto` is a set of Python modules to automate the Microsoft Windows GUI. `pyautogui` lets Python control the mouse and keyboard to automate interactions with the screen. Together, these libraries provide a powerful toolkit for automating GUI tasks on Windows systems.

## Prerequisites
- Python 3.6 or higher
- Windows operating system

## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/automation-pywinauto-pyautogui.git
    cd automation-pywinauto-pyautogui
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To start automating, you can use the sample scripts provided or create your own scripts. Below are a few examples to get you started.

### Sample Scripts

#### Automating Notepad with pywinauto
```python
import pywinauto

# Launch Notepad
app = pywinauto.Application().start("notepad.exe")

# Type some text into Notepad
dlg = app.UntitledNotepad
dlg.Edit.type_keys("Hello, pywinauto!", with_spaces=True)
