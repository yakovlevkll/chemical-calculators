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
