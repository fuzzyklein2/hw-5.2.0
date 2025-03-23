import logging
from pathlib import Path
import sys
import tkinter as tk
from tkinter import messagebox
from warnings import warn

from PIL import Image, ImageTk

DEBUG = '-d' in sys.argv
TESTING = '-t' in sys.argv
try:
    from __init__ import ARGS, BASEDIR, log
except:
    BASEDIR = Path(__file__).parent.parent

if DEBUG:
    print(f'{BASEDIR=}')

class Error(Exception):
    """Custom exception with additional attributes for UI-related error handling."""
    
    def __init__(self, message, code=None, title="ERROR!", icon=str(BASEDIR / "img/stop.png"), buttons=None, **kwargs):
        super().__init__(message)
        self.code = code  # Optional error code
        self.title = title  # Title of the error message
        self.icon = icon  # Icon representing the error
        self.buttons = buttons  # Buttons available in the error dialog
        self.extra = kwargs  # Store any additional keyword arguments
        self.message = message
        self.buttons_loaded = False
        self.choice = None
        self.log = logging.getLogger("Error")
        self.log.info("Error object initialized.")

    def __str__(self):
        details = f"[Error {self.code}] " if self.code else ""
        details += super().__str__()
        if self.title:
            details = f"{self.title}: {details}"
        return details

    def on_button_click(self, choice):
        print(f'Button clicked: {choice}')
        self.choice = choice
        self.root.destroy()

    def get_clicked_button(self):
        print(f'Button clicked: {self.choice}') 
        self.root.destroy()

    def show(self):
        if DEBUG:
            breakpoint()
            print(f"Debugging {__file__}")
        self.root = tk.Tk()
        self.root.title(self.title)
        self.root.geometry("400x175")
        self.root.resizable(False, False)
        
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack()

        if DEBUG:
            breakpoint()

        try:
            image = Image.open(self.icon)  # Replace with the path to your image
            image = image.resize((50, 50), Image.LANCZOS)
            img = ImageTk.PhotoImage(image)
            img_label = tk.Label(frame, image=img)
            img_label.pack()
        except Exception as e:
            print(f"Error loading image: {self.icon}")
            warn(f"Error loading image: {self.icon}")

            # stop_icon = tk.Label(frame, text=self.icon, font=("Arial", 24))
            # stop_icon.pack()
        
        message_label = tk.Label(frame, text=f"Code {self.code} Error: {self.message}", font=("Arial", 12), wraplength=350)
        message_label.pack(pady=10)
        
        button_frame = tk.Frame(frame)
        button_frame.pack()
        
        for b in (self.buttons if self.buttons else []):
            tk.Button(button_frame, text=b, command=lambda b=b: self.on_button_click(b)).pack(side=tk.RIGHT, padx=5)
        self.buttons_loaded = True;
        self.root.mainloop()
        # self.root.destroy()

    def output(self):
        log.error(f'{self}')
        self.show()

class Caution(Error):
    def __init__(self, message, code=None, title="ERROR!", icon=str(BASEDIR / "img/stop.png"), buttons=None, **kwargs):
        super().__init__(message, code=None, title="Warning!", icon=str(BASEDIR / "img/warn.png"), buttons=None, **kwargs)

    def output(self):
        warn(self.message)
        self.show()

if __name__ == "__main__":
# Example usage
    try:
        # Load and display the image
        # image = None
        # try:
        #     image = Image.open(str(BASEDIR / "img/stop.png"))  # Replace with the path to your image
        #     image = image.resize((50, 50), Image.LANCZOS)
        #     img = ImageTk.PhotoImage(image)
        #     img_label = tk.Label(frame, image=img)
        #     img_label.pack()
        # except Exception as e:
        #     print(f"Error loading image: {e}")
        raise Error("File not found!", code=404, buttons=["OK", "Retry"])
    except Error as e:
        e.output()

    try:
        raise Caution("Danger, Will Robinson!", code=1965, buttons=["OK", "Cancel"])
    except Caution as c:
        c.output()
        
    
    if TESTING:
        def on_button_click(choice):
            print(f'Button clicked: {choice}')
            root.destroy()
        
        root = tk.Tk()
        root.title("Error")
        root.geometry("400x250")
        root.resizable(False, False)
        
        frame = tk.Frame(root)
        frame.pack(pady=10)
        
        # Load and display the image
        try:
            image = Image.open(str(BASEDIR / "img/stop.png"))  # Replace with the path to your image
            image = image.resize((50, 50), Image.LANCZOS)
            img = ImageTk.PhotoImage(image)
            img_label = tk.Label(frame, image=img)
            img_label.pack()
        except Exception as e:
            print(f"Error loading image: {e}")
        
        # Error message label
        label = tk.Label(frame, text="System SQL Error: Database Unrecoverable!", font=("Arial", 12), fg="red")
        label.pack(pady=10)
        
        # Buttons
        buttons_frame = tk.Frame(root)
        buttons_frame.pack(pady=10)
        
        tk.Button(buttons_frame, text="OK", command=lambda: on_button_click("OK")).pack(side=tk.LEFT, padx=5)
        tk.Button(buttons_frame, text="Cancel", command=lambda: on_button_click("Cancel")).pack(side=tk.LEFT, padx=5)
        tk.Button(buttons_frame, text="OH, FUCK!", fg="red", command=lambda: on_button_click("OH, FUCK!")).pack(side=tk.LEFT, padx=5)
        
        root.mainloop()
    # else:
    #     breakpoint()
    #     show_error_dialog()
