import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import math


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Suma')

        layout = QGridLayout()
        self.setLayout(layout)

        lab1 = QLabel("Numero 1")
        self.le1 = QLineEdit()
        lab2 = QLabel("Numero 2")
        self.le2 = QLineEdit()
        b1 = QPushButton("Sumar")
        b1.clicked.connect(self.sumar)
        layout.addWidget(lab1, 0, 0)
        layout.addWidget(self.le1, 1, 0)
        layout.addWidget(lab2, 0, 1)
        layout.addWidget(self.le2, 1, 1)
        layout.addWidget(b1, 2, 0, 1, 2)

        img = QPixmap("tonota.png").scaled(150, 150)
        lab3 = QLabel("")
        lab3.setPixmap(img)
        layout.addWidget(lab3, 3, 0, 2, 1)

        self.lab4 = QLabel("Resultado = ")
        layout.addWidget(self.lab4, 3, 1, 2, 1)
        self.lab4.setStyleSheet("font-size: 15px; color: violet; font-weight: bold;")

        self.show()

    def sumar(self):
        num1 = int(self.le1.text())
        num2 = int(self.le2.text())
        suma = num1 + num2
        self.lab4.setText(f"Suma = {suma}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())