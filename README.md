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
1. **Clone the repository**:
    ```bash
    git clone https://github.com/mihaiapostol14/auto_typing_text.git
    cd auto_typing_text
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies** (if not already installed):
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the AutoTyper**:
    ```bash
    python main.py
    ```

5. **Instructions**:
    - Ensure that the text file you want to be auto-typed is specified in the script.
    - Press `Ctrl` to start the auto-typing process.
    - Press `Esc` to stop the auto-typing process.

## **Contributing**
- Fork the repository.
- Create a new branch (`git checkout -b feature-branch`).
- Make your changes.
- Commit your changes (`git commit -m 'Add some feature'`).
- Push to the branch (`git push origin feature-branch`).
- Open a Pull Request.

## **License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## **Contact**
For any inquiries or issues, please contact [mihaiapostol14](https://github.com/mihaiapostol14).