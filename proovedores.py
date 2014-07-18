# -*- coding: utf-8 -*-
import sqlite3

con = sqlite3.connect("basedatos.db")
cur = con.cursor()
print "Se ha creado la conexión correctamente"

class Proovedor:
    def __init__(self,rfc):
        self.rfc = rfc

    def insertar(self,nombre,email,direccion,telefono):
        cur.execute("INSERT INTO PROOVEDORES (RFC,NOMBRE,EMAIL,DIRECCION,TELEFONO) VALUES ('%s','%s','%s','%s','%s')" % (self.rfc,nombre,email,direccion,telefono))
        con.commit()
        return True

    def actualizar(self,nombre,email,direccion,telefono):
        cur.execute("UPDATE PROOVEDORES SET RFC='%s',NOMBRE='%s',EMAIL='%s',DIRECCION='%s',TELEFONO='%s' WHERE RFC = '%s'" % (self.rfc,nombre,email,direccion,telefono,self.rfc))
        con.commit()
        return True

    def eliminar(self):
        cur.execute("DELETE FROM PROOVEDORES WHERE RFC = '%s'" % self.rfc)
        con.commit()
        return True

    def consultar_p(self):
        cur.execute("SELECT RFC,NOMBRE,EMAIL,DIRECCION,TELEFONO FROM PROOVEDORES WHERE RFC = '%s'" % self.rfc)
        return cur

    def mostrarTodos(self):
        cur.execute("SELECT RFC,NOMBRE,EMAIL,DIRECCION,TELEFONO FROM PROOVEDORES ORDER BY ID")
        return cur