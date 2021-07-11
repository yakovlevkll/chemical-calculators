import pytest

from core.reaction import Reaction


def test_arrow():
    react = Reaction('H2 + O2 -> H2O')

    assert react.solution == [2, 1, 2]


def test_equal_sign():
    react = Reaction('CO2 + H2O = C6H12O6 + O2')

    assert react.solution == [6, 6, 1, 6]


# @pytest.mark.skip('Not implemented yet')
def test_substances_with_brackets_1():
    react = Reaction('FeCl3 + NaOH = Fe(OH)3 + NaCl')

    assert react.solution == [1, 3, 1, 3]


# @pytest.mark.skip('Not implemented yet')
def test_substances_with_brackets_2():
    react = Reaction('Fe(OH)3 + H2SO4 = Fe2(SO4)3 + H2O')

    assert react.solution == [2, 3, 1, 6]


@pytest.mark.skip('Takes algorithm long time to solve')
def test_substances_with_brackets_3():
    react = Reaction('Al + HNO3 = Al(NO3)3 + NH4NO3 + H2O')

    assert react.solution == [8, 30, 8, 3, 9]

@pytest.mark.skip()
def test_suspicious_reaction_1():
    react = Reaction('H2S + KMnO4 + H2SO4 = S + MnSO4 + K2SO4 + H2O')

    assert react.solution == [2, 2, 2, 1, 2, 1, 4]

@pytest.mark.skip()
def test_suspicious_reaction_2():
    react = Reaction('KNO2 + K2Cr2O7 + H2SO4 = KNO3 + Cr2(SO4)3 + K2SO4 + H2O')

    assert react.solution == []

def test_excess():
    '''
    Reaction        3Pb + 2H3PO4 = 3H2 + Pb3(PO4)2
    User_moles      9       10
    normalized       *3       *5
    min_val         min
    optimal          9       6       9     3
    excess          0       4
    '''

    r = Reaction('Pb + H3PO4 = H2 + Pb3(PO4)2', ['9mol', '10mol', '', ''])

    assert r.reaction_items[0].optimal_moles == 9
    assert r.reaction_items[1].optimal_moles == 6
    assert r.reaction_items[2].optimal_moles == 9
    assert r.reaction_items[3].optimal_moles == 3
