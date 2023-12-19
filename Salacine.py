import sys
from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QWidget, QLabel, QPushButton, QComboBox, QLineEdit, QTextEdit

class Asientos:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.asiento = [[0] * columnas for _ in range(filas)]

    def Asiento_disponible(self, fila, columna):
        return self.asiento[fila][columna] == 0

    def reservar_asiento(self, fila, columna):
        self.asiento[fila][columna] = 1

    def mostrar_matriz(self):
        return '\n'.join([' '.join(['X' if asiento else 'O' for asiento in fila]) for fila in self.asientos])

class SummaryDialog(QDialog):
    def __init__(self, matrices_asientos, resumen_venta=''):
        super().__init__()

        self.matrices_asientos = matrices_asientos
        self.resumen_venta = resumen_venta

        self.iniciar_interfaz()

    def iniciar_interfaz(self):
        layout = QVBoxLayout()

        etiqueta_resumen = QLabel('Resumen de la venta:')
        layout.addWidget(etiqueta_resumen)

        texto_resumen = QTextEdit()
        texto_resumen.setPlainText(self.resumen_venta)
        texto_resumen.setReadOnly(True)
        layout.addWidget(texto_resumen)

        etiqueta_disponibles = QLabel('Resumen de asientos disponibles:')
        layout.addWidget(etiqueta_disponibles)

        for i, matriz_asientos in enumerate(self.matrices_asientos):
            etiqueta_sala = QLabel(f'\nSala {i + 1}:')
            layout.addWidget(etiqueta_sala)

            texto_disponibles = QTextEdit()
            texto_disponibles.setPlainText(matriz_asientos.mostrar_matriz())
            texto_disponibles.setReadOnly(True)
            layout.addWidget(texto_disponibles)

        self.setLayout(layout)
