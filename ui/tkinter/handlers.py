import tkinter as tk





def fontSettings(fontsize=12):
    default_font = tkFont.nametofont("TkDefaultFont")
    text_font = tkFont.nametofont("TkTextFont")
    fixed_font = tkFont.nametofont("TkFixedFont")

    default_font.configure(size=fontsize)
    text_font.configure(size=fontsize)
    fixed_font.configure(size=fontsize)


data = tk.StringVar

