"""
 Django command to wait for database to be available
"""
from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg20pError
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to wait for database to be available"""

    def handle(self, *args, **options):
        """ Entry point for command """
        self.stdout.write('Waiting for database...')
        db_up = False
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg20pError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
