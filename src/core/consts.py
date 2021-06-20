
class Consts:

    @property
    def NA(self) -> float:
        '''
        Avogadro constant
        '''
        return 6.02214076 * 10**23

    @property
    def kB(self) -> float:
        '''
        Boltzmann constant
        '''
        return 1.380649 * 10** (-23)

    @property
    def R(self) -> float:
        '''
        Ideal gas constant
        '''
        return self.NA * self.kB

class Empirical:
    '''
    For unit-austronauts, metric is for real humans)
    '''

    INCH = 0.0254