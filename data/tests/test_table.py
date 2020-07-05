from unittest import TestCase

from data.table import TABLE


class TestPeriodicTable(TestCase):

    def test_out_of_range(self):
        with self.assertRaises(ValueError):
            TABLE[0]

    def test_unknown_atom(self):
        with self.assertRaises(ValueError):
            TABLE['Ab']
