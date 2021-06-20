import pytest
from core.quantities import Quantities

def test_self_mass():
    q = Quantities('2.5kg', 1)

    assert q.to_mass() == 2500

def test_self_volume():
    q = Quantities('1500cl', 1)

    assert q.to_volume() == 0.015

def test_self_moles():
    q = Quantities('30mol', 1)

    assert q.to_moles() == 30

def test_empirical_vol():
    q = Quantities('45inch^3',1)

    assert q.to_volume == 0.000737418