"""
WSGI config for Django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

# Import the config singleton which handles Python path
from UniqueName.config import config

# Set default settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', config.get_settings_module())

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
