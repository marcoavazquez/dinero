# -*- coding: utf-8 -*-
import sqlite3

con = sqlite3.connect("basedatos.db")
cur = con.cursor()
print "Se ha creado la conexión correctamente"

cur.execute("CREATE TABLE PROOVEDORES(ID INTEGER PRIMARY KEY AUTOINCREMENT,RFC CHAR(15) NOT NULL UNIQUE, NOMBRE TEXT NOT NULL, EMAIL CHAR(50), DIRECCION TEXT, TELEFONO CHAR(15));")
print "se ha creado la tabla"