'''
Chemical substance class.

Features:

- Determines substance composition
- Calculates molar (atomic) mass of a substance
- Beautifies chemical formula for text output
'''

from string import ascii_letters
from typing import Optional

from .composition import Composition
from .table import TABLE
from helpers.string import subscript_it, clean_ws


class Substance:
    '''
    Main class for substance.

    formula - something like `H2O`
    composition - self-descriptive, something like {'H': 2, 'O': 1}
    mass - molar (atomic) mass
    '''

    def __init__(self, formula: str):
        self.formula: str = clean_ws(formula)
        self.validate()

        self.composition: Optional[Composition] = None
        self.mass: float = 0

        self.find_composition()
        self.find_mass()

    def validate(self):
        allowed_chars = ascii_letters + "1234567890()[]"

        for char in self.formula:
            if not char in allowed_chars:
                raise ValueError(f'Unknown char is given: `{char}`')

    def find_composition(self):
        '''
        Determines atomic composition of a substance
        '''

        stack: list[str] = ['']

        bracket_index: Optional[str] = None

        for char in self.formula:
            if not bracket_index == None:
                if char.isnumeric():
                    bracket_index += char
                    continue
                else:
                    last = stack.pop()

                    stack[-1] += str(Composition(
                        last) * int(bracket_index))

                    bracket_index = None

            if char.isalnum():
                stack[-1] += char
            elif char in ['(', '[']:
                stack.append('')
            elif char in [')', ']']:
                bracket_index = ''

        # Checking end of a formula
        if bracket_index:
            last = stack.pop()
            stack[-1] += str(Composition(last) * int(bracket_index))

        self.composition = Composition(stack[0])

    def find_mass(self):
        '''
        Finds molar (atomic) mass of a substance
        '''

        self.mass = 0

        for atom, index in self.composition.items():
            self.mass += TABLE[atom].mass * index

        self.mass = round(self.mass, 3)

    def __str__(self):
        '''
        Returns beautified version of the formula with subscripts
        For example, `H2O` becomes `H₂O`
        '''

        return subscript_it(self.formula)

    def __repr__(self):
        return f'{str(self)} ({repr(self.composition)}, {self.mass} g/mol)'
