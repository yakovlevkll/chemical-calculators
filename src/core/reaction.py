from string import ascii_letters
from itertools import product
from typing import Set, List
import numpy as np
import numpy.typing as npt

from .substance import Substance
from helpers.string import clean_ws

class Reaction:
    '''
    Reacton class

    TODO: add description
    '''

    def __init__(self, reaction: str):
        self.reaction: str = clean_ws(reaction)
        self.validate()

        self.atoms: Set[str] = set([])
        self.reactants: List[Substance] = []
        self.products: List[Substance] = []
        self.solution: List[int] = []

        self.parse()
        self.solve()

    def validate(self):
        allowed_chars = ascii_letters + '0123456789()->=+'

        for char in self.reaction:
            if not char in allowed_chars:
                raise ValueError(f'Unknown char found: `{char}`')


    def split(self):
        if '=' in self.reaction:
            reaction = self.reaction.split('=')
        elif '->' in self.reaction:
            reaction = self.reaction.split('->')
        else:
            raise ValueError('No reaction symbol found')

        return [item.split('+') for item in reaction]

    def parse(self):
        reactants, products = self.split()

        self.reactants = [Substance(item) for item in reactants]
        self.products = [Substance(item) for item in products]

        for subs in self.reactants:
            self.atoms.update(set(subs.composition.keys()))

    def solve(self):
        matrix = []

        for atom in self.atoms:
            coeffs = []

            for item in self.reactants:
                if atom in item.composition:
                    coeffs.append(item.composition[atom])
                else:
                    coeffs.append(0)

            for item in self.products:
                if atom in item.composition:
                    coeffs.append(-item.composition[atom])
                else:
                    coeffs.append(0)

            matrix.append(coeffs)

        coeffs: npt.ArrayLike = np.array(matrix)

        combs = product(range(1, 12), repeat=len(self.atoms) + 1)

        for i in combs:
            solution = np.array(i)
            res = coeffs.dot(solution)

            if np.count_nonzero(res, axis=None) == 0:
                self.solution = list(solution)
                break

    def __repr__(self):
        len_reactants = len(self.reactants)

        reactant_coeffs = self.solution[:len_reactants]
        product_coeffs = self.solution[len_reactants:]

        equation = [zip(reactant_coeffs, self.reactants),
                    zip(product_coeffs, self.products)]

        # equation = [
        #     [(2, Substance('H2')), (1, Substance('O2'))],
        #     [(2, Substance('H2O'))]
        #     ]

        solution = []

        for half in equation:
            temp = []
            for coeff, subs in half:
                if coeff == 1:
                    coeff = ''
                temp.append(f'{coeff}{subs.pretty_formula}')
            # temp = ['2H2', 'O2']
            solution.append(' + '.join(temp))
            # solution = ['2H2 + O2']

        # solution = ' -> '.join(solution)
        # solution = ['2H2 + O2', '2H2O']

        return f'''{solution[0]} -> {solution[1]} 
        ({self.reaction})'''
