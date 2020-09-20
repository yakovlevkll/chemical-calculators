import tkinter as tk
from .Var import Styles


class SubstanceModule:

    def __init__(self, parent, *args, **kwargs):
        self.frame = tk.LabelFrame(parent, text="Substance Module")
        self.parent = parent
        # self.parent.grid(padx=100)
        self.substance_txt = tk.StringVar()
        self.reaction_txt = tk.StringVar()
        # self.val.set("H2O")

        frame = tk.LabelFrame(parent, text="Enter Substance")
        frame.grid(row=subs_row, column=subs_col,
                   columnspan=2, pady=padd_y, padx=padd_x)

        self.label = tk.Label(frame, text="")
        self.label.grid(row=1, column=widgets_col, ipady=10)

        entry = tk.Entry(
            frame, textvariable=self.substance_txt, font=("Helvetica", "12"))
        entry.grid(row=entry_row, column=entry_col, ipady=3)
        parent.bind("<Control-Key-q>", self.submit_func_pretty)

        button_submit = tk.Button(
            frame, text="Submit", command=self.submit_func_pretty)
        button_submit.grid(
            row=submit_row, column=widgets_col, ipady=1, **padding)
