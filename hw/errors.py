import sys
import tkinter as tk
from tkinter import messagebox

from PIL import Image, ImageTk

DEBUG = '-d' in sys.argv

def show_error_dialog():
    if DEBUG:
        breakpoint()
        print(f"Debugging {__file__}")
    root = tk.Tk()
    root.title("Danger, Will Robinson! :O")
    root.geometry("400x150")
    root.resizable(False, False)
    
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack()
    
    stop_icon = tk.Label(frame, text="", font=("Arial", 24))
    stop_icon.pack()
    
    message_label = tk.Label(frame, text="System SQL Error: Database Unrecoverable!", font=("Arial", 12), wraplength=350)
    message_label.pack(pady=10)
    
    button_frame = tk.Frame(frame)
    button_frame.pack()
    
    tk.Button(button_frame, text="OK", command=root.destroy).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Cancel", command=root.destroy).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Debug", command=root.destroy, fg="red").pack(side=tk.LEFT, padx=5)
    
    root.mainloop()

if __name__ == "__main__":
    if DEBUG:
        from PIL import Image, ImageTk
        
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
            image = Image.open("../img/stop.png")  # Replace with the path to your image
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
    else:
        breakpoint()
        show_error_dialog()
