import tkinter as tk
from .Var import var
from reactions.reactions import Reaction
from helpers.string import clean_str


class ReactionModule(tk.Frame):

    def __init__(self, parent):
        self.frame = tk.LabelFrame(parent, text="React Module")
        self.parent = parent
        self.reaction_txt = tk.StringVar()
        self.error_txt = tk.StringVar
        # for testing/ remove later
        # self.fixture()

        frame = tk.LabelFrame(parent, text="Enter Reaction")
        frame.grid(var.main_react_module)

        self.label = tk.Label(frame, text="")
        self.label.grid(row=1, column=var.widgets_col, ipady=10)

        entry = tk.Entry(
            frame, textvariable=self.reaction_txt, font=("Helvetica", "12"))
        entry.grid(row=var.entry_row, column=var.widgets_col, ipady=3)
        parent.bind("<Control-Key-r>", self.submit_func_calc)

        button_submit = tk.Button(
            frame, text="Submit", command=self.submit_func_calc)
        button_submit.grid(
            row=var.submit_row, column=var.widgets_col, ipady=1)

        self.instruct_label = tk.Label(frame, text="(Ctrl + r)")
        self.instruct_label.grid(
            row=var.shortcut_label_row, column=var.widgets_col, ipady=3)

        self.label_error = tk.Label(frame, textvariable=self.error_txt)
        self.label_error.grid(row=var.label_error_row,
                              column=var.widgets_col, ipady=3)

    def pretty(self, _event=None):
        text = self.substance_txt.get()
        try:
            subs = Substance(text)
            self.label["text"] = f'{subs.pretty_formula}\n{subs.mass}u\n{subs.composition}'
        except ValueError as e:
            self.error_call(e)

    def fixture(self):
        self.reaction_txt.set('H2 + O2 -> H2O')

    def clear_entry_react(self, _event=None):
        self.reaction_txt.set('')

    def submit_func_calc(self, _event=None):
        self.clear_error_msg()
        text = self.reaction_txt.get()
        self.reaction_txt.set(Reaction(text))

        self.label["text"] = react

        self.clear_entry_react()

    def select_entry(self, _event=None):
        entry.focus

    def error_call(self, msg, event=None):
        # change label_error colour
        self.error_txt.set(msg)

    def clear_error_msg(self, event=None):
        self.error_txt.set('')
