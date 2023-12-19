import sys
from PyQt6 import QtWidgets
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton
from Salacine import Asientos
from ventadeboletos import Venta_de_Boletos

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Cinema PM')
        self.setFixedSize(QSize (640,480))
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        contenedor = QVBoxLayout()

        texto1 = QLabel("Bienvenido al cinema PM")
        self.btn_ventadeboletos = QPushButton("Ir a venta de boletos")
        self.btn_ventadeboletos.setGeometry(60,50,150,50)

        contenedor.addWidget(texto1)
        contenedor.addWidget(self.btn_ventadeboletos)

        escena = QWidget()
        escena.setLayout(contenedor)
        self.setCentralWidget(escena)
        self.show()

if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana =Ventana()
    app.exec()