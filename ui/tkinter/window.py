import tkinter as tk
import tkinter.font as tkFont
from .Var import Variable
from .ReactionModule import ReactionModule
from .SubstanceModule import SubstanceModule
from .Functions import Functions
from .Outside_layer import OuterLayer


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

        reaction_module = ReactionModule(parent)
        reaction_module.frame.grid(
            row=2, column=1, columnspan=2, pady=100, padx=100)

        substance_module = SubstanceModule(parent)
        substance_module.frame.grid(row=1, column=1, ipady=10)

        outer_layer = OuterLayer(parent)

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
