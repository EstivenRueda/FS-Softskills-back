# Stdlib imports
import os

# Core Django imports
from django.core.management import call_command
from django.core.management.base import BaseCommand

# Imports from your apps
from apps.core import utils


class Command(BaseCommand):
    help = "Use this command to load all the production fixtures set"

    def handle(self, **kwargs):
        self.load_production_fixtures()
        self.stdout.write("Data was loaded successfully!")

    def load_production_fixtures(self):
        """
        Read each of the production fixtures files contained in the folder.
        """

        production_fixtures = self.get_production_fixtures()
        for fixture in production_fixtures:
            try:
                call_command(
                    "loaddata",
                    f"{fixture}",
                )
            except Exception as err:
                print(err)

    def get_production_fixtures(self):
        """
        Gets the name of all production fixtures files contained in the production fixtures folder.
        """
        production_fixtures = os.listdir("production_fixtures")
        return utils.sorted_alphanumeric(production_fixtures)
