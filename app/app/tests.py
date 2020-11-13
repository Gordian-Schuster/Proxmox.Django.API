from django.test import TestCase

from app.calc import add, subtract


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test adding two numbers"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """test subtracting numbers funktion"""
        self.assertEqual(subtract(6, 4), 2)
