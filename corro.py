#!/usr/bin/python

import smtplib 
 
from email.MIMEText import MIMEText
 
emisor = "pbsi11gg@gmail.com"
receptor = "saicorogo@gmail.com"
 
# Configuracion del mensaje
mensaje = MIMEText("Este es el contenido del correo enviado desde Python")
mensaje['From']=emisor
mensaje['To']=receptor
mensaje['Subject']="pruebajoojojo"
 
# Nos conectamos al servidor SMTP de Gmail
serverSMTP = smtplib.SMTP('smtp.gmail.com',587)
serverSMTP.ehlo()
serverSMTP.starttls()
serverSMTP.ehlo()
serverSMTP.login(emisor,"hola123.,")
 
# Enviamos el mensaje
serverSMTP.sendmail(emisor,receptor,mensaje.as_string())
 
# Cerramos la conexion
serverSMTP.close()
