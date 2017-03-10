#!/usr/bin/python
import requests
import urllib, httplib
import itertools
import os
import ssl
import time

class conSisTickets():
  datos={'Cookie':'','port':'443'}
  session = requests.Session()
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
    # print datos

  def datos(self):
    print str(self.datos)

  def login(self):
    context = ssl._create_unverified_context()
    path="https://"+self.datos['host']+"/user/login"
    k = requests.get(path,verify=False)
    for cookie in k.cookies:
      if cookie.name=='PHPSESSID':
        self.datos['Cookie']=cookie.name+"="+cookie.value
    datos = urllib.urlencode({
      '_username':self.datos['username'],
      '_password':self.datos["password"],
      '_remember_me':'on',
      'login':'Login'
    })
    headers = {
      "Content-type":"application/x-www-form-urlencoded", 
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
      "Cookie": self.datos['Cookie']
    }
    path="https://"+self.datos['host']+self.datos['path']
    
    self.session.post(path,data=datos,headers=headers,verify=False)
    PHPSESSID=""
    REMEMBERME=""
    for cookie in self.session.cookies:
      if cookie.name=='PHPSESSID':
        PHPSESSID=cookie.name+"="+cookie.value
      if cookie.name=='REMEMBERME':
        REMEMBERME=cookie.name+"="+cookie.value
    self.datos['Cookie']=PHPSESSID+"; "+REMEMBERME
    print self.datos['Cookie']
    headers['Cookie']=self.datos['Cookie']
    k = self.session.get("https://"+self.datos['host']+"/incidents/internals",headers=headers,verify=False)
  def ticket(self,parameters):
    datos={
      'hostAddress':parameters['hostAddress'],
      'feed':parameters['feed'],
      'type':parameters['type'],
      'reporter':3,
      'state':'open',
      'date':parameters['date'],
      'sendReport':1
    }
    headers = {
      "Content-type":"application/x-www-form-urlencoded", 
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }
    path="https://"+self.datos['host']+"/api/v2/incidents/internals?apikey=c894e16b95b71eb300d14a4d05205ceeedfc6324"
    req=self.session.post(path,data=datos,headers=headers,verify=False)
    print req.content
    print req.status_code