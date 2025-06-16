from os import environ

import django

environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
