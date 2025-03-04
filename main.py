from pynput import keyboard
from pynput.keyboard import Controller, Key
import time
import threading

class AutoTyper:
    """
    A class to handle auto-typing text from a file using pynput.
    """
    def __init__(self, file_path, typing_speed=0.1):
        """
        Initialize the AutoTyper with a file path and typing speed.

        :param file_path: Path to the text file.
        :param typing_speed: Delay between typing each character (in seconds).
        """
        self.file_path = file_path
        self.typing_speed = typing_speed
        self.keyboard_controller = Controller()
        self.running = False
        self.listener = None

        self.start_listener()

    def start_listener(self):
        """
        Start listening for keyboard input (Ctrl to start, Esc to stop).
        """
        print("Press 'Ctrl' to start auto-typing or 'Esc' to exit.")

        def on_press(key):
            try:
                if key == Key.esc:
                    print("Exiting program.")
                    self.stop_listener()
                    exit()
                elif key == Key.ctrl_l or key == Key.ctrl_r:
                    if not self.running:
                        print("Starting auto-typing.")
                        self.running = True
                        threading.Thread(target=self.start_typing).start()
            except Exception as e:
                print(f"Error: {e}")

        self.listener = keyboard.Listener(on_press=on_press)
        self.listener.start()
        self.listener.join()

    def stop_listener(self):
        """Stops the keyboard listener."""
        if self.listener is not None:
            self.listener.stop()

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
        time.sleep(5)

        for char in text:
            if not self.running:
                print("Auto-typing stopped by user.")
                return
            self.keyboard_controller.type(char)
            time.sleep(self.typing_speed)

        print("Auto-typing completed.")
        self.running = False

def main():
    AutoTyper(file_path="example.txt", typing_speed=0.05)

if __name__ == "__main__":
    main()
