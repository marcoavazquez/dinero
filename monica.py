# -*- coding: UTF-8 -*-
import sys
from PySide.QtCore import Qt
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtGui import QFileDialog
from proovedores import Proovedor

app = QApplication(sys.argv)

class main(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setMinimumSize(1000,400)
        self.setWindowTitle("Monica")
        self.btn_consultar = QPushButton("  Consultar  ",self)
        self.btn_ingresar = QPushButton("  Ingresar Nuevo  ",self)
        self.btn_mostrar = QPushButton("  Mostrar Todos  ",self)
        self.btn_consultar.move(200,20)
        self.btn_ingresar.move(10,20)
        self.btn_mostrar.move(400,20)

        self.lbl_consultar = QLabel(" Ingrese RFC: ",self)
        self.lbl_consultar.move(10,72)
        self.lne_buscar = QLineEdit(self)
        self.lne_buscar.move(100,70)
        self.btn_buscar = QPushButton(" Buscar ",self)
        self.btn_buscar.move(230,70)
        self.btn_buscar.hide()
        self.lne_buscar.hide()
        self.lbl_consultar.hide()

        self.lbl_rfc = QLabel("RFC: ",self)
        self.lne_rfc = QLineEdit(self)
        self.lbl_rfc.move(10,52)
        self.lne_rfc.move(40,50)
        self.lbl_rfc.hide()
        self.lne_rfc.hide()

        self.lbl_nombre = QLabel("Nombre: ",self)
        self.lne_nombre = QLineEdit(self)
        self.lbl_nombre.move(170,52)
        self.lne_nombre.move(220,50)
        self.lbl_nombre.hide()
        self.lne_nombre.hide()

        self.lbl_email = QLabel("e-mail: ",self)
        self.lne_email = QLineEdit(self)
        self.lbl_email.move(350,52)
        self.lne_email.move(390,50)
        self.lbl_email.hide()
        self.lne_email.hide()

        self.lbl_direccion = QLabel(u"Dirección: ",self)
        self.lne_direccion = QLineEdit(self)
        self.lne_direccion.setMinimumSize(150,40)
        self.lbl_direccion.move(530,52)
        self.lne_direccion.move(590,50)
        self.lbl_direccion.hide()
        self.lne_direccion.hide()

        self.lbl_telefono = QLabel("Tel: ",self)
        self.lne_telefono = QLineEdit(self)
        self.lbl_telefono.move(750,52)
        self.lne_telefono.move(770,50)
        self.lbl_telefono.hide()
        self.lne_telefono.hide()

        self.btn_guardar = QPushButton(" Guardar ",self)
        self.btn_guardar.move(900,50)
        self.btn_guardar.setMinimumSize(90,40)
        self.btn_guardar.hide()

        self.btn_ingresar.clicked.connect(self.ingresarD)
        self.btn_guardar.clicked.connect(self.guardar)
        self.btn_consultar.clicked.connect(self.consultar)
        self.btn_buscar.clicked.connect(self.buscar)

        self.datos = [('','','','','')]
        self.tbl_datos = QTableView(self)
        self.tbl_datos.move(10,100)
        self.tbl_datos.setMinimumSize(980,100)
        self.tbl_datos.setMaximumSize(980,500)
        self.tbl_model = MyTableModel(self,self.datos,header)
        self.tbl_datos.setModel(self.tbl_model)
        self.tbl_datos.resizeColumnsToContents()

        #self.layout = QVBoxLayout(self)
        #self.layout.addWidget(self.tbl_datos)
        #self.setLayout(self.layout)

    def ingresarD(self):
        self.lbl_rfc.show()
        self.lne_rfc.show()
        self.lbl_nombre.show()
        self.lne_nombre.show()
        self.lbl_email.show()
        self.lne_email.show()
        self.lbl_direccion.show()
        self.lne_direccion.show()
        self.lbl_telefono.show()
        self.lne_telefono.show()
        self.btn_guardar.show()
        self.btn_buscar.hide()
        self.lne_buscar.hide()
        self.lbl_consultar.hide()

    def guardar(self):
        if self.lne_rfc or self.lne_nombre != "":
            self.lbl_rfc.hide()
            self.lne_rfc.hide()
            self.lbl_nombre.hide()
            self.lne_nombre.hide()
            self.lbl_email.hide()
            self.lne_email.hide()
            self.lbl_direccion.hide()
            self.lne_direccion.hide()
            self.lbl_telefono.hide()
            self.lne_telefono.hide()
            self.btn_guardar.hide()
            p = Proovedor(self.lne_rfc.text())
            p.insertar(self.lne_nombre.text(),self.lne_direccion.text(),self.lne_telefono.text(),self.lne_email.text())
            self.buscar(self.lne_rfc)
            self.lne_rfc.setText("")
            self.lne_nombre.setText("")
            self.lne_direccion.setText("")
            self.lne_telefono.setText("")
            self.lne_email.setText("")

        else:
            QMessageBox.text(u"No puede haber campos vacíos")

    def consultar(self):
        self.lbl_rfc.hide()
        self.lne_rfc.hide()
        self.lbl_nombre.hide()
        self.lne_nombre.hide()
        self.lbl_email.hide()
        self.lne_email.hide()
        self.lbl_direccion.hide()
        self.lne_direccion.hide()
        self.lbl_telefono.hide()
        self.lne_telefono.hide()
        self.btn_guardar.hide()
        self.btn_buscar.show()
        self.lne_buscar.show()
        self.lbl_consultar.show()

    def buscar(self):
        p = Proovedor(self.lne_rfc.text())
        self.datos = p.consultar_p()
        print self.datos

    def run(self):
        self.show()
        app.exec_()

class MyTableModel(QAbstractTableModel):
    def __init__(self,parent,datos,header,*args):
        QAbstractTableModel.__init__(self,parent,*args)
        self.datos = datos
        self.header = header

    def rowCount(self,parent):
        return len(self.datos)

    def columnCount(self,parent):
        return len(self.datos[0])

    def data(self,index,role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.datos[index.row()][index.column()]

    def headerData(self,col,orientation,role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    #def sort(self,col,order):
     #   self.emit(SIGNAL("layoutAboutToBeChanged()"))
      #  self.datos = sorted(self.datos,key=operator.itemgetter(col))
       # if order == Qt.DescendingOrder:
        #    self.datos.reverse()
        #self.emit(SIGNAL("layoutChanged()"))

header = [' RFC ', ' Nombre ', ' e-mail ', u' Dirección ',u' Teléfono ']
# use numbers for numeric data to sort properly


datos = [
('',"","","",""),

]

app_main = main()
app_main.run()