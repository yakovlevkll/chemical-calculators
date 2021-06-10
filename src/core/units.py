import re


class Unit:
    power: int = 0
    original_unit: str = ''

    prefixes = {
        'm': -3,
        'c': -2,
        'k':3,
        'M':6,
    }

    base_units: list[str]
    base_power: int

    def __init__(self, unit: str):
        if not self.base_units:
            raise NotImplementedError('Child unit class must provide a list with base units')
        
        prefix, original_unit = self.split_into_components(unit)

        self.original_unit = original_unit

        if prefix:
            self.power = self.prefixes[prefix]

    def split_into_components(self, unit):
        '''
        Returns ('k', 'g') from kg
        '''

        # combines base units into a string
        prefix = '|'.join(self.prefixes.keys())
        units = '|'.join(self.base_units)# --> 'g'
        regexp = f'^({prefix})*({units})$'
        # regexp = f'^(\d+\.{0,1}\d*)(m|k|M)*(g|pound|l)$'
        # Find with regexp
        match = re.match(regexp, unit)
        if match:
            return match.group(1), match.group(2)
        else:
            raise ValueError
         




class MassUnit(Unit):
    base_units = ['g']
    base_power = 1

    

class VolumeUnit(Unit):
    base_units = ['l', 'm^3']
    base_power = 3

class Moles(Unit):
    pass


