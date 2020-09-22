import tkinter as tk
from .Var import Variable
from .Functions import Functions


class SubstanceModule:

    def __init__(self, parent, *args, **kwargs):
        self.frame = tk.LabelFrame(parent, text="Substance Module")
        self.parent = parent
        self.substance_txt = tk.StringVar()

        frame = tk.LabelFrame(parent, text="Enter Substance")
        frame.grid(row=self.subs_row, column=self.subs_col,
                   columnspan=2, pady=self.padd_y, padx=self.padd_x)

        self.label = tk.Label(frame, text="")
        self.label.grid(row=1, column=self.widgets_col, ipady=10)

        entry = tk.Entry(
            frame, textvariable=self.substance_txt, font=("Helvetica", "12"))
        entry.grid(row=self.entry_row, column=self.entry_col, ipady=3)
        #parent.bind("<Control-Key-q>", self.submit_func_pretty)

        button_submit = tk.Button(
            frame, text="Submit", command=self.submit_func_pretty)
        button_submit.grid(
            row=self.submit_row, column=self.widgets_col, ipady=1, **padding)
