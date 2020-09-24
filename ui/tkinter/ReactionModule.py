import tkinter as tk
from .Var import Variable
from .Functions import Functions


class ReactionModule(tk.Frame):

    def __init__(self, parent):
        self.frame = tk.LabelFrame(parent, text="React Module")
        self.parent = parent
        self.reaction_txt = tk.StringVar()
        var = Variable(parent)
        func = Functions(parent)

        frame = tk.LabelFrame(parent, text="Enter Reaction")
        frame.grid(row=2, column=3, columnspan=2, ipady=10)

        self.label = tk.Label(frame, text="")
        self.label.grid(row=1, column=var.widgets_col, ipady=10)

        entry = tk.Entry(
            frame, textvariable=self.reaction_txt, font=("Helvetica", "12"))
        entry.grid(row=var.entry_row, column=var.widgets_col, ipady=3)
        #entry.bind("<w>", self.submit_func_calc)

        button_submit = tk.Button(
            frame, text="Submit", command=func.submit_func_calc)
        button_submit.grid(
            row=var.submit_row, column=var.submit_col, ipady=1, **padding)

    def test_func(self):
        print(1)
