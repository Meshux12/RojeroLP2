import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ULSA')

        layout = QGridLayout()
        self.setLayout(layout)

        lab1 = QLabel("ULSA Chihuahua")
        layout.addWidget(lab1, 0, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        lab1.setStyleSheet("font-size: 20px; color: darkgreen; font-weight: bold;")

        lab2 = QLabel("Nombre")
        le1 = QLineEdit("")
        lab3= QLabel("Carrera")
        le2 = QLineEdit("")
        #primero es el renglon y despues la columna
        layout.addWidget(lab2, 1, 0)
        layout.addWidget(le1, 2, 0)
        layout.addWidget(lab3, 3, 0)
        layout.addWidget(le2, 4, 0)
        
        b1 = QPushButton("OK")
        b2 = QPushButton("Cancel")
        layout.addWidget(b1, 5, 0)
        layout.addWidget(b2, 5, 1)

        img = QPixmap("ofie.png").scaled(150, 150)
        lab4 = QLabel("")
        lab4.setPixmap(img)
        layout.addWidget(lab4, 1, 1, 4, 1)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())