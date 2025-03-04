# Auto Typing Text

## Overview

`auto_typing_text` is a Python utility that automates typing text from a file into any application of your choice. It leverages the `pynput` library to simulate keyboard input, allowing you to "type" large amounts of text with the press of a key. This can be useful for demonstrations, testing, or any scenario where you need to automate text entry.

## Key Features

- **Automated Typing**: Reads content from a specified text file and types it out character by character.
- **Customizable Speed**: Set the typing speed (delay between characters).
- **Keyboard Controls**:
  - Press `Ctrl` to start auto-typing.
  - Press `Esc` to exit the program at any time.
- **Cross-app Typing**: Works with any application where keyboard input is accepted.

## How It Works

The core of the tool is the `AutoTyper` class, which:
- Reads content from a specified file.
- Listens for keyboard input to trigger actions (`Ctrl` to start, `Esc` to stop/exit).
- Types the file's content into the active window after a short delay, allowing you to switch to your target application.

## Setup and Execution

### 1. Clone the Repository

```bash
git clone https://github.com/mihaiapostol14/auto_typing_text.git
cd auto_typing_text
```

### 2. Create and Activate a Virtual Environment

**Install Python**

If you don't have Python installed, follow [this link](https://www.python.org/downloads/) and download the latest version of Python. Then you can check your version of Python using the command lines below:

```bash
# Create a virtual environment
python -m venv venv  

# Activate the virtual environment
source venv/bin/activate  # Linux/MacOS  
venv\Scripts\activate     # Windows  
```

### 3. Install the Required Libraries

```bash
pip install -r requirements.txt
```

## Usage

1. **Prepare your text file**:
   - Place the text you want to auto-type into a file (e.g., `example.txt`) in the same directory as the script.

2. **Run the script**:
    ```bash
    python main.py
    ```

3. **Control the typing**:
    - When prompted, press `Ctrl` to start typing. You have 5 seconds to switch focus to your desired application.
    - Press `Esc` at any time to exit.

### Example

```python
# Inside main.py
def main():
    AutoTyper(file_path="example.txt", typing_speed=0.05)

if __name__ == "__main__":
    main()
```

You can adjust the `file_path` and `typing_speed` parameters as needed.

## Technologies Used

- **Python**
- **pynput**: For listening to keyboard events and simulating typing.

## Project Structure

- `main.py`: Main script containing the `AutoTyper` class and program entry point.
- `requirements.txt`: Python dependencies for the project.
- `example.txt`: Example text file to be auto-typed (user-provided).

## Notes & Limitations

- The tool simulates keyboard input; make sure to use it responsibly.
- Requires permission to control the keyboard, which may require additional settings on some operating systems.
- Works on Windows, macOS, and Linux with Python 3.x.

## Author

- [mihaiapostol14](https://github.com/mihaiapostol14)

## License

*No license specified yet. Please add a license file to clarify usage rights.*
