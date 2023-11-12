# Despliegue de aplicación con contenedores en AWS con Terraform
## Andrés Arias Medina

### La aplicación fue desarrollada para desplegarse en dos contenedores.

## Frontend:
Desarrollado en HTML y Javascript en Visual Studio Code.
La interfaz gráfica se maneja en el puerto 80 del host local.
Cada archivo .html fue configurado para recibir la IP pública de la instancia AWS creada por Terraform, de modo, que se administre correctamente el direccionamiento. Cada archivo mediante scripts solicita a la URL respectiva del backend el contenido de esa API en formato JSON, lo procesa y ubica en la interfaz gráfica.

## Backend:
Desarrollado con Python-Flask en Visual Studio Code.
Contiene una base de datos .sqlite cuya información es desplegada mediante una API en formato JSON en un browser.
La aplicación se maneja en el puerto 7024 y está configurada para permitir el tráfico de información usando Flask-Cors.

<img width="960" alt="image" src="https://github.com/AndresAriasM/DockerContainers-Terraform/assets/77759820/f1e7375c-8a4c-4076-877e-de5b773d6641">

<img width="959" alt="image" src="https://github.com/AndresAriasM/DockerContainers-Terraform/assets/77759820/158a7b5e-ed74-41be-8f67-e8626075f26a">

## Instrucciones para el despliegue con Terraform
El proyecto contiene un archivo main.tf donde se indican todas las instrucciones para:
- La creación de la instancia Ubuntu 22.04 - t2.micro en AWS
- Grupo de seguridad (Reglas de entrada: SSH-22, HTTP-80, TCP-7024) - (Reglas de salida: todo el tráfico).
- Instalación de los paquetes necesarios (git, docker.io, docker-compose).
- Clonación del proyecto en la nueva instancia
- Despliegue de la arquitectura de contenedores.
  
Antes de ejecutar el .tf se debe hacer una configuración adicional. Se debe abrir el archivo main.tf en un blog de notas o editor de código. Una vez esté abierto, hay que reemplazar dos campos del archivo con infromación propia.
El primer campo a modificar esta abajo, toca reemplazar la llave de seguridad con alguna propia de su cuenta AWS. Esta es la que le permitirá conectarse a la instancia por SSH.
```
resource "aws_instance" "cervezas_colombia" {
  ami           = "ami-0fc5d935ebf8bc3bc"
  instance_type = "t2.micro"
  key_name      = "llave_privada"  # Reemplaza con el nombre de tu par de claves en AWS

  vpc_security_group_ids = [aws_security_group.el_killer.id]

  tags = {
    Name = "CervezasColombia"
  }
}
```

El segundo campo que hay que tratar también es para el manejo de la llave de seguridad, en este caso hay que poner la ruta local donde usted tenga su llave.
```
connection {
  type        = "ssh"
  user        = "ubuntu"
  private_key = file("C:\\Users\\Putin\\Documents\\llave_privada.pem") # Reemplaza con la ruta de su equipo local donde tenga su par de claves en AWS (CON extensión)
  host        = aws_instance.cervezas_colombia.public_ip
}
```
### Recuerde gestionar sus credenciales de AWS en la carpeta .aws con Command Line Interface - AWS CLI.
### Credentials & Config

Una vez este hecho, deberá abrir una terminal, dirigirse al directorio clonado de este proyecto y ejecutar los siguientes comandos. 
Nota: Debe estar exactamente donde se encuentra el archivo main.tf.
- terraform init
- terraform plan
- terraform apply

El proyecto tarda aproximadamente entre 10-15min en crearse. Una vez haya culminado verá en consola la IP pública de la instancia creada.
Copiela y peguela en el browser de su preferencia y listo!
Ya estará viendo el proyecto desplegado.




