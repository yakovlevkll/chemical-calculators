from src.reaction import Reaction


def test_arrow():
    react = Reaction('H2 + O2 -> H2O')

    assert react.solution == [2, 1, 2]


def test_equal_sign():
    react = Reaction('CO2 + H2O = C6H12O6 + O2')

    assert react.solution == [6, 6, 1, 6]


def test_substances_with_brackets():
    react = Reaction('Al + HNO3 = Al(NO3)3 + NH4NO3 + H2O')
    
    assert react.solution == [8, 30, 8, 3, 9]
