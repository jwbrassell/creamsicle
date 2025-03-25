"""
ASGI config for Django project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

# Import the config singleton which handles Python path
from UniqueName.config import config

# Set default settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', config.get_settings_module())

from django.core.asgi import get_asgi_application

application = get_asgi_application()
