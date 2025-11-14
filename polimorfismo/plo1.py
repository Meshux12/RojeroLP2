import sys
from PyQt6.QtWidgets import QWidget, QPushButton, QApplication, QVBoxLayout, QLabel

class Ejemplo(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()

        b1 = QPushButton("Boton 1")
        layout.addWidget(b1)
        b1.clicked.connect(self.evento)

        b2 = QPushButton("Boton 2")
        layout.addWidget(b2)
        b2.clicked.connect(self.evento)

        b3 = QPushButton("Boton 3")
        layout.addWidget(b3)
        b3.clicked.connect(self.evento)

        self.setLayout(layout)
        self.show()

    def evento(self):
        obj = self.sender()   # llama al metodo sender 
        print("hola: ", obj.text())

#Main

app = QApplication(sys.argv)
ex = Ejemplo()
sys.exit(app.exec())

