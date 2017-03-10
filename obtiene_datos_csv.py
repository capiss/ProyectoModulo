#!/usr/bin/python
import login

class obtienecsv:
  datos=[]
  contenido=[]
  def leecsv(self,rutacsv):
    ticket= login.conSisTickets()
    ticket.login()
    csv=open(rutacsv,"r")
    self.contenido = csv.read().split("\n")
    contador = 0
    
    for reporte in self.contenido:
      if contador == 0 :
        contador+=1
        continue
      if reporte=="":
        continue
      self.datos=reporte.split(",")
      Host_address = self.datos[1]
      Date = self.datos[2]
      feed = self.datos[4]
      Type = self.datos[6]
      datos={
        'hostAddress':Host_address,
        'feed':feed,
        'type':Type,
        'reporter':3,
        'state':'open',
        'date':Date,
        'sendReport':1
      }
      #Magia de enviar un ticket

      ticket.ticket(datos)
      contador+=1
