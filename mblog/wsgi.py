"""
WSGI config for mblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os

PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))#3
import sys # 4
sys.path.insert(0,PROJECT_DIR) # 5

os.environ["DJANGO_SETTINGS_MODULE"] = "mblog.settings"
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mblog.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
