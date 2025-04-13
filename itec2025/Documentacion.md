# 🚀 Proyecto Django - ITEC2025

## 📘 Bitácora de Desarrollo

Documentación del proceso de construcción del proyecto Django, incluyendo comandos utilizados, configuraciones importantes, estructura de carpetas, y consejos útiles para nuevos desarrolladores que trabajen en este repositorio.

---

### 🧱 1. Crear entorno virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```
> 💡 El punto delante del nombre del entorno lo oculta en el explorador de archivos.

---

### 📦 2. Instalar Django y dependencias

```bash
pip install Django
```
Instalación dentro del entorno virtual. Se recomienda luego correr:

```pip freeze > requirements.txt```

---

### 🏗️ 3. Crear el proyecto principal

```bash
django-admin startproject itec2025
```

Esto genera:

```text
itec2025/
├── itec2025/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── manage.py
```

---

### 🗃️ 4. Migraciones iniciales

```bash
python3 manage.py migrate
```
> 🧠 Esto aplica las migraciones por defecto de Django (auth, admin, contenttypes, etc).

---

### 👤 5. Crear superusuario

```bash
python3 manage.py createsuperuser --username admin --email admin@mail.com
```

---

### 🧩 6. Crear aplicaciones

```bash
django-admin startapp products
```

También se creó:

```bash
django-admin startapp home
```

Agregarlas al archivo `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'products',
    'home',
]
```

---

### 🛠️ 7. Crear modelos y migrarlos

Ejemplo de modelo en `products/models.py`:

```python
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
```

Luego:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

---

### 🌐 8. Configurar URLs

Se crea un archivo `urls.py` en cada app. Se conectan en `itec2025/urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('', include('home.urls')),
]
```

---

## ✅ Recomendaciones para terceros

- Activar entorno: `source .venv/bin/activate`
- Instalar dependencias: `pip install -r requirements.txt`
- Correr migraciones: `python3 manage.py migrate`
- Ejecutar servidor: `python3 manage.py runserver`
- Docker: `docker-compose up --build`

---

## 🐳 Dockerización

### 📄 Dockerfile

```Dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
```

### 📄 docker-compose.yml

```yaml
services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
```

> ⚠️ Si ves un error `DisallowedHost`, asegurate de tener esto en `settings.py`:

```python
ALLOWED_HOSTS = ['0.0.0.0', 'localhost']
```

---

## 📁 Estructura del Proyecto

```text
📁 itec2025/
├── db.sqlite3
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── requirements.txt
├── itec2025/  # Proyecto principal
├── home/      # App home
│   ├── templates/
│   │   └── base.html
├── products/  # App products
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   │   ├── products/list.html
│   │   └── products/detail.html
│   ├── services/
│   └── repositories/
```

---

## 💬 Notas adicionales

- Podés acceder al panel admin desde `/admin/` una vez logueado como superusuario.
- El proyecto está estructurado por responsabilidad (services, repositories, views).
- Se recomienda mantener los comentarios en los archivos explicando la función de cada clase o método.

---

¿Preguntas? Contactar a Matías. 😄

