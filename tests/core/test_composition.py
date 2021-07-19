from chemical_calculators.core.composition import Composition


def test_add():
    comp1 = Composition({'H': 2, 'O': 1})
    comp2 = Composition({'O': 1})
    res = comp1 + comp2
    test = Composition({'H': 2, 'O': 2})

    assert res == test


def test_iadd():
    comp1 = Composition({'H': 2, 'O': 1})
    comp2 = Composition({'O': 1})
    comp1 += comp2
    test = Composition({'H': 2, 'O': 2})

    assert comp1 == test


def test_mul():
    comp1 = Composition({'H': 1, 'O': 1})
    comp2 = comp1 * 2
    test2 = Composition({'H': 2, 'O': 2})

    assert comp2 == test2

    # Checking for immutance
    test1 = Composition({'H': 1, 'O': 1})

    assert comp1 == test1


def test_imul():
    comp1 = Composition({'H': 1, 'O': 1})
    comp1 *= 2
    test = Composition({'H': 2, 'O': 2})

    assert comp1 == test


def test_not_equal():
    comp1 = Composition({'H': 2, 'O': 1})
    comp2 = Composition({'O': 1})

    assert comp1 != comp2
