
from .units import MassUnit, VolumeUnit, Moles, Unit
import re
from typing import Optional, Tuple

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
        coeff, unit_str = self.split_coeff()
        
        self.coeff = coeff
        
        self.unit = self.check_unit(unit_str)
        # converts everything to moles
        # self.to_moles()
        self.quantity_value = coeff * 10**self.unit.final_exponent * self.unit.conv_value
        

    def split_coeff(self) -> Tuple[float, str]:
        '''
        separates coefficient from the index-unit
        Example 1: 5kg --> 5, kg
        Example 2: 4cl --> 4, cl
        '''
        # combines base units into a string
        
        regexp = r'^(\d+\.{0,1}\d*)([A-z\^\d]+)$'

        # Find with regexp
        match = re.match(regexp, self.user_input)
        if match:
            coeff = float(match.group(1)) if match.group(1) else 1
            return coeff, match.group(2)
        else:
            raise ValueError
    
    def get_SI_coeff(self):
        print(self.coeff*self.unit.conv_value)
        return self.coeff * self.unit.conv_value
        
    def check_unit(self, unit_str: str) -> Unit: #Some kind of error here
        '''
        Checks to determine the appropriate class (i.e. Mass, Volume or Moles)

        Runs units.py through each class until a non-error solution is obtained
        '''
        unit_classes = [MassUnit, VolumeUnit, Moles]

        for unit_cls in unit_classes:
            try:
                return unit_cls(unit_str)
            except:
                continue

        raise ValueError(f'Unknown units given - {unit_str}')

    def get_moles(self) -> float:
        '''
        Get quantity in moles
        '''
        if isinstance(self.unit, MassUnit):
            pass
        elif isinstance(self.unit, VolumeUnit):
            pass

        return 0.0

    def get_mass(self, unit: str) -> float:
        '''
        get quantity in specified mass units
        '''

        return 0.0

    def get_volume(self, unit: str) -> float:
        '''
        converts volume (xl, xm^3) to amount of substance (moles)
        '''
        return 0.0




    

