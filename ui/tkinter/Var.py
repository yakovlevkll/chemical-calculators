import tkinter as tk


class Variable:
    def __init__(self, parent, *args, **kwargs):

        self.subs_row = 1
        self.subs_col = 2
        self.react_row = 2
        self.react_col = 2
        self.widgets_col = 1
        self.label_row = 1
        self.entry_row = label_row + 1,
        self.submit_row = label_row + 2

        self.padd_x = 100,
        self.padd_y = 100


data = tk.StringVar


# either dict or class
