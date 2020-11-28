from django.test import TestCase

from app.calc import add, sub


class CalcTests(TestCase):
    def test_add_numbers(self):
        """Test that two numbers are added"""
        soma = add(3, 8)
        self.assertEqual(soma, 11)

    def test_subtract_numbers(self):
        """Test that two numbers are subtracted"""
        subtraction = sub(8, 3)
        self.assertEqual(subtraction, 5)
