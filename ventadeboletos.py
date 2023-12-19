import sys
from PyQt6.QtWidgets import QGridLayout, QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QComboBox, QLineEdit, QTextEdit

from Salacine import Asientos

class Venta_de_Boletos:
    def __init__(self):
        self.asientos = [Asientos(5, 5) for _ in range(3)]  
    def vender_boletos(self, sala, horario, cantidad_asientos, asientos):
        Dinero_recaudado = cantidad_asientos * 3000

        if self.verify_seats_available(sala, horario, asientos):
            self.update_seats_status(sala, horario, asientos)
            return f'Resumen de la compra:\n\n' \
                   f'Sala: {sala + 1}\n' \
                   f'Horario: {["Matine", "Vermut", "Vespertino"][horario]}\n' \
                   f'Cantidad de asientos: {cantidad_asientos}\n' \
                   f'Asientos: {", ".join(map(str, asientos))}\n' \
                   f'Total: ${Dinero_recaudado}'
        else:
            return print("Error: Alguno de los asientos solicitados no está disponible.")

    def verificar_asientos_disponibles(self, sala, horario, asientos):
        for asiento in asientos:
            fila, columna = divmod(asiento - 1, 5)
            if not self.seat_matrices[sala].is_seat_available(fila, columna):
                return False
        return True

    def disponibilidad_asientos(self, sala, horario, asientos):
        for asiento in asientos:
            fila, columna = divmod(asiento - 1, 5)
            self.seat_matrices[sala].reserve_seat(fila, columna)

            