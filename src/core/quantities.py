

import re
from typing import Optional

# cases
# 1. given quantities -> find excess or how much is needed
# EXAMPLE ---> H2+O2->H2O :  X quantity of H + Y quantity of O
# 2. Final quantities given -> find initial quantities

# aos == Amount of Substance

class Unit:
    coeff: float = 0
    original_unit: str = ''

    prefixes = {
        'm': -3,
        'c': -2,
        'k':3,
        'M':6,
    }

    base_units: list[str] = None
    base_power: int = None

    def __init__(self, unit: str):
        coeff, prefix, original_unit = self.split_into_components(unit)

        self.coeff = float(coeff)
        self.original_unit = original_unit

        if prefix:
            exponent = self.prefixes[prefix]
            self.coeff *= 10 ** exponent

    def split_into_components(self, unit):
        '''
        Returns (5, 'k', 'g') from 5kg
        '''

        if not self.base_units:
            raise NotImplementedError('Child unit class must provide a list with base units')

        # combines base units into a string
        coeff = '\d+\.{0,1}\d*'
        prefix = '|'.join(self.prefixes.keys())
        units = '|'.join(self.base_units)# --> 'g'
        regexp = f'^({coeff})({prefix})*({units})$'
        # regexp = f'^(\d+\.{0,1}\d*)(m|k|M)*(g|pound|l)$'
        # Find with regexp
        match = re.match(regexp, unit)
        if match:
            return match.group(1), match.group(2), match.group(3)
        else:
            raise ValueError


class MassUnit(Unit):
    base_units = ['g']
    base_power = 1

    

class VolumeUnit(Unit):
    base_units = ['l', 'm^3']
    base_power = 3




class Quantities:
    '''
    Quantity description here
    '''
    # coefficient before the unit
    amount: float = 0
    # unit of measurement (g, ml, cm^3...etc)
    unit: Optional[Unit] = None
    
    def __init__(self, amount: float, unit: str):
        # finds excess
        self.excess()
        # converts everything to moles
        self.to_moles()
        

    def excess(self):
        '''
        difference between mass on right and mass on left
        '''
        pass

    def to_moles(self, amount: float, units: str):
        '''
        Generic converts units to moles
        Calls situation-specific functions
        '''
        pass

    def mass_to_aos(self) -> float:
        '''
        converts mass (g, kg, ...) to amount of substance (moles)
        '''
        return 0.0

    def volume_to_aos(self) -> float:
        '''
        converts volume (ml, l, m3, dm3, cm3, ...) to amount of substance (moles)
        '''
        return 0.0

    def aos_to_mass(self, units: MassUnit):
        '''
        converts amount of substance (moles) to mass (g, kg, ...)
        '''
        pass

    def aos_to_volume(self, units: VolumeUnit):
        '''
        converts amount of substance (moles) to volume (ml, l, m3, dm3, cm3, ...)
        '''
        pass
        

if __name__ == '__main__':
    test = VolumeUnit('50.2ml')
    print(test.coeff, test.original_unit)