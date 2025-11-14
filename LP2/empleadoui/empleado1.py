import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class Empleado1(QWidget):
    def __init__(self, nombre:str, foto:str, carrera:str):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        lb_nombre = QLabel(nombre)
        layout.addWidget(lb_nombre)

        img = QPixmap(foto).scaled(150, 150)
        lb_foto = QLabel()
        lb_foto.setPixmap(img)
        layout.addWidget(lb_foto)

        lb_carrera = QLabel(carrera)
        layout.addWidget(lb_carrera)