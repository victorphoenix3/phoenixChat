import os
import django
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE","phoenixChat.settings")
django.setup()
appllication = get_default_application()