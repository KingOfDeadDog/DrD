import tkinter as tk


class Gui:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("DrD")

    def show(self):
        self.window.mainloop()
