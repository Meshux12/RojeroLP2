import sys
from PyQt6.QtWidgets import QWidget, QPushButton, QApplication, QGridLayout, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

#yo lo hice un poco diferente ya que queria practicar un poco con el acomodo de los botones y le quise poner una imagen solom para 
#jugar un poco con el codigo y el diseño.
class Calculadora(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora")

        self.lbl = QLabel("0")
        self.lbl.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.lbl.setStyleSheet("font-size: 24px; border: 1px solid green; padding: 5px;") #el detallado me sirve para ver de que manera quiero 
        #que salga el cudaro de texto de la calculador. en este caso lo puse de color verde.

        layout = QGridLayout()
        layout.addWidget(self.lbl, 0, 0, 1, 4) 

        botones = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ('C', 4, 2), ("+", 4, 3), ("=", 4, 4)
        ]

        for texto, fila, col in botones:
            boton = QPushButton(texto)
            boton.setFixedSize(50, 40)
            layout.addWidget(boton, fila, col)

            if texto == "=":
                boton.clicked.connect(self.resultado)
            elif texto == 'C':
                boton.clicked.connect(self.limpiar)
            else:
                boton.clicked.connect(self.evento)

        imagen_label = QLabel()
        pixmap = QPixmap("gatoNi.jpeg")  
        imagen_label.setPixmap(pixmap)
        imagen_label.setScaledContents(True)
        imagen_label.setFixedSize(150, 150)  

        layout.addWidget(imagen_label, 1, 4, 3, 1, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)
        self.show()

    def limpiar(self):
        self.lbl.setText("0")

    def evento(self):
        obj = self.sender()
        texto = obj.text()

        if self.lbl.text() == "0":
            self.lbl.setText(texto)
        else:
            self.lbl.setText(self.lbl.text() + texto)

    def resultado(self):
        try:
            res = eval(self.lbl.text())
            self.lbl.setText(str(res))
        except Exception:  
            self.lbl.setText("Error")

# Main
app = QApplication(sys.argv)
ex = Calculadora()
sys.exit(app.exec())
