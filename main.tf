provider "aws" {
  region = "us-east-1"
}

resource "aws_security_group" "el_killer" {
  name        = "el_killer"
  description = "Security group CervezasColombia"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 7024
    to_port     = 7024
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "cervezas_colombia" {
  ami           = "ami-0fc5d935ebf8bc3bc"
  instance_type = "t2.micro"
  key_name      = "llave_privada"  # Reemplaza con el nombre de tu par de claves en AWS (SIN extensión)

  vpc_security_group_ids = [aws_security_group.el_killer.id]

  tags = {
    Name = "CervezasColombia"
  }
}

resource "null_resource" "run_provisioner" {
  depends_on = [aws_instance.cervezas_colombia]

  provisioner "remote-exec" {
    inline = [
      "sudo apt-get update",
      "sleep 45",
      "sudo apt-get install -y git",
      "sleep 20",
      "sudo apt-get install -y docker.io",
      "sleep 45",
      "sudo apt update",
      "sleep 20",
      "sudo apt-get install -y docker-compose",
      "sleep 20",
      "git clone https://github.com/AndresAriasM/DockerContainers-Terraform.git",
      "sleep 25",
      "echo '${aws_instance.cervezas_colombia.public_ip}' > /home/ubuntu/DockerContainers-Terraform/Frontend_CervezasColombia/public_ip.txt",
      "sleep 5",
      "cd DockerContainers-Terraform",
      "cd Frontend_CervezasColombia",
      "sudo echo \"var backendUrl = 'http://$(cat public_ip.txt):7024/api/Resumen';\" | sudo tee -a index.html",
      "nueva_linea=$(tail -n 1 index.html)",
      "sudo sed -i \"/function obtenerDatosDesdeBackend() {/i $nueva_linea\" index.html",
      "sudo echo \"var backendUrl = 'http://$(cat public_ip.txt):7024/api/cervecerias';\" | sudo tee -a cervecerias.html",
      "nueva_linea1=$(tail -n 1 cervecerias.html)",
      "sudo sed -i \"/fetch(backendUrl)/i $nueva_linea1\" cervecerias.html",
      "sudo echo \"var backendUrl = 'http://$(cat public_ip.txt):7024/api/cervezas';\" | sudo tee -a cervezas.html",
      "nueva_linea2=$(tail -n 1 cervezas.html)",
      "sudo sed -i \"/fetch(backendUrl)/i $nueva_linea2\" cervezas.html",
      "sudo echo \"var backendUrl = 'http://$(cat public_ip.txt):7024/api/envasados';\" | sudo tee -a envasados.html",
      "nueva_linea3=$(tail -n 1 envasados.html)",
      "sudo sed -i \"/fetch(backendUrl)/i $nueva_linea3\" envasados.html",
      "sudo echo \"var backendUrl = 'http://$(cat public_ip.txt):7024/api/estilos';\" | sudo tee -a estilos.html",
      "nueva_linea4=$(tail -n 1 estilos.html)",
      "sudo sed -i \"/fetch(backendUrl)/i $nueva_linea4\" estilos.html",
      "sudo echo \"var backendUrl = 'http://$(cat public_ip.txt):7024/api/ubicaciones';\" | sudo tee -a ubicaciones.html",
      "nueva_linea5=$(tail -n 1 ubicaciones.html)",
      "sudo sed -i \"/fetch(backendUrl)/i $nueva_linea5\" ubicaciones.html",
      "sudo echo \"var backendUrl = 'http://$(cat public_ip.txt):7024/api/ingredientes';\" | sudo tee -a ingredientes.html",
      "nueva_linea6=$(tail -n 1 ingredientes.html)",
      "sudo sed -i \"/fetch(backendUrl)/i $nueva_linea6\" ingredientes.html",
      "docker stop $(docker ps -aq)",
      "docker rm $(docker ps -aq)",
      "docker rmi $(docker images -q)",
      "cd /home/ubuntu/DockerContainers-Terraform/Frontend_CervezasColombia",
      "sudo docker build -t frontend_cervezas .",
      "sleep 15",
      "cd /home/ubuntu/DockerContainers-Terraform/Backend_CervezasColombia",
      "sudo docker build -t backend_cervezas .",
      "sleep 20",
      "cd /home/ubuntu/DockerContainers-Terraform",
      "sudo docker-compose up -d",
      "echo 'Este es la url de acceso al programa: http://${aws_instance.cervezas_colombia.public_ip}:7024/api/Resumen'",
    ]

    connection {
      type        = "ssh"
      user        = "ubuntu"
      private_key = file("C:\\Users\\Putin\\Documents\\llave_privada.pem") # Reemplaza con la ruta de su equipo local donde tenga su par de claves en AWS (CON extensión)
      host        = aws_instance.cervezas_colombia.public_ip
    }
  }
}

output "public_ip" {
  value = aws_instance.cervezas_colombia.public_ip
}
