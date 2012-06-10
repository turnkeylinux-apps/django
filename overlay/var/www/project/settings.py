import os
import sys

DEBUG = False
TEMPLATE_DEBUG = False

ADMINS = (
    ('Django Admin', 'admin@example.com'),
)

MANAGERS = ADMINS

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(PROJECT_ROOT, "apps"))

DATABASE_ENGINE = 'mysql'
DATABASE_NAME = 'django'
DATABASE_USER = 'django'
DATABASE_PASSWORD = '0fdaad2d20b61cb13ca4652bc6b18923'

EMAIL_HOST = "localhost"
EMAIL_PORT = "25"
DEFAULT_FROM_EMAIL = "noreply@example.com"

TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False

DOC_ROOT = '/usr/share/doc/python-django-doc/html'

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'

SECRET_KEY = 'h__b!q!i6npx%@e@((w5+$_dq9d&v+maogm87edx_@978$=!=g'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.core.context_processors.auth',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
)

if os.environ.get('DEVELOPMENT', None):
    from settings_dev import *

