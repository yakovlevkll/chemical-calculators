'''
Chemical substance class.

Features:

- Determines substance composition
- Calculates molar (atomic) mass of a substance
- Beautifies chemical formula for text output
'''

from string import ascii_letters
import re

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

    def find_in_brackets(self, formula):
        bracket = ''
        temp = formula.split('(')
        temp2 = temp[2].split(')')

        bracket += temp2[1]

    def brackets_rule(self, bracket_block):  # working with brackets
        factor = ''
        for char in bracket_block[::-1]:
            if char.isnumeric():
                factor += char
            else:
                break

        for element in find_in_bracket(bracket_block):
            pass

        # Substance()

    def __mul__(self, num):
        # TODO: Check
        self.composition = {key: val * num for key,
                            val in self.composition.items()}

    def __add__(self, sub):
        # TODO: Check
        # comp = sub.composition
        # new = {}

        # self.composition = {key: val + sub[key] for key,
        #                     val in self.composition.items()}
        print('We are here')

    def find_composition(self):
        '''
        Determines atomic composition of a substance
        '''

        formula = self.formula
        composition = {}

        brackets_pattern = r'\((.+)\)(\d*)'
        brackets_block = re.search(brackets_pattern, formula)

        if brackets_block:
            inner, index = brackets_block.groups()
            pass
            # sub = Substance()
            # Multiply by brackets index
            # Replace block from original formula

        # Split formula in atom-index pairs
        atom_pattern = r'([A-Z]{1}[a-z]{0,1})(\d*)'
        pairs = re.findall(atom_pattern, formula)

        for pair in pairs:
            name, index = pair

            if index == '':
                index = 1
            else:
                index = int(index)

            if not name in composition:
                composition.setdefault(name, index)
            else:
                composition[name] += index

        if brackets_block:
            pass
            # Add brackets to composition

        self.composition = composition

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


sub_1 = Substance('OH')
sub_2 = Substance('Ba')

sub_1 * 2
sub_1 + sub_2

print(sub_1.composition)
