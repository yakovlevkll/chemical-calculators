'''
Chemical substance class.

Features:

- Determines substance composition
- Calculates molar (atomic) mass of a substance
- Beautifies chemical formula for text output
'''

import re
from string import ascii_letters
from typing import Union

from .table import TABLE
from helpers.string import subscript_it, clean_ws


class Substance:

    '''
    Main class for substance.

    formula - something like `H20`
    pretty_formula - beautified version of the formula
    composition - self-descriptive, something like {'H': 2, 'O': 1}
    mass - molar (atomic) mass
    '''

    def __init__(self, formula: str):
        self.formula: str = clean_ws(formula)
        self.validate()

        self.pretty_formula: str = ''
        self.expanded_formula: str = ''
        self.composition: dict[str, int] = {}
        self.mass: float = 0

        self.prettify_formula()
        self.find_composition()
        self.find_mass()

    def __mul__(self, factor: int):
        # TODO: Is it expected behaviour?
        if type(factor) is int:
            sub = Substance(self.formula)
            sub.composition = {key: val * factor for key,
                            val in self.composition.items()}
            return sub
        else:
            raise ValueError(f'The factor type must be `int`')

    def __add__(self):
        # TODO: Should it be a Reaction?
        pass

    def validate(self):
        allowed_chars = ascii_letters + "1234567890()[]"

        for char in self.formula:
            if not char in allowed_chars:
                raise ValueError(f'Unknown char is given: `{char}`')

    def prettify_formula(self):
        '''
        Turns `H2O` into `H₂O`
        '''

        self.pretty_formula = subscript_it(self.formula)

    def expand_formula(self):
        '''
        Determines atomic composition of a substance
        '''

        stack = ['']

        bracket_index = None

        for char in self.formula:
            if not bracket_index == None:
                if char.isnumeric():
                    bracket_index += char
                    continue
                else:
                    last = stack.pop()
                    stack[-1] += Substance.multiply_indexes(last, bracket_index)

                    bracket_index = None

            if char.isalnum():
                stack[-1] += char
            elif char in ['(', '[']:
                stack.append('')
            elif char in [')', ']']:
                bracket_index = ''

        if bracket_index:
            last = stack.pop()
            stack[-1] += Substance.multiply_indexes(last, bracket_index)

        self.expanded_formula = stack[0]

    @staticmethod
    def multiply_indexes(formula: str, factor: Union[str, int]) -> str:
        if not type(factor) is int:
            factor = int(factor)

        if factor == 0:
            factor = 1

        pairs = Substance.get_atom_index_pairs(formula)
        pairs_mult = [(key, val * factor) for key, val in pairs]
        return ''.join([f'{key}{val}' for key, val in pairs_mult])


    @staticmethod
    def get_atom_index_pairs(formula: str):
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
