# Usa una imagen oficial de Python
FROM python:3.11

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requerimientos y lo instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código del proyecto al contenedor
COPY . .

# Define la variable GOOGLE_ENTRYPOINT
ENV GOOGLE_ENTRYPOINT "gunicorn orion.wsgi:application --bind 0.0.0.0:8080"

# Expone el puerto en el que correrá Django
EXPOSE 8080

# Ejecuta migraciones y luego inicia el servidor
CMD ["gunicorn", "orion_backend.wsgi:application", "--bind", "0.0.0.0:8080"]
