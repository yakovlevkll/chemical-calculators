import pytest

from chemical_calculators.core.substance import Substance


def test_one_char_symbol():
    sub = Substance('O')

    assert sub.composition == {'O': 1}
    assert sub.mass == 15.999


def test_two_chars_symbol():
    sub = Substance('He')

    assert sub.composition == {'He': 1}
    assert sub.mass == pytest.approx(4.0026, 3)


def test_one_char_symbol_with_index():
    sub = Substance('O3')

    assert sub.composition == {'O': 3}
    assert sub.mass == 47.997


def test_water():
    sub = Substance('H2O')

    assert sub.composition == {'H': 2, 'O': 1}
    assert sub.mass == 18.015


def test_carbon_dioxide():
    sub = Substance('CO2')

    assert sub.composition == {'C': 1, 'O': 2}


def test_salt():
    sub = Substance('NaCl')

    assert sub.composition == {'Na': 1, 'Cl': 1}


def test_soda():
    sub = Substance('Na2CO3')

    assert sub.composition == {'Na': 2, 'C': 1, 'O': 3}


def test_spread_atom():
    sub = Substance('C2H5OH')

    assert sub.composition == {'C': 2, 'H': 6, 'O': 1}


def test_single_brackets_1():
    sub = Substance('Ba(OH)2')

    assert sub.composition == {'Ba': 1, 'O': 2, 'H': 2}


def test_single_brackets_2():
    sub = Substance('PtCl2(NH3)2')

    assert sub.composition == {'Pt': 1, 'Cl': 2, 'N': 2, 'H': 6}


def test_two_single_brackets():
    sub = Substance('Fe(H2O)4(OH)2')

    assert sub.composition == {'Fe': 1, 'O': 6, 'H': 10}


def test_nested_brackets():
    sub = Substance('TiCl2[(CH3)2PCH2CH2P(CH3)2]2')

    assert sub.composition == {
        'Ti': 1, 'Cl': 2, 'C': 12, 'H': 32, 'P': 4}


def test_brackets_fail_1():
    with pytest.raises(ValueError):
        sub = Substance('Ti[(CH3)2')


def test_brackets_fail_1():
    with pytest.raises(ValueError):
        sub = Substance('Ti[(CH3])2')


def test_unknown_element():
    with pytest.raises(ValueError):
        sub = Substance('A3')


def test_lowercase():
    with pytest.raises(ValueError):
        sub = Substance('H2Clo')


def test_empty_string():
    with pytest.raises(ValueError):
        sub = Substance('')


def test_garbage():
    with pytest.raises(ValueError):
        sub = Substance('()12')
