import tkinter as tk
import tkinter.font as tkFont


def fontSettings(fontsize=12):
    default_font = tkFont.nametofont("TkDefaultFont")
    #text_font = tkFont.nametofont("TkTextFont")
    fixed_font = tkFont.nametofont("TkFixedFont")
    text_font = tkFont.Font(family="Helvetica", size=36, weight="bold")
    heading_font = tkFont.nametofont("TkHeadingFont")

    default_font.configure(size=fontsize)
    text_font.configure(size=fontsize)
    fixed_font.configure(size=fontsize)
    heading_font.configure(size=20)
