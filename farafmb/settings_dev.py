from .settings import *

DEBUG = True

ALLOWED_HOSTS = []


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}


# Security

SECURE_HSTS_SECONDS = 0

SECURE_HSTS_PRELOAD = False

SECURE_HSTS_INCLUDE_SUBDOMAINS = False

SECURE_SSL_REDIRECT = False

SECURE_PROXY_SSL_HEADER = None

SESSION_COOKIE_SECURE = False

CSRF_COOKIE_SECURE = False
