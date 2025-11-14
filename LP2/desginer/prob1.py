import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Yeet')
        uic.loadUi("desginer/pruebaui.ui",self)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())