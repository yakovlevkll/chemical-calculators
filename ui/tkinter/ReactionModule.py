import tkinter as tk
from .Var import Variable
from reactions.reactions import Reaction


class ReactionModule(tk.Frame):

    def __init__(self, parent):
        self.frame = tk.LabelFrame(parent, text="React Module")
        self.parent = parent
        self.reaction_txt = tk.StringVar()
        # for testing/ remove later
        self.fixture()
        var = Variable(parent)

        frame = tk.LabelFrame(parent, text="Enter Reaction")
        frame.grid(row=2, column=3, columnspan=2, ipady=10)

        self.label = tk.Label(frame, text="")
        self.label.grid(row=1, column=var.widgets_col, ipady=10)

        entry = tk.Entry(
            frame, textvariable=self.reaction_txt, font=("Helvetica", "12"))
        entry.grid(row=var.entry_row, column=var.widgets_col, ipady=3)
        #entry.bind("<w>", self.submit_func_calc)

        button_submit = tk.Button(
            frame, text="Submit", command=self.submit_func_calc)
        button_submit.grid(
            row=var.submit_row, column=var.widgets_col, ipady=1)

    def pretty(self, _event=None):
        text = self.substance_txt.get()
        subs = Substance(text)

        self.label["text"] = f'{subs.pretty_formula}\n{subs.mass}u\n{subs.composition}'

    def fixture(self):
        self.reaction_txt.set('H2 + O2 -> H2O')

    def clear_entry_react(self, _event=None):
        self.reaction_txt.set('')

    def submit_func_calc(self, _event=None):
        text = self.reaction_txt.get()
        react = Reaction(text)

        self.label["text"] = react

        self.clear_entry_react()

    def select_entry(self, _event=None):
        entry.focus

    '''def test_func(self):
        print(1)'''
