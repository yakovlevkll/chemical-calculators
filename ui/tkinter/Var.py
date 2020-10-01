import tkinter as tk
import tkinter.font as tkFont


class Variable:
    def __init__(self):

        #self.fonts =  {}

        self.subs_row = 1
        self.subs_col = 2
        self.react_row = 2
        self.react_col = 2
        self.widgets_col = 1
        self.label_row = 1
        self.entry_row = self.label_row + 1,
        self.submit_row = self.label_row + 2
        self.instruct_label_row = self.label_row + 3

        self.padx = 20
        self.pady = 20

        self.ipadx = 8
        self.ipady = 8

        # Main Window

        self.main_label = {
            'row': 1,
            'column': 1,
            'sticky': tk.N
        }

        self.main_substance_module = {
            'row': 2,
            'column': 1,
            'padx':  self.padx,
            'pady': self.pady,
            'ipadx':  self.ipadx,
            'ipady': self.ipady,
            'columnspan': 2
        }

        self.main_react_module = {
            'row': self.main_substance_module['row'] + 1,
            'column': self.main_substance_module['column'],
            'padx':  self.padx,
            'pady': self.pady,
            'ipadx':  self.ipadx,
            'ipady': self.ipady,
            'columnspan': 2
        }
       # self.fontSettings()

    '''@staticmethod
    def fontSettings(fontsize=12):
        #default_font = tkFont.nametofont("TkDefaultFont")
        #text_font = tkFont.nametofont("TkTextFont")
        #fixed_font = tkFont.nametofont("TkFixedFont")
        #text_font = tkFont.Font(family="Helvetica", size=36, weight="bold")
        heading_font = tkFont.nametofont("TkHeadingFont")

        # default_font.configure(size=fontsize)
        # text_font.configure(size=fontsize)
        # fixed_font.configure(size=fontsize)
        heading_font.configure(size=20)'''


var = Variable()
