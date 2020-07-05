from unittest import TestCase

from substance.substance import Substance


class TestSubstanceClass(TestCase):

    def test_one_char_symbol(self):
        sub = Substance('O')
        self.assertEqual(sub.composition, {'O': 1})
        self.assertEqual(sub.mass, 15.999)

    def test_two_chars_symbol(self):
        sub = Substance('He')
        self.assertEqual(sub.composition, {'He': 1})
        self.assertEqual(sub.mass, 4.0026)

    def test_one_char_symbol_with_index(self):
        sub = Substance('O3')
        self.assertEqual(sub.composition, {'O': 3})
        self.assertEqual(sub.mass, 47.997)

    def test_water(self):
        sub = Substance('H2O')
        self.assertEqual(sub.composition, {'H': 2, 'O': 1})
        self.assertEqual(sub.mass, 18.015)

    def test_carbon_dioxide(self):
        sub = Substance('CO2')
        self.assertEqual(sub.composition, {'C': 1, 'O': 2})

    def test_salt(self):
        sub = Substance('NaCl')
        self.assertEqual(sub.composition, {'Na': 1, 'Cl': 1})

    def test_cuprose(self):
        sub = Substance('Na2SO4')
        self.assertEqual(sub.composition, {'Na': 2, 'S': 1, 'O': 4})

    def test_distributed_atom(self):
        sub = Substance('C2H5OH')
        self.assertEqual(sub.composition, {'C': 2, 'H': 6, 'O': 1})
