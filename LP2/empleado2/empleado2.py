import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap

class Empleado2(QWidget):
    def __init__(self, nombre: str, foto: str, carrera: str):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.lb_nombre = QLabel()
        layout.addWidget(self.lb_nombre)

        img = QPixmap(foto).scaled(150, 150)
        lb_foto = QLabel()
        lb_foto.setPixmap(img)
        layout.addWidget(lb_foto)

        lb_carrera = QLabel(carrera)
        layout.addWidget(lb_carrera)

        self.nombre = nombre

    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre) -> None:
        if not isinstance(nombre, str):
            raise TypeError("Debe ser un texto")
        self.__nombre = nombre
        self.lb_nombre.setText(nombre)
