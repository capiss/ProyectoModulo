#!/usr/bin/python

class obtienecsv:
  def leecsv(self,rutacsv):
    csv=open(rutacsv,"r")
    linea1 = csv.readline()[:-1]
    titulos = linea1.split(",")
    print titulos

ob=obtienecsv()
ob.leecsv("doc.csv")

