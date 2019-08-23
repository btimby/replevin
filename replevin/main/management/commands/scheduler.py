from django.core.management.base import BaseCommand, CommandError
from main.models import Backup, Restore


class Command(BaseCommand):
    help = 'Schedules and executes backup and restore jobs.'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        pass
