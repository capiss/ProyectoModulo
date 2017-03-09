#!/usr/bin/python

#Se importan los modulos para ssh y scp
import paramiko
from scp import SCPClient
import time
from pprint import pprint

class conexionssh():
  # datos={'host':'','username':'','password':'','port':''}
  datos={}
  def __init__(self):
    datos={}
    env=open(".env","r")
    linea=env.readline()[:-1]
    while linea!='':
      tmp=linea.split("=")
      datos[str(tmp[0])]=str(tmp[1])
      self.datos=datos
      linea=env.readline()[:-1]
    env.close()
  def datosf(self):
    print str(self.datos)
  def copiar(self):  
    fecha=time.strftime("%Y-%m-%d")
    try:
      key = paramiko.RSAKey.from_private_key_file(str(self.datos['keyfile']))
      #Se crea una instancia de cliente SSH
      ssh_client = paramiko.SSHClient()
      #Establece politica por defecto para buscar la llave de host en el equipo
      ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      #Inicia la conexion a la maquina donde se guardan los archivos csv
      ssh_client.connect(
        str(self.datos['host']),
        port=int(self.datos['port']),
        username=str(self.datos['username']),
        password=str(self.datos['password']),
        pkey=key
      )
      stdin, stdout, stderr = ssh_client.exec_command("ls "+self.datos["rutacsv"]+"/*.csv")
      archivo=stdout.readline()[:-1]
      with SCPClient(ssh_client.get_transport()) as scp:
        while archivo!='': 
          if archivo.find(fecha) != -1:
            # archivo=archivo[len(path):]
            print archivo
            scp.get(""+archivo+"")
          archivo=stdout.readline()[:-1]
        #Se cierran las conexiones scp y ssh
        scp.close()
      ssh_client.close()
    except Exception, e:
      # raise e
      pass
    finally:
      pass

conn=conexionssh()
# conn.datosf()
conn.copiar()
