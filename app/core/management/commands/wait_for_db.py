import time
from typing import Optional, Any

from django.db import connections
from django.db.utils import OperationalError
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Django command to pause boot until db is ready"""
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        self.stdout.write('waiting for db...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('db not ready, waiting 1 more sec.')
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS('db is finally ready!'))