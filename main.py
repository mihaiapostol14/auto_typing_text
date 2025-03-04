import pyautogui
import keyboard
import time

class AutoTyper:
    """
    A class to handle auto-typing text from a file.
    """
    def __init__(self, file_path, typing_speed=0.1):
        """
        Initialize the AutoTyper with a file path and typing speed.

        :param file_path: Path to the text file.
        :param typing_speed: Delay between typing each character (in seconds).
        """
        self.file_path = file_path
        self.typing_speed = typing_speed

        self.check_keypress()

    def check_keypress(self):
        """
        Wait for the user to press 'ctrl' to start the program or 'esc' to stop it.
        """
        print("Press 'ctrl' to start auto-typing or 'esc' to exit.")
        while True:
            if keyboard.is_pressed('esc'):
                print("Exiting program.")
                return exit()
            elif keyboard.is_pressed('ctrl'):
                print("Starting auto-typing.")
                return self.start_typing()

    def read_file(self):
        """
        Reads the content of the file.
        :return: The text content of the file.
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' was not found.")
            return None
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return None

    def start_typing(self):
        """
        Starts typing the text from the file.
        """
        text = self.read_file()
        if text is None:
            return

        print("Auto-typing will start in 5 seconds. Switch to the desired application.")

        time.sleep(5)  # Delay to allow the user to switch to the target application

        for char in text:
            if keyboard.is_pressed('esc'):
                print("Auto-typing stopped by user.")
                return
            pyautogui.typewrite(char)
            time.sleep(self.typing_speed)

        print("Auto-typing completed.")

def main():
    # Replace 'example.txt' with the path to your text file
    AutoTyper(file_path="example.txt", typing_speed=0.05)

if __name__ == "__main__":
    main()