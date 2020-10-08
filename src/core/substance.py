'''
Chemical substance class.

Features:

- Determines substance composition
- Calculates molar (atomic) mass of a substance
- Beautifies chemical formula for text output
'''

from string import ascii_letters

from .table import TABLE
from helpers.string import subscript_it, clean_str


class Substance:

    '''
    Main class for substance.

    formula - something like `H20`
    pretty_formula - beautified version of the formula
    composition - self-descriptive, something like {'H': 2, 'O': 1}
    mass - molar (atomic) mass
    '''

    formula = ''
    pretty_formula = ''
    composition = {}
    mass = 0

    def __init__(self, formula):
        self.formula = formula
        self.validate_formula()
        self.prettify_formula()
        self.find_composition()
        self.find_mass()

    def validate_formula(self):
        self.formula = clean_str(self.formula, ascii_letters + "1234567890()")

    def prettify_formula(self):
        '''
        Turns `H2O` into `H₂O`
        '''

        chars = list(self.formula)

        self.pretty_formula = ''.join([subscript_it(char) for char in chars])

    def find_composition(self):
        '''
        Determines atomic composition of a substance
        '''

        self.composition = {}

        pairs = []

        # Split formula in atom-index pairs
        for char in self.formula:
            if char.isupper():
                pairs.append([char, ''])
            elif char.islower():
                pairs[-1][0] += char
            else:
                pairs[-1][1] += char

        for pair in pairs:
            name, index = pair

            # Kind of validation
            name = TABLE[name].symbol

            if index == '':
                index = 1
            else:
                index = int(index)

            if not name in self.composition:
                self.composition.setdefault(name, index)
            else:
                self.composition[name] += index

    def find_mass(self):
        '''
        Finds molar (atomic) mass of a substance
        '''

        self.mass = 0

        for name, amount in self.composition.items():
            self.mass += TABLE[name].mass * amount

        self.mass = round(self.mass, 3)

    def __repr__(self):
        return f'''
        Formula: {self.pretty_formula}
        Composition: {self.composition}
        Mass: {self.mass} g/mol
        '''
