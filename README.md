# AutoTyper: Automated Text Typing in Any Application

## **Overview**
The **AutoTyper** is a Python script that reads text from a file and automatically types it into any active application. It uses `PyAutoGUI` for typing simulation and `keyboard` for keypress detection.

## **Features**
- Reads text from a specified file.
- Types text into any application with a configurable speed.
- Waits for the user to press `Ctrl` before starting the typing process.
- Allows an emergency exit by pressing the `Esc` key.
- Provides a **5-second delay** to allow switching to the target application.

## **Usage**
1. **Install dependencies** (if not already installed):
   ```bash
   pip install -r requirements.txt
   

