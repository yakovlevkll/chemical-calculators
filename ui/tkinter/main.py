import tkinter as tk

import tkinter.font as tkFont
from .window import MainApplication


def start_gui():
    root = tk.Tk()
    MainApplication(root)
    root.mainloop()
