import tkinter as tk
from PIL import ImageTk, Image

# from reactions.reactions import Reaction
from substance.substance import Substance
from reactions.reactions import Reaction



class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.val = tk.StringVar()
        #self.val.set("H2O")

        frame_1 = tk.LabelFrame(parent, text="hello there")
        frame_1.grid(row=1, column=1, pady=15, padx=15)

        self.label1 = tk.Label(frame_1, text="general kenobi")
        self.label1.grid(row=1, column=1, ipady=10)

        button_close = tk.Button(frame_1, text="Close")
        button_close["command"] = self.close
        button_close.grid(row=7, column=4, columnspan=5)

        entry = tk.Entry(frame_1, textvariable=self.val)
        entry.grid(row=2, column=1)
        parent.bind("<Return>", self.calc)

    def close(self, _event=None):
        self.parent.quit()

    def calc(self, _event=None):
        text = self.val.get()
        subs = Reaction(text)
        
        self.label1["text"] = subs.pretty_formula




"""if __name__ == "__main__":
    thing = Reaction(entry)
    print(thing)"""