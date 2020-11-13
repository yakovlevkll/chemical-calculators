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
    expanded_formula = ''
    composition = {}
    mass = 0

    def __init__(self, formula):
        self.formula = formula
        self.validate_formula()
        self.prettify_formula()
        self.find_composition()
        self.find_mass()

    def __mul__(self, num):
        # TODO: Is it expected behaviour?
        sub = Substance(self.formula)
        sub.composition = {key: val * num for key,
                           val in self.composition.items()}
        return sub

    def __add__(self, sub):
        # TODO: Should it be a Reaction?
        pass

    def validate_formula(self):
        self.formula = clean_str(self.formula, ascii_letters + "1234567890()")

    def prettify_formula(self):
        '''
        Turns `H2O` into `H₂O`
        '''

        chars = list(self.formula)

        self.pretty_formula = ''.join([subscript_it(char) for char in chars])

    def expand_formula(self):
        '''
        Determines atomic composition of a substance
        '''

        stack = ['']

        bracket_index_mode = False
        bracket_index = ''

        for char in self.formula:
            if bracket_index_mode:
                if char.isnumeric():
                    bracket_index += char
                    continue
                else:
                    last = stack.pop()
                    pairs = Substance.get_atom_index_pairs(last)
                    num = int(bracket_index)
                    multiplied_sub = [(key, val * num) for key, val in pairs]
                    stack[-1] += ''.join([f'{key}{val}' for key, val in multiplied_sub])

                    bracket_index_mode = False
                    bracket_index = ''

            if char.isalnum():
                stack[-1] += char
            elif char == '(':
                stack.append('')
            elif char == ')':
                bracket_index_mode = True

        self.expanded_formula = stack[0]

    @staticmethod
    def get_atom_index_pairs(formula):
        '''
        Split formula in atom-index pairs
        '''

        pattern = r'([A-Z]{1}[a-z]{0,1})(\d*)'
        res = re.findall(pattern, formula)

        pairs = []

        for atom, index in res:
            if index == '':
                index = 1
            
            pairs.append((atom, int(index)))

        return pairs


    def find_composition(self):
        '''
        Determines atomic composition of a substance
        '''

        self.expand_formula()
        self.composition = {}

        pairs = Substance.get_atom_index_pairs(self.expanded_formula)

        for atom, index in pairs:
            if not atom in self.composition:
                self.composition.setdefault(atom, 0)

            self.composition[atom] += index

    def find_mass(self):
        '''
        Finds molar (atomic) mass of a substance
        '''

        self.mass = 0

        for atom, index in self.composition.items():
            self.mass += TABLE[atom].mass * index

        self.mass = round(self.mass, 3)

    def __repr__(self):
        return f'''
        Formula: {self.pretty_formula}
        Composition: {self.composition}
        Mass: {self.mass} g/mol
        '''
