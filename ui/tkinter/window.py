import tkinter as tk
import tkinter.font as tkFont
from .Var import var
from .ReactionModule import ReactionModule
from .SubstanceModule import SubstanceModule


from substance.substance import Substance
from reactions.reactions import Reaction


class MainApplication(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.label = tk.Label(
            text="Chemical calculators", font=("Helvetica", "20"))

        self.label.grid(**var.main_label)

        substance_module = SubstanceModule(parent)
        substance_module.frame.grid(**var.main_substance_module)

        reaction_module = ReactionModule(parent)
        reaction_module.frame.grid(**var.main_react_module)

        self.close_button = tk.Button(parent, text="close", command=self.close)
        self.close_button.grid(row=4, column=2, sticky=tk.N)

    def close(self, _event=None):
        self.parent.quit()
