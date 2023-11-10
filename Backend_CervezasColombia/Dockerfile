# Utiliza una imagen base de Python
FROM python:3.8-slim-buster

# Define el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de la aplicación al contenedor
COPY . .

# Instala las dependencias de la aplicación, incluyendo flask-cors
RUN pip install --no-cache-dir -r requirements.txt

# Configura las variables de entorno para Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=7024

# Expone el puerto en el que se ejecuta la aplicación
EXPOSE 7024

# Comando para ejecutar la aplicación
CMD ["flask", "run"]
