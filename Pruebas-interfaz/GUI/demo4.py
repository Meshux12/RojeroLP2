import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QLabel
from PyQt6.QtGui import QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Qt Signals & Slots')

        b1 = QPushButton("Ok")
        b2 = QPushButton("Cancel")
        l1 = QLabel("Hola Mundo")
        l2 = QLabel("Ulsa")
        le = QLineEdit("Hola")

        l3 = QLabel()
        img = QPixmap("ofie.png").scaled(400,400)
        l3.setPixmap(img)

        layout = QGridLayout()
        self.setLayout(layout)

        layout.addWidget(b1, 0, 0, 1, 2)
        layout.addWidget(b2, 0, 2)
        layout.addWidget(l1, 1, 0)
        layout.addWidget(l2, 1, 1)
        layout.addWidget(le, 2, 0)
        layout.addWidget(l3, 3, 0)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())