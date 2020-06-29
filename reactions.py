from string import ascii_letters

from substance import Substance


class Reaction:
    def __init__(self, reaction):
        self.plain_reaction = reaction
        self.sanitize()
        self.split()
        self.find_atoms()
        self.solve()

    def sanitize(self):
        # Delete all unecessary chars
        chars_to_left = ascii_letters + '0123456789()->=+'
        self.clean_form = []
        for char in self.plain_reaction:
            if char in char_to_left:
                self.clean_form += char

    def split(self):
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
            self.atoms.add(subs.composition.keys())

        self.reactants = [Substance('H2'), Substance('O2')]
        self.products = [Substance('H2O')]

    def solve(self):
    'def matrices(self):'

    def __repr__(self):
        solution = ''

        for item in self.reactants:
            pass

        solution += '->'

        for item in self.products:
            pass

        return f'''Reaction given: {self.plain_reaction}
        Solution: {solution}
        '''
