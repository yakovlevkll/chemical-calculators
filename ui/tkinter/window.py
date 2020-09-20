import tkinter as tk
import tkinter.font as tkFont
from .Var import Styles
from .ReactionModule import ReactionModule
from .SubstanceModule import SubstanceModule


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

        self.label0 = tk.Label(
            text="Chemical calculators", font=("Helvetica", "20"))
        self.label0.grid(row=1, column=1, sticky=tk.N)

        reaction_module = ReactionModule(parent)
        reaction_module.frame.grid(
            row=2, column=1, columnspan=2, pady=100, padx=100)

        substance_module = SubstanceModule(parent)
        substance_module.frame.grid(row=1, column=1, ipady=10)

        '''frame_1 = tk.LabelFrame(parent, text="Enter Substance")
        frame_1.grid(row=1, column=3, columnspan=2, pady=100, padx=100)

        ''''''

        button_test = tk.Button(text="padtest")
        button_test.grid(row=1, column=1)

        self.label1 = tk.Label(frame_1, text="")
        self.label1.grid(row=1, column=1, ipady=10)

        # button_close = tk.Button(text="Close")
        # button_close["command"] = self.close
        # button_close.grid(row=3, column=3, sticky=tk.E)

        entry1 = tk.Entry(
            frame_1, textvariable=self.substance_txt, font=("Helvetica", "12"))
        entry1.grid(row=entry_row, column=entry_col, ipady=3)
        parent.bind("<Control-Key-q>", self.submit_func_pretty)

        button_submit1 = tk.Button(
            frame_1, text="Submit", command=self.submit_func_pretty)
        button_submit1.grid(
            row=submit_row, column=submit_col, ipady=1, **padding)'''

        frame_2 = tk.LabelFrame(parent, text="Enter Reaction")
        frame_2.grid(row=2, column=3, columnspan=2, ipady=10)

        self.label2 = tk.Label(frame_2, text="")
        self.label2.grid(row=1, column=1, ipady=10)

        entry2 = tk.Entry(
            frame_2, textvariable=self.reaction_txt, font=("Helvetica", "12"))
        entry2.grid(row=entry_row, column=entry_col, ipady=3)
        entry2.bind("<w>", self.submit_func_calc)

        button_submit2 = tk.Button(
            frame_2, text="Submit", command=self.submit_func_calc)
        button_submit2.grid(
            row=submit_row, column=submit_col, ipady=1, **padding)

        self.fixture()  # for testing

    def close(self, _event=None):
        self.parent.quit()

    def pretty(self, _event=None):
        text = self.substance_txt.get()
        subs = Substance(text)

        self.label1["text"] = f'{subs.pretty_formula}\n{subs.mass}u\n{subs.composition}'

    def fixture(self):
        self.substance_txt.set('CO2')
        self.reaction_txt.set('H2 + O2 -> H2O')

    def select_entry1(self, _event=None):
        entry1.focus

    def select_entry2(self, _event=None):
        entry2.focus

    def clear_entry_subs(self, _event=None):
        self.substance_txt.set('')

    def clear_entry_react(self, _event=None):
        self.reaction_txt.set('')

    def submit_func_pretty(self, _event=None):
        self.pretty()
        self.clear_entry_subs()
        print(1)

    def submit_func_calc(self, _event=None):
        text = self.reaction_txt.get()
        react = Reaction(text)

        self.label2["text"] = react

        self.clear_entry_react
        print(2)
