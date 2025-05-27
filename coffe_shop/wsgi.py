import os
import sys

# Añade el path de tu proyecto al PYTHONPATH
project_home = '/home/franzAlcoba/CoffeShop'  # ajusta con tu ruta exacta
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Activa el entorno virtual
# activate_env = '/home/franzAlcoba/CoffeShop/venv/bin/activate_this.py'  # ruta a tu activate_this.py
# with open(activate_env) as f:
#     exec(f.read(), {'__file__': activate_env})
os.environ['DJANGO_ENV'] = 'production'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coffe_shop.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
# This file is used to configure the WSGI application for your Django project.