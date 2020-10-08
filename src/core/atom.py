'''
Atom class.

'''


class Atom:
    '''
    '''

    Z = 0
    symbol = ''
    name = ''
    mass = 0
    electron_config = ''

    def __init__(self, Z, symbol, mass):
        self.Z = Z
        self.symbol = symbol
        self.mass = mass

    def find_electron_config(self):
        pass

    def __repr__(self):
        return f'{self.symbol}\nMass: {self.mass}'
