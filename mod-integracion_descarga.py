#!/usr/bin/env python

#Se importan los modulos para ssh y scp
import paramiko
from scp import SCPClient


#Se crea una instancia de cliente SSH
ssh_client = paramiko.SSHClient()
#Establece politica por defecto para buscar la llave de host en el equipo
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#Inicia la conexion a la maquina donde se guardan los archivos csv
ssh_client.connect('10.0.0.10',22,'diana','hola123.,')
#Se pasa la conexion ssh a cliente scp
scp = SCPClient(ssh_client.get_transport())
#Se descarga el archivo(Modificar a csv)
scp.get('archivo.txt')
#Se cierran las conexiones scp y ssh
scp.close()
ssh_client.close()
