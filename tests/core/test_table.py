import pytest

from core.table import TABLE


def test_out_of_range():
    with pytest.raises(ValueError):
        TABLE[0]


def test_unknown_atom():
    with pytest.raises(ValueError):
        TABLE['Ab']
