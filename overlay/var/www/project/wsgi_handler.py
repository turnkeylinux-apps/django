import os, sys
import django.core.handlers.wsgi

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
application = django.core.handlers.wsgi.WSGIHandler()
