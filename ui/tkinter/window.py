import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image
from .Var import entry_row, entry_col, submit_row, submit_col, padding
from.handlers import fontSettings

from substance.substance import Substance
from reactions.reactions import Reaction



class MainApplication(tk.Frame):
    #fontSettings()
    

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.val = tk.StringVar()
        #self.val.set("H2O")

        frame_1 = tk.LabelFrame(parent, text="Enter Substance")
        frame_1.grid(row=1, column=1, pady=15, padx=15)

        self.label1 = tk.Label(frame_1, text="")
        self.label1.grid(row=1, column=1, ipady=10)

        button_close = tk.Button(text="Close")
        button_close["command"] = self.close
        button_close.grid(row=1, column=4)

        entry1 = tk.Entry(frame_1, textvariable=self.val)
        entry1.grid(row=entry_row, column=entry_col, ipady=3)
        parent.bind("<Return>", self.pretty)

        button_submit = tk.Button(frame_1, text="Submit", command=self.pretty)
        button_submit.grid(row=submit_row, column=submit_col, ipady=1, **padding)

        frame_2 = tk.LabelFrame(parent, text = "Enter Reaction")
        frame_2.grid(row=2,column=1,ipady=10)
        
        self.label2 = tk.Label(frame_2, text="")
        self.label2.grid(row=1, column=1, ipady=10)

        entry2 = tk.Entry(frame_2, textvariable=self.val)
        entry2.grid(row=entry_row, column=entry_col, ipady=3)
        parent.bind("<Return>", self.calc)

        button_submit = tk.Button(frame_2, text="Submit", command=self.calc)
        button_submit.grid(row=submit_row, column=submit_col, ipady=1, **padding)



    def close(self, _event=None):
        self.parent.quit()

    def pretty(self, _event=None):
        text = self.val.get()
        subs = Substance(text)
        
        self.label1["text"] = subs.pretty_formula

    def calc(self,_event=None):
        text = self.val.get()
        react = Reaction(text)

        self.label2["text"] = react




"""if __name__ == "__main__":
    thing = Reaction(entry)
    print(thing)"""