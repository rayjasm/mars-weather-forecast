"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append('/home/ec2-user/Django/mars-weather-forecast')
sys.path.append('/home/ec2-user/Django/mars-weather-forecast/env/lib/python3.11/site-packages')

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "app.settings"

application = get_wsgi_application()