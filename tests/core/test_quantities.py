import pytest

from chemical_calculators.core.quantity import Quantity
from chemical_calculators.core.typings import UnitType


def test_self_mass():
    q = Quantity('50mg', 1, UnitType.mass)

    assert q.to_mass() == 0.05


def test_self_volume():
    q = Quantity('1500cl', 1, UnitType.volume)

    assert q.to_volume() == 0.015


def test_self_moles():
    q = Quantity('30mol', 1, UnitType.moles)

    assert q.to_moles() == 30


def test_impirial_vol():
    q = Quantity('45in3', 1, UnitType.volume)

    assert q.to_volume() == pytest.approx(0.000737418)


def test_prefix_metric_volume():
    assert Quantity('5cm3', 1, UnitType.volume).to_volume(
    ) == pytest.approx(5 * 10**-6)
    assert Quantity('12mm3', 1, UnitType.volume).to_volume(
    ) == pytest.approx(12 * 10**-9)
    assert Quantity('25.6cm3', 1, UnitType.volume).to_volume(
    ) == pytest.approx(25.6 * 10**-6)
