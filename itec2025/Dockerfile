# Usar una imagen base de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de requerimientos
COPY requirements.txt /app/

# Instalar las dependencias
# filepath: /home/matias/Documentos/3ro-DSW/ingenieriaSoftware/django_primera_parte/Dockerfile
# ...existing code...
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código del proyecto
COPY . /app/

# Exponer el puerto que usará Django
EXPOSE 8000

# Comando para ejecutar el servidor de desarrollo de Django
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000", "--reload"]