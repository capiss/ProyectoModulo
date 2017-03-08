#!/usr/bin/python

#Se importan los modulos para ssh y scp
import paramiko
from scp import SCPClient

class conexionssh():
  datos={'host':'','username':'','password':'','port':''}
  def __init__(self):
    env=open(".env","r")
    linea=env.readline()[:-1]
    while linea!='':
      tmp=linea.split("=")
      if(tmp[0].lower()=='host'):
        self.datos['host']=tmp[1]
      if(tmp[0].lower()=='username'):
        self.datos['username']=tmp[1]
      if(tmp[0].lower()=='password'):
        self.datos['password']=tmp[1]
      if(tmp[0].lower()=='port'):
        self.datos['port']=tmp[1]
      linea=env.readline()[:-1]
    env.close()
  def copiar(self):  
    #Se crea una instancia de cliente SSH
    ssh_client = paramiko.SSHClient()
    #Establece politica por defecto para buscar la llave de host en el equipo
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #Inicia la conexion a la maquina donde se guardan los archivos csv
    ssh_client.connect(self.datos['host'],self.datos['port'],self.datos['username'],self.datos['password'])
    #Se pasa la conexion ssh a cliente scp
    scp = SCPClient(ssh_client.get_transport())
    #Se descarga el archivo(Modificar a csv)
    scp.get('doc.csv')
    #Se cierran las conexiones scp y ssh
    scp.close()
    ssh_client.close()

conn=conexionssh()
print conn.datos
conn.copiar()
