from django.test import TestCase

from app.calc import add

class CalcTests(TestCase):
    def test_add_numbers(self):
        """Test that two numbers are added"""
        soma = add(3,8)
        self.assertEqual(soma, 11)