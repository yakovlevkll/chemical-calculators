import re
from typing import NamedTuple


class Unit:
    user_unit: str
    power: int = 0

    prefixes = {
        'm': -3,
        'c': -2,
        'k':3,
        'M':6,
    }

    # Must be defined in children classes
    BASE_UNIT: str
    BASE_POWER: int
    CONVERSIONS: dict[str, float]

    def __init__(self, unit: str):
        '''
        unit: `kg`, for example
        '''
        if not (self.CONVERSIONS and self.BASE_UNIT and self.BASE_POWER):
            raise NotImplementedError('Child unit class must provide ...')
        
        prefix, unit = self.split_into_components(unit)

        self.user_unit = unit

        if prefix:
            self.power = self.prefixes[prefix]

    def split_into_components(self, unit):
        '''
        Returns ('k', 'g') from kg
        '''

        # combines base units into a string
        prefix = '|'.join(self.prefixes.keys())
        units = '|'.join(self.CONVERSIONS.keys())# --> 'g'
        regexp = f'^({prefix})*({units})$'
        # regexp = f'^(\d+\.{0,1}\d*)(m|k|M)*(g|pound|l)$'
        # Find with regexp
        match = re.match(regexp, unit)
        if match:
            return match.group(1), match.group(2)
        else:
            raise ValueError

    def convert(self, to: str):
        # TODO: Implement
        pass

    def convert_to_user_unit(self):
        return self.convert(self.user_unit)

class FactorExpPair(NamedTuple):
    factor: float
    exp: float


class MassUnit(Unit):
    BASE_UNITS = ['g']
    CONVERSIONS = {
        'g': 1,
        'ounce': 2.424,
    }
    BASE_POWER = 1
    

class VolumeUnit(Unit):
    BASE_UNITS = ['l', 'm^3']
    CONVERSIONS = {
        'm^3': FactorExpPair(1, 3),
        'l': FactorExpPair(0.001, 1),
    }
    BASE_POWER = 3


class Moles(Unit):
    pass
