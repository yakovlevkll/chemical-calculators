import tkinter as tk
from .Var import Variable
from .Functions import Functions


class OuterLayer:
    def __init__(self, parent, *args, **kwargs):
        var = Variable(parent)
        func = Functions(parent)

        self.label = tk.Label(
            text="Chemical calculators", font=("Helvetica", "20"))
        self.label.grid(row=1, column=1, sticky=tk.N)

        self.close_button = tk.Button(parent, text="close", command=func.close)
        self.close_button.grid(row=1, column=6, sticky=tk.N)
