import tkinter as tk
from .Var import Variable
from substance.substance import Substance


class SubstanceModule:

    def __init__(self, parent, *args, **kwargs):
        self.frame = tk.LabelFrame(parent, text="Substance Module")
        self.parent = parent
        self.substance_txt = tk.StringVar()

        # for testing/ remove later
        self.fixture()
        var = Variable(parent)

        frame = tk.LabelFrame(parent, text="Enter Substance")
        frame.grid(row=var.subs_row, column=var.subs_col,
                   columnspan=2, pady=var.padd_y, padx=var.padd_x)

        self.label = tk.Label(frame, text="")
        self.label.grid(row=1, column=var.widgets_col, ipady=10)

        entry = tk.Entry(
            frame, textvariable=self.substance_txt, font=("Helvetica", "12"))
        entry.grid(row=var.entry_row, column=var.widgets_col, ipady=3)
        #parent.bind("<Control-Key-q>", self.submit_func_pretty)

        button_submit = tk.Button(
            frame, text="Submit", command=self.submit_func_pretty)
        button_submit.grid(
            row=var.submit_row, column=var.widgets_col, ipady=1)

    def pretty(self, _event=None):
        text = self.substance_txt.get()
        subs = Substance(text)

        self.label["text"] = f'{subs.pretty_formula}\n{subs.mass}u\n{subs.composition}'

    def clear_entry_subs(self, _event=None):
        self.substance_txt.set('')

    def submit_func_pretty(self, _event=None):
        self.pretty()
        self.clear_entry_subs()
        print(1)  # remove

    def fixture(self):
        self.substance_txt.set('CO2')

    '''def select_entry(self, _event=None):
        entry.focus'''
