import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coin.settings.local')
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
application = get_asgi_application()

