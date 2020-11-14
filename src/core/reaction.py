from string import ascii_letters
from itertools import product

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
        self.solution: list[int] = []

        self.parse()
        self.solve()

    def validate(self):
        # TODO: Improve validation
        allowed_chars = ascii_letters + '0123456789()->=+'

        for char in self.equation:
            if not char in allowed_chars:
                raise ValueError(f'Unknown char found: `{char}`')

    def parse(self):
        if '=' in self.equation:
            eq = self.equation.split('=')
        elif '->' in self.equation:
            eq = self.equation.split('->')
        else:
            raise ValueError('No reaction symbol found')

        reactants, products = [item.split('+') for item in eq]

        self.reactants = [ReactionItem(item) for item in reactants]
        self.products = [ReactionItem(item) for item in products]

        for subs in self.reactants:
            self.atoms.update(set(subs.composition.keys()))

    def get_coeffs_matrix(self):
        r_len = len(self.reactants)
        p_len = len(self.products)
        items_len = r_len + p_len
        matrix = {key: [0]*items_len for key in self.atoms}

        for i, item in enumerate(self.reactants):
            for atom, index in item.composition.items():
                matrix[atom][i] += index

        for i, item in enumerate(self.products):
            for atom, index in item.composition.items():
                matrix[atom][i + r_len - 1] += index

        return np.array(list(matrix.values()))

    def solve(self):
        coeffs = self.get_coeffs_matrix()
        combs = product(range(1, 12), repeat=len(self.atoms) + 1)

        for i in combs:
            solution = np.array(i)
            res = coeffs.dot(solution)

            if np.count_nonzero(res, axis=None) == 0:
                self.solution = list(solution)
                print(solution)
                break

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
