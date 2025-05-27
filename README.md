# Coffee Shop

Este es un proyecto Django para la gestión de una cafetería, que incluye módulos para usuarios, productos y órdenes.

## Estructura del proyecto

- `coffe_shop/`: Configuración principal del proyecto Django.
- `orders/`: Aplicación Django para la gestión de órdenes.
- `products/`: (Presumiblemente) gestión de productos.
- `users/`: (Presumiblemente) gestión de usuarios.
- `logos/`: Imágenes y logotipos usados en la aplicación.
- `db.sqlite3`: Base de datos SQLite por defecto.
- `manage.py`: Script de administración de Django.

## Requisitos

- Python 3.12
- Django 5.2
- djangorestframework

Instala las dependencias con:

```sh
pip install -r requirements.txt
```

## Uso

### Migraciones y base de datos

Aplica las migraciones iniciales:

```sh
python manage.py migrate
```

### Crear superusuario

```sh
python manage.py createsuperuser
```

### Ejecutar el servidor de desarrollo

```sh
python manage.py runserver
```

## Estructura de carpetas

- `static/` y `staticfiles/`: Archivos estáticos.
- `templates/`: Plantillas HTML.

## Notas

- El proyecto está en modo DEBUG, no usar en producción sin cambiar la configuración.
- El archivo `.gitignore` excluye archivos sensibles y temporales.

---

Puedes agregar detalles sobre endpoints, modelos y ejemplos de uso según avances en el desarrollo.