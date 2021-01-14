from string import ascii_letters
from itertools import product

import re
import numpy as np
from numpy.lib.npyio import recfromtxt

from .substance import Substance
from helpers.string import clean_ws


class Reaction:
    '''
    Reaction class.

    TODO: add description
    '''

    def __init__(self, equation: str):
        self.equation: str = clean_ws(equation)
        self.validate()

        self.atoms: set[str] = set([])
        self.reactants: list[ReactionItem] = []
        self.products: list[ReactionItem] = []
        self.substances: list[ReactionItem] = []
        self.solution: list[int] = []

        self.parse()
        self.solve()

    def validate(self):
        # TODO: Improve validation

        reactant_pattern = '([A-z\d]+\+)*[A-z\d]+'
        product_pattern = reactant_pattern

        pattern = '^{0}(=|->){1}$'.format(reactant_pattern, product_pattern)
        print(pattern)
        print(self.equation)
        check = re.match(pattern, self.equation)

        if not check:
            raise ValueError('Invalid reaction syntax')

    def parse(self):
        reaction_symbol = re.search(r'(->|=)', self.equation)
        if reaction_symbol:
            eq = self.equation.split(reaction_symbol.group(0))
        else:
            raise ValueError('No reaction symbol found')

        reactants, products = [item.split('+') for item in eq]

        self.reactants = [ReactionItem(item) for item in reactants]
        self.products = [ReactionItem(item) for item in products]
        self.substances = self.reactants + self.products

        for subs in self.reactants:
            self.atoms.update(set(subs.composition.keys()))

    def get_coeffs_matrix(self):
        matrix = {key: [0]*len(self.substances) for key in self.atoms}

        for i, item in enumerate(self.substances):
            for atom, index in item.composition.items():
                if i < len(self.reactants):
                    matrix[atom][i] = index
                else:
                    matrix[atom][i] = -index

        return np.array(list(matrix.values()))

    def solve(self):
        coeffs = self.get_coeffs_matrix()
        combs = product(range(1, 12), repeat=len(self.atoms) + 1)

        for i in combs:
            solution = np.array(i)
            res = coeffs.dot(solution)

            if np.count_nonzero(res, axis=None) == 0:
                self.solution = list(solution)
                break

        for i, item in enumerate(self.substances):
            item.coeff = self.solution[i]

    def __str__(self):
        reactants = ' + '.join([str(item) for item in self.reactants])
        products = ' + '.join([str(item) for item in self.products])
        return f'{reactants} -> {products}'


class ReactionItem(Substance):
    def __init__(self, data, coeff: int = 1, *args, **kwargs):
        super().__init__(data, *args, **kwargs)
        self.coeff = coeff

    def __str__(self):
        formula = super().__str__()
        coeff = '' if self.coeff == 1 else self.coeff
        return f'{coeff}{formula}'

    def __repr__(self):
        res = super().__repr__()
        return f'{self.coeff}{res}'
