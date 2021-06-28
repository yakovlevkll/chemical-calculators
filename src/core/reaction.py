from string import ascii_letters
from itertools import product

import re
import numpy as np
from numpy.lib.npyio import recfromtxt

from .substance import Substance
from helpers.string import clean_ws

from .quantities import Quantities


class Reaction:
    '''
    Reaction class.

    TODO: add description
    '''

    def __init__(self, equation: str, quantities: list[str] = None):  
        # TODO: Add comments
        self.equation: str = clean_ws(equation)
        self.validate()

        self.atoms: set[str] = set([])
        self.reactants: list[ReactionItem] = []
        self.products: list[ReactionItem] = []
        self.substances: list[ReactionItem] = []
        self.solution: list[int] = []

        if quantities:
            self.quantities = quantities

        self.parse()
        self.solve()

    def validate(self):
        # TODO: Improve validation

        subs_symbols = '[A-z\d\(\)\[\]]'
        reactant_pattern = f'({subs_symbols}+\+)*{subs_symbols}+'
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
        # The system of linear equations to be solved is represented in the form of matrix AX = B

        # Select all columns except the last one
        A = coeffs[:, :-1]

        # Select the last column
        B = -coeffs[:, -1]
        
        # Solution could be found as X = A^-1 * B
        # X = np.linalg.inv(A).dot(B)

        # Alternative way
        try:
            X = np.linalg.solve(A, B)
            self.find_coeffs(X)
        except:
            self.solve_backup()
        for i, item in enumerate(self.substances):
            item.coeff = self.solution[i]


        # Check that all coeffs are integers
    def find_coeffs(self, X):
        for i in range(1,50):
            probe = i * X
            probe_int = np.around(probe)

            if np.allclose(probe, probe_int):
                solution = list(probe_int.astype(int))
                solution.append(i)
                self.solution = solution
                break

            #if the matrix isn't square
    def solve_backup(self):
        coeffs = self.get_coeffs_matrix()
            #generates possible combinations
        combs = product(range(1, 12), repeat=coeffs.shape[1])

        for i in combs:
            solution = np.array(i)
            res = coeffs.dot(solution)

            if np.count_nonzero(res, axis=None) == 0:
                self.solution = list(solution)
                break

       

    def __str__(self):
        reactants = ' + '.join([str(item) for item in self.reactants])
        products = ' + '.join([str(item) for item in self.products])
        return f'{reactants} -> {products}'


class ReactionItem(Substance):
    def __init__(self, data, coeff: int = 1, quantity: str = None, *args, **kwargs):
        super().__init__(data, *args, **kwargs)
        self.coeff = coeff
        if quantity:
            self.quantity = Quantities(quantity, self.mass)
        

    def __str__(self):
        formula = super().__str__()
        coeff = '' if self.coeff == 1 else self.coeff
        return f'{coeff}{formula}'

    def __repr__(self):
        res = super().__repr__()
        return f'{self.coeff}{res}'


