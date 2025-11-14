import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QGridLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from empleado2 import Empleado2

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('2XKO')

        layout = QGridLayout()
        self.setLayout(layout)

        self.e1 = Empleado2("Pepe Martinez", "empleadoui/splendid.jpeg", "Ing ITIT")
        e2 = Empleado2("Ahri", "empleadoui/ahri.jpg", "Lic. Admin")

        layout.addWidget(self.e1, 0, 1)
        layout.addWidget(e2, 0, 2)

        b1 = QPushButton("Modificar")
        b1.clicked.connect(self.modificar)
        layout.addWidget(b1, 1, 1)

        self.show()

    def modificar(self):
        self.e1.nombre = "Jose"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())