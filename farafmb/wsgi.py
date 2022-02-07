import os

from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farafmb.settings.production')

application = get_wsgi_application()
