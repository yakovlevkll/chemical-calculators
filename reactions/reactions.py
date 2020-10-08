from string import ascii_letters

from substance.substance import Substance

from itertools import product
import numpy as np

from helpers.string import clean_str


class Reaction:
    def __init__(self, reaction):
        self.plain_reaction = reaction
        self.validate()
        self.sepparate()
        self.find_atoms()
        self.solve()

    def validate(self):
        # Delete all unnecessary chars

        self.clean_form = clean_str(
            self.plain_reaction, ascii_letters + '0123456789()->=+')

    def sepparate(self):
        self.reactants = []
        self.products = []

        # use split function to separate

        if '=' in self.clean_form:
            temp_form = self.clean_form.split('=')

        elif '->' in self.clean_form:
            temp_form = self.clean_form.split('->')

        else:
            raise ValueError('No reaction symbol found')

        self.reactants = temp_form[0].split('+')
        self.products = temp_form[1].split('+')

    def find_atoms(self):
        self.atoms = set([])

        self.reactants = [Substance(item) for item in self.reactants]
        self.products = [Substance(item) for item in self.products]

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

        coeffs = np.array(matrix)

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
        ({self.plain_reaction})'''


if __name__ == "__main__":
    test = Reaction('H2 + O2 = H2O')
    print(test)
