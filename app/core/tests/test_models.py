from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user"""
        email = "math@darkm.com.br"
        password = "pass123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test if new user email is normalized"""
        raw_email = "lala@CAPSLOCK.com"
        user = get_user_model().objects.create_user(raw_email, 'randompass')

        self.assertEqual(user.email, raw_email.lower())

    def test_new_user_invalid_email(self):
        """Test try to create user with no email expects error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'randompass')

    def test_create_a_super_user(self):
        """Test should create a new user with super powers"""
        user = get_user_model().objects.create_superuser(
            'test@darkmath.com',
            'randompass'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
