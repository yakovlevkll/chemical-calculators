import tkinter as tk


class Variable:
    def __init__(self, parent, *args, **kwargs):

        self.subs_row = 1
        self.subs_col = 2
        self.react_row = 2
        self.react_col = 2
        self.widgets_col = 1
        self.label_row = 1
        self.entry_row = self.label_row + 1,
        self.submit_row = self.label_row + 2

        self.padd_x = 100
        self.padd_y = 100

        # For frames
        self.subs_frame_row = 1
        self.react_frame_row = self.subs_frame_row + 1
        self.frame col = 2


data = tk.StringVar


# either dict or class
