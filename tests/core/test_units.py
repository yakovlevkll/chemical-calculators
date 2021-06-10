import pytest

from core.units import MassUnit, VolumeUnit


def test_mass_power():
    test = MassUnit('50.2kg')

    assert test.power == 3

def test_volume_power():
    test = VolumeUnit('50.2ml')

    assert test.power == -3