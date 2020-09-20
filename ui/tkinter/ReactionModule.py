import tkinter as tk


class ReactionModule(tk.Frame):

    def __init__(self, parent):
        self.frame = tk.LabelFrame(parent, text="React Module")

        button_close = tk.Button(self.frame, text="Hello")
        button_close["command"] = self.test_func
        button_close.grid(row=1, column=6)

    def test_func(self):
        print(1)
