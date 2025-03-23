import sys
import tkinter as tk
from tkinter import messagebox

DEBUG = '-d' in sys.argv

def show_error_dialog():
    root = tk.Tk()
    root.title("Social Security Database Viewer")
    root.geometry("400x200")
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
    tk.Button(button_frame, text="OH, FUCK!", command=root.destroy, fg="red").pack(side=tk.LEFT, padx=5)
    
    root.mainloop()

if __name__ == "__main__":
    if DEBUG:
        import tkinter as tk
        root = tk.Tk()
        root.mainloop()
    else: show_error_dialog()
