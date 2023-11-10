# Usa una imagen base de nginx
FROM nginx:latest

# Copia los archivos HTML y CSS al directorio de trabajo de Nginx
COPY cervezas.html /usr/share/nginx/html
COPY cervecerias.html /usr/share/nginx/html
COPY ubicaciones.html /usr/share/nginx/html
COPY estilos.html /usr/share/nginx/html
COPY envasados.html /usr/share/nginx/html
COPY ingredientes.html /usr/share/nginx/html
COPY index.html /usr/share/nginx/html
COPY css/ /usr/share/nginx/html/css/
COPY js/ /usr/share/nginx/html/js/
COPY js/script.js /usr/share/nginx/html/js/
COPY css/images/ /usr/share/nginx/html/css/images/

# Reemplaza la URL del backend en los scripts
RUN sed -i "s|http://localhost:7024/api/Resumen|${BACKEND_URL}|" /usr/share/nginx/html/js/script.js

# Expone el puerto 80 para servir la aplicación
EXPOSE 80

# Ejecuta Nginx en primer plano
CMD ["nginx", "-g", "daemon off;"]
