import pytest
from core.quantities import Quantities

def test_self_mass():
    q = Quantities('2.5kg', 3, 'Mass')

    assert q.to_mass() == 2500

def test_self_volume():
    q = Quantities('1500cl', 1, 'Volume')

    assert q.to_volume() == 0.015

def test_self_moles():
    q = Quantities('30mol', 1, 'Mole')

    assert q.to_moles() == 30

def test_impirial_vol():
    q = Quantities('45in3', 1, 'Volume')

    assert q.to_volume() == pytest.approx(0.000737418)


def test_prefix_metric_volume():

    assert Quantities('5cm3', 1, 'Volume').to_volume() == pytest.approx(5 * 10**-6)
    assert Quantities('12mm3', 1, 'Volume').to_volume() == pytest.approx(12 * 10**-9)
    assert Quantities('25.6cm3', 1, 'Volume').to_volume() == pytest.approx(25.6 * 10**-6)
