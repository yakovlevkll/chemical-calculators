import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image
from .Var import entry_row, entry_col, submit_row, submit_col, padding


from substance.substance import Substance
from reactions.reactions import Reaction


class MainApplication(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        # self.parent.grid(padx=100)
        self.substance_txt = tk.StringVar()
        self.reaction_txt = tk.StringVar()
        # self.val.set("H2O")

        frame_1 = tk.LabelFrame(parent, text="Enter Substance")
        frame_1.grid(row=1, column=1, columnspan=2, pady=15)

        self.label1 = tk.Label(frame_1, text="")
        self.label1.grid(row=1, column=1, ipady=10)

        button_close = tk.Button(text="Close")
        button_close["command"] = self.close
        button_close.grid(row=3, column=1, sticky=tk.E)

        entry1 = tk.Entry(frame_1, textvariable=self.substance_txt)
        entry1.grid(row=entry_row, column=entry_col, ipady=3)
        entry1.bind("<Return>", self.pretty)

        button_submit = tk.Button(frame_1, text="Submit", command=self.pretty)
        button_submit.grid(
            row=submit_row, column=submit_col, ipady=1, **padding)

        frame_2 = tk.LabelFrame(parent, text="Enter Reaction")
        frame_2.grid(row=2, column=1, columnspan=2, ipady=10)

        self.label2 = tk.Label(frame_2, text="")
        self.label2.grid(row=1, column=1, ipady=10)

        entry2 = tk.Entry(frame_2, textvariable=self.reaction_txt)
        entry2.grid(row=entry_row, column=entry_col, ipady=3)
        entry2.bind("<Return>", self.calc)

        button_submit = tk.Button(frame_2, text="Submit", command=self.calc)
        button_submit.grid(
            row=submit_row, column=submit_col, ipady=1, **padding)

        self.fixture()

    def close(self, _event=None):
        self.parent.quit()

    def pretty(self, _event=None):
        text = self.substance_txt.get()
        subs = Substance(text)

        self.label1["text"] = f'{subs.pretty_formula}\n{subs.mass}u\n{subs.composition}'

    def calc(self, _event=None):
        text = self.reaction_txt.get()
        react = Reaction(text)

        self.label2["text"] = react

    def fixture(self):
        self.substance_txt.set('CO2')
        self.reaction_txt.set('H2 + O2 -> H2O')
