#!/usr/bin/python

class obtienecsv:
  titulos=[]
  def leecsv(self,rutacsv):
    csv=open(rutacsv,"r")
    linea1 = csv.readline()[:-1]
    self.titulos = linea1.split(",")
    print self.titulos

