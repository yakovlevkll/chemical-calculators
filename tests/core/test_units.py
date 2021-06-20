import pytest

from core.units import MassUnit, VolumeUnit


def test_mass_power():
    test = MassUnit('kg')

    assert test.final_exponent == 1

def test_volume_power_1():
    test = VolumeUnit('ml')

    assert test.final_exponent == 1

def test_volume_power_2():
    test = VolumeUnit('m^3')

    assert test.final_exponent == 3

def test_volume_power_3():
    test = VolumeUnit('cm^3')

    assert test.final_exponent == -6