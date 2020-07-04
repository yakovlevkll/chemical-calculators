from string import ascii_letters

from substance import Substance

from itertools import product
import numpy as np


class Reaction:
    def __init__(self, reaction):
        self.plain_reaction = reaction
        self.sanitize()
        self.sepparate()
        self.find_atoms()
        self.solve()

    def sanitize(self):
        # Delete all unecessary chars
        chars_to_left = ascii_letters + '0123456789()->=+'
        temp = []
        for char in self.plain_reaction:
            if char in chars_to_left:
                temp += char
        self.clean_form = ''.join(temp)

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
                self.solution = solution
                break

    def __repr__(self):
        solution = ''

        solution += ' + '.join([item.pretty_formula for item in self.reactants])

        solution += ' -> '

        solution += ' + '.join([item.pretty_formula for item in self.products])

        return f'{self.solution} ({self.plain_reaction})'


if __name__ == "__main__":
    test = Reaction('H2 + O2 = H2O')
    print(test)
