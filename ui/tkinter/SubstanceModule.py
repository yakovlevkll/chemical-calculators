import tkinter as tk
from .Var import Variable
from .Functions import Functions


class SubstanceModule:

    def __init__(self, parent, *args, **kwargs):
        self.frame = tk.LabelFrame(parent, text="Substance Module")
        self.parent = parent
        self.substance_txt = tk.StringVar()
        var = Variable(parent)
        func = Functions(parent)

        frame = tk.LabelFrame(parent, text="Enter Substance")
        frame.grid(row=var.subs_row, column=var.subs_col,
                   columnspan=2, pady=var.padd_y, padx=var.padd_x)

        self.label = tk.Label(frame, text="")
        self.label.grid(row=1, column=var.widgets_col, ipady=10)

        entry = tk.Entry(
            frame, textvariable=self.substance_txt, font=("Helvetica", "12"))
        entry.grid(row=var.entry_row, column=var.entry_col, ipady=3)
        #parent.bind("<Control-Key-q>", self.submit_func_pretty)

        button_submit = tk.Button(
            frame, text="Submit", command=func.submit_func_pretty())
        button_submit.grid(
            row=self.submit_row, column=self.widgets_col, ipady=1, **padding)
