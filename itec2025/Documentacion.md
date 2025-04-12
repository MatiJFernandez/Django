# 📘 Bitácora de desarrollo del proyecto
## 🧱 1. Creación del entorno virtual

```python3 -m venv .venv```
El punto (.) delante del nombre oculta la carpeta .venv en sistemas Linux/macOS.
Esto permite mantener las dependencias separadas del sistema.

## ⚙️ 2. Activación del entorno

```source .venv/bin/activate```  
Esto debe hacerse cada vez que se comienza a trabajar.
En Windows sería .\.venv\Scripts\activate.

## 📦 3. Instalación de Django

```pip install Django```
Instalación dentro del entorno virtual. Se recomienda luego correr:

```pip freeze > requirements.txt```

## 🛠️ 4. Creación del proyecto principal

```django-admin startproject itec2025```
Esto crea la estructura base con:

itec2025/settings.py

itec2025/urls.py

manage.py

## 🗃️ 5. Migraciones iniciales

```python3 manage.py migrate```
Crea las tablas por defecto que trae Django: autenticación, sesiones, permisos, etc.

## 🧪 6. Ejecutar el servidor de desarrollo

```python3 manage.py runserver```
Por defecto corre en http://127.0.0.1:8000/

## 👤 7. Crear superusuario

```python3 manage.py createsuperuser --username admin --email admin@mail.com```
Este usuario podrá acceder al admin de Django.

## 🧩 8. Crear una aplicación

```django-admin startapp products```
Se agrega la app 'products' en INSTALLED_APPS dentro de settings.py.
También se crea su propio archivo urls.py dentro de la app y se incluye en itec2025/urls.py.

## 🧬 9. Crear modelos
Se define un modelo dentro de products/models.py. Luego:

```python3 manage.py makemigrations```
```python3 manage.py migrate```
Esto crea las tablas correspondientes en la base de datos.


