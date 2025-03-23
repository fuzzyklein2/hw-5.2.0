from cmd import Cmd
import tkinter as tk
from tkinter import messagebox

from .filter import Filter
from .startup import PROGRAM

class Driver(Cmd, Filter):
    def run(self):
        self.process_files()
        super().cmdloop()

    def do_quit(self, args):
        
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        
        # Show the dialog
        response = messagebox.askyesnocancel("Question", f"Do you really want to quit {PROGRAM}?")
        
        # Destroy the root window after the dialog is closed
        root.destroy()
        
        # Handle responses
        return response

    def do_ask(self, args):
        pass
