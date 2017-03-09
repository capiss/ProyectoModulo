#!/usr/bin/python
import requests
import urllib, httplib
import itertools
import os

class conSisTickets():
  datos={}
  def __init__(self):
    datos={}
    env=open(".envlogin","r")
    linea=env.readline()[:-1]
    while linea!='':
      tmp=linea.split("=")
      datos[str(tmp[0])]=str(tmp[1])
      self.datos=datos
      linea=env.readline()[:-1]
    env.close()
    print datos

  def datos(self):
    print str(self.datos)

  def login(self):
    conn = httplib.HTTPConnection(self.datos['host'],self.datos['puerto']);
    datos = urllib.urlencode({'email':self.datos['username'], 'pass':self.datos["password"],'lsd':'AVorlP-h','lgndim':'eyJ3IjoxMzY2LCJoIjo3NjgsImF3IjoxMzY2LCJhaCI6NzQxLCJjIjoyNH0='})
    type = {"Content-type":"application/x-www-form-urlencoded", "Accept": "text/plain"}
    print "datos"+str(datos)
    conn.request("POST","/"+self.datos["path"], datos, type)
    respuesta = conn.getresponse()
    code = str(respuesta.read())
    print respuesta.status;
    print str(respuesta.getheader('location'));
    print code
    conn.close()

ticket=conSisTickets()
ticket.login()