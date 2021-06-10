
from .units import MassUnit, VolumeUnit, Moles, Unit
import re
from typing import Optional

# cases
# 1. given quantities -> find excess or how much is needed
# EXAMPLE ---> H2+O2->H2O :  X quantity of H + Y quantity of O
# 2. Final quantities given -> find initial quantities

# aos == Amount of Substance

class Quantities:
    coeff: float
    unit: Unit

    def __init__(self, unit_quantity: str, molar_mass: float):
        self.user_input = unit_quantity
        # finds excess
        coeff, unit_str = self.find_coeff_unit_pair()
        self.coeff = coeff
        self.unit = self.check_unit(unit_str)

        self.excess()
        # converts everything to moles
        # self.to_moles()

    def find_coeff_unit_pair(self):
        '''
        Returns (5, 'kg') from 5kg
        '''
        # combines base units into a string
        
        regexp = r'^(\d+\.{0,1}\d*)([A-z\^\d]+)$'

        # Find with regexp
        match = re.match(regexp, self.user_input)
        if match:
            return float(match.group(1)), match.group(2)
        else:
            raise ValueError
    
        
    def check_unit(self, unit_str: str) -> Unit:
        unit_classes = [MassUnit, VolumeUnit, Moles]
        res = None
        for unit_cls in unit_classes:
            try:
                res = unit_cls(unit_str)
                break
            except:
                pass

        if res:
            return res
        else:
            raise ValueError(f'Unknown units given - {unit_str}')

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
        converts mass (xg) to amount of substance (moles)
        '''


        return 0.0

    def volume_to_aos(self) -> float:
        '''
        converts volume (xl, xm^3) to amount of substance (moles)
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




    

