from .base import *

DEBUG = True

ALLOWED_HOSTS = []

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}