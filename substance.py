'''
Chemical substance class.

Features:

- Determines substance composition
- Calculates molar (atomic) mass of a substance
- Beautifies chemical formula for text output
'''

from helpers import subscript_it


class Substance:

    '''
    Main class for substance.

    formula - something like `H20`
    pretty_formula - beautified version of the formula
    composition - self-descriptive, something like {'H': 2, 'O': 1}
    mass - molar (atomic) mass
    '''

    formula = ''
    pretty_formula = ''
    composition = {}
    mass = 0

    MASSES = {
        'H': 1.008,
        'He': 4.0026,
        'Li': 6.94,
        'Be': 9.0122,
        'B': 10.81,
        'C': 12.011,
        'N': 14.007,
        'O': 15.999,
        'F': 18.998,
        'Ne': 20.18,
        'Na': 22.99,
        'Mg': 24.305,
        'Al': 26.982,
        'Si': 28.085,
        'P': 30.974,
        'S': 32.06,
        'Cl': 35.45,
        'Ar': 39.948,
        'K': 39.098,
        'Sc': 44.956,
        'Ti': 47.867,
        'V': 50.942,
        'Cr': 51.996,
        'Mn': 54.938,
        'Fe': 55.845,
        'Co': 58.933,
        'Ni': 58.693,
        'Cu': 63.546,
        'Zn': 65.39,
        'Ga': 69.723,
        'Ge': 72.64,
        'As': 74.922,
        'Se': 78.96,
        'Br': 79.904,
        'Kr': 83.798,
        'Rb': 85.468,
        'Sr': 87.62,
        'Y': 88.906,
        'Zr': 91.224,
        'Nb': 92.906,
        'Mo': 95.95,
        'Tc': 98,
        'Ru': 101.07,
        'Rh': 102.91,
        'Pd': 106.42,
        'Ag': 107.87,
        'Cd': 112.41,
        'In': 114.82,
        'Sn': 118.71,
        'Sb': 121.76,
        'Te': 127.60,
        'I': 126.90,
        'Xe': 131.29,
        'Cs': 132.91,
        'Ba': 137.33,
        'La': 138.91,
        'Ce': 140.12,
        'Pr': 140.92,
        'Nd': 144.24,
        'Pm': 145,
        'Sm': 150.36,
        'Eu': 151.96,
        'Gd': 157.25,
        'Tb': 158.93,
        'Dy': 162.50,
        'Ho': 164.93,
        'Er': 167.26,
        'Tm': 168.26,
        'Yb': 173.05,
        'Lu': 174.97,
        'Hf': 178.49,
        'Ta': 180.95,
        'W': 183.84,
        'Re': 186.21,
        'Os': 190.23,
        'Ir': 192.22,
        'Pt': 195.08,
        'Au': 196.97,
        'Hg': 200.59,
        'Tl': 204.38,
        'Pb': 207.2,
        'Bi': 208.98,
        'Po': 209,
        'At': 210,
        'Rn': 222,
        'Fr': 223,
        'Ra': 226,
        'Ac': 227,
        'Th': 232.04,
        'Pa': 231.04,
        'U': 238.03,
        'Np': 237,
        'Pu': 244,
        'Am': 243,
        'Cm': 247,
        'Bk': 247,
        'Cf': 251,
        'Es': 252,
        'Fm': 257,
        'Md': 258,
        'No': 259,
        'Lr': 266,
        'Rf': 267,
        'Db': 268,
        'Sg': 269,
        'Bh': 270,
        'Hs': 270,
        'Mt': 278,
        'Ds': 281,
        'Rg': 282,
        'Cn': 285,
        'Nh': 286,
        'Fl': 289,
        'Mc': 290,
        'Lv': 293,
        'Ts': 294,
        'Og': 294
    }

    def __init__(self, formula):
        self.formula = formula
        self.validate_formula()
        self.prettify_formula()
        self.find_composition()
        self.find_mass()

    def validate_formula(self):
        for char in self.formula:
            if not char.isascii() or not char.isalnum():
                raise ValueError(
                    f'Unknown character found - `{char}`')

    def prettify_formula(self):
        '''
        Turns `H2O` into `H₂O`
        '''

        chars = list(self.formula)

        self.pretty_formula = ''.join([subscript_it(char) for char in chars])

    def find_composition(self):
        '''
        Determines atomic composition of a substance
        '''

        self.composition = {}

        pairs = []

        # Split formula in atom-index pairs
        for char in self.formula:
            if char.isupper():
                pairs.append([char, ''])
            elif char.islower():
                pairs[-1][0] += char
            else:
                pairs[-1][1] += char

        for pair in pairs:
            name, index = pair
            if not name in self.MASSES:
                raise ValueError(f'Unknown atom found - `{name}`')

            if index == '':
                index = 1
            else:
                index = int(index)

            if not name in self.composition:
                self.composition.setdefault(name, index)
            else:
                self.composition[name] += index

    def find_mass(self):
        '''
        Finds molar (atomic) mass of a substance
        '''

        self.mass = 0

        for name, amount in self.composition.items():
            self.mass += self.MASSES[name] * amount

        self.mass = round(self.mass, 3)

    def __repr__(self):
        return f'''
        Formula: {self.pretty_formula}
        Composition: {self.composition}
        Mass: {self.mass} g/mol
        '''


if __name__ == "__main__":
    # For testing purposes
    subs = [
        Substance('H2O'),
        Substance('C6H12O6'),
        Substance('Na2SO4'),
        Substance('C2H5OH'),
        Substance('CO2'),
        Substance('He'),
        Substance('O3')
    ]

    for sub in subs:
        print(sub)
