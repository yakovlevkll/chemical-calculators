import tkinter as tk


class OuterLayer:
    def __init__(self, parent, *args, **kwargs):
        self.label0 = tk.Label(
            text="Chemical calculators", font=("Helvetica", "20"))
        self.label0.grid(row=1, column=1, sticky=tk.N)
