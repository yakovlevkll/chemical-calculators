import tkinter as tk
import tkinter.font as tkFont
from .Var import Variable
from .ReactionModule import ReactionModule
from .SubstanceModule import SubstanceModule


from substance.substance import Substance
from reactions.reactions import Reaction


class MainApplication(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        substance_module = SubstanceModule(parent)
        substance_module.frame.grid(
            row=var.subs_frame_row, column=var.frame_col, ipady=10)

        reaction_module = ReactionModule(parent)
        reaction_module.frame.grid(
            row=var.react_frame_row, column=var.frame_col, columnspan=2, pady=100, padx=100)

        var = Variable(parent)

        self.label = tk.Label(
            text="Chemical calculators", font=("Helvetica", "20"))
        self.label.grid(row=1, column=1, sticky=tk.N)

        self.close_button = tk.Button(parent, text="close", command=self.close)
        self.close_button.grid(row=1, column=6, sticky=tk.N)

    def close(self, _event=None):
        self.parent.quit()
