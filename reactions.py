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
        coeffs = np.array([[1, 0, -2, 0, 0, 0], [1, 0, 0, 0, -1, 0],
                           [3, 4, -12, 0, -2, -1], [0, 2, 0, 0, 0, -2], [0, 1, -3, -1, 0, 0]])

        combs = product(range(1, 12), repeat=6)

        for i in combs:
            solution = np.array(i)
            res = coeffs.dot(solution)

            if np.count_nonzero(res, axis=None) == 0:
                print(res, solution)
                break

    def __repr__(self):
        solution = ''

        solution += ' + '.join([item.pretty_formula for item in self.reactants])

        solution += ' -> '

        solution += ' + '.join([item.pretty_formula for item in self.products])

        return f'''Reaction given: {self.plain_reaction}
        Solution: {solution}
        '''


if __name__ == "__main__":
    test = Reaction('H2 + O2 = H2O')
    print(test)
