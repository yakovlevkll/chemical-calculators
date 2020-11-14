import pytest

from core.reaction import Reaction


def test_arrow():
    react = Reaction('H2 + O2 -> H2O')

    assert react.solution == [2, 1, 2]


def test_equal_sign():
    react = Reaction('CO2 + H2O = C6H12O6 + O2')

    assert react.solution == [6, 6, 1, 6]


@pytest.mark.skip('Not implemented yet')
def test_substances_with_brackets_1():
    react = Reaction('FeCl3 + NaOH = Fe(OH)3 + NaCl')

    assert react.solution == [1, 3, 1, 3]


@pytest.mark.skip('Not implemented yet')
def test_substances_with_brackets_2():
    react = Reaction('Fe(OH)3 + H2SO4 = Fe2(SO4)3 + H2O')

    assert react.solution == [2, 3, 1, 6]


@pytest.mark.skip('Takes algorithm long time to solve')
def test_substances_with_brackets_3():
    react = Reaction('Al + HNO3 = Al(NO3)3 + NH4NO3 + H2O')

    assert react.solution == [8, 30, 8, 3, 9]
