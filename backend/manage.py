#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    project_path = os.path.abspath(os.path.dirname(__file__))
    sys.path.insert(0, project_path)
    print(f"DEBUG: Project path inserted into sys.path: {project_path}") # <--- ADD THIS LINE

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gatepass_project.settings.dev')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()