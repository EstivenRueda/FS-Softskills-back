#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import dotenv


def main():
    # Environment values
    file_path = os.path.join(os.path.dirname(__file__), ".env")
    if os.path.exists(file_path):
        dotenv.read_dotenv(file_path)

    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "finishing_school.settings.local")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
