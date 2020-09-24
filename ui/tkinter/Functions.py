import tkinter as tk


class Functions:
    def __init__(self, parent, *args, **kwargs):
        def close(self, _event=None):
            self.parent.quit()

        def pretty(self, _event=None):
            text = self.substance_txt.get()
            subs = Substance(text)

            self.label1["text"] = f'{subs.pretty_formula}\n{subs.mass}u\n{subs.composition}'

        def fixture(self):
            self.substance_txt.set('CO2')
            self.reaction_txt.set('H2 + O2 -> H2O')

        def select_entry1(self, _event=None):
            entry1.focus

        def select_entry2(self, _event=None):
            entry2.focus

        def clear_entry_subs(self, _event=None):
            self.substance_txt.set('')

        def clear_entry_react(self, _event=None):
            self.reaction_txt.set('')

        def submit_func_pretty(self, _event=None):
            self.pretty()
            self.clear_entry_subs()
            print(1)

        def submit_func_calc(self, _event=None):
            text = self.reaction_txt.get()
            react = Reaction(text)

            self.label2["text"] = react

            self.clear_entry_react
