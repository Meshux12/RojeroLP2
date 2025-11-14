import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QGridLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from empleado1 import Empleado1

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('2XKO')

        layout = QGridLayout()
        self.setLayout(layout)

        e1 = Empleado1("Pepe Martinez", "empleadoui/splendid.jpeg", "Ing ITIT")
        e2 = Empleado1("Ahri", "empleadoui/ahri.jpg", "Lic. Admin")

        layout.addWidget(e1, 0, 1)
        layout.addWidget(e2, 0, 2)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())