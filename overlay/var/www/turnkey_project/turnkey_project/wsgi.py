"""
WSGI config for turnkey_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/..')
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/../turnkey_project')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "turnkey_project.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
