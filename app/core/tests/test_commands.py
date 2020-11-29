from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTest(TestCase):
    
    def test_wait_for_db_ready(self):
        """Test waiting for db when db is on"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as db:
            db.return_value = True
            call_command('wait_for_db')

            self.assertEqual(db.call_count, 1)

    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, sleep):
        """Test waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as db:
            db.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')

            self.assertEqual(db.call_count, 6)
