#!/usr/bin/python

import MySQLdb

bd = MySQLdb.connect("localhost","ngen","ngen","registros" )
  #("localhost", "usuario", "pass", "nombase")
# Preparamos el cursor que nos va a ayudar a realizar las operaciones con la base de datos
cursor = bd.cursor()
class operaciones():
  def insertar(self):
    # Preparando el query SQL para insertar un registro en la BD
    sql = "INSERT INTO Segmento(id_segmento, segmento, rango, id_dependencia) VALUES (7, '196.234.8.0','196.234.8.1-196.234.8.254', 3)"
    try:
      # Ejecutamos el comando
      cursor.execute(sql)
      # Efectuamos los cambios en la base de datos
      bd.commit()
    except:
      # Si se genero algun error revertamos la operacion
      bd.rollback()
  def select(self):
    # Preparamos el query SQL para obtener todos los empleados de la BD
    sql = "SELECT * FROM Segmento"
    try:
      # Ejecutamos el comando
      cursor.execute(sql)
      # Obtenemos todos los registros en una lista de listas
      resultados = cursor.fetchall()
      for registro in resultados:
        id_segmento = registro[0]
        segmento = registro[1]
        rango = registro[2]
        id_dependencia = registro[3]
        # Imprimimos los resultados obtenidos
        print "id_segmento=%d, segmento=%s, rango=%s, id_dependencia=%d" % (id_segmento, segmento, rango, id_dependencia)
    except:
      print "Error: No se pudo obtener la data"
    
class conexionbd():
 # bd = MySQLdb.connect("localhost","ngen","ngen","registros" )
  # ("localhost", "usuario", "pass", "nombase")
  cursor = bd.cursor()
  segmento = operaciones()
  segmento.select()
# Nos desconectamos de la base de datos
bd.close()

