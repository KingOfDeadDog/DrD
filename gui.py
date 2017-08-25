import tkinter as tk
from tkinter import ttk


class Gui:
    def button_ok_click(self):
        """Handles click on the ok buttons"""
        self.label_welcome.configure(text="Thanks for playing")

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("DrD")
        self.window.resizeable(False, False)
        # basic initialization is done, lets add widgets
        self.label_welcome = ttk.Label(self.window,
                                       text="Welcome to the DrD game")
        self.label_welcome.grid(column=0, row=0)
        self.ok_button = ttk.Button(self.window, text="OK",
                                    command=button_ok_click(self))
        self.ok_button.grid(column=0, row=1)


    def show(self):
        self.window.mainloop()
