# -*- coding: utf-8 -*-
import os
import sys
import platform

# путь к проекту, там где manage.py
sys.path.insert(0, '/home/c/cq45999/iva_site/public_html/iva_site/iva_site')
# путь к фреймворку, там где settings.py
sys.path.insert(0, '/home/c/cq45999/iva_site/public_html/iva_site/iva_site/iva_site')
# путь к виртуальному окружению myenv
sys.path.insert(0, '/home/c/cq45999/iva_site/public_html/myenv/lib/python{0}/site-packages'.format(
    platform.python_version()[0:3]))
# sys.path.insert(0, '/home/c/cq45999/iva_site/public_html/myenv/lib/python3.6/site-packages')
os.environ["DJANGO_SETTINGS_MODULE"] = "iva_site.settings"

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
