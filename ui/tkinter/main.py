import tkinter as tk

import tkinter.font as tkFont
from .window import MainApplication
from .handlers import fontSettings


def start_gui():
    root = tk.Tk()
    fontSettings()
    MainApplication(root)
    root.mainloop()
