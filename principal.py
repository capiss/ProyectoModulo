#!/usr/bin/python
import mod_integracion_descarga as mod
import obtiene_datos_csv as csv

conn=mod.conexionssh()
ob=csv.obtienecsv()

conn.copiar()
ob.leecsv(conn.datos['reportecsv'])

