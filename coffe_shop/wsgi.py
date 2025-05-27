import os
import sys
from dotenv import load_dotenv  # ⬅️ AGREGADO

# Añade el path de tu proyecto al PYTHONPATH
project_home = '/home/franzAlcoba/CoffeShop'  # ajusta con tu ruta exacta
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# ⬇️ CARGAMOS EL ARCHIVO .env ANTES DE CUALQUIER OTRA COSA
env_path = os.path.join(project_home, '.env')
load_dotenv(env_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coffe_shop.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
