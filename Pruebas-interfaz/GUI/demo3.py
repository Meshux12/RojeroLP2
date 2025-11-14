import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # set the window title
        self.setWindowTitle('Qt Signals & Slots')

        # create a button widget and connect its clicked signal
        # to a method
        button = QPushButton('Click me')
        button.clicked.connect(self.button_clicked)
        button2 = QPushButton("ULSA")
        button3 = QPushButton("Chihuahua")
        # place the buton on window using a vertical box layout
        layout = QHBoxLayout()
        self.setLayout(layout)

        layout.addWidget(button)
        layout.addWidget(button2)
        layout.addWidget(button3)
        
        # show the window
        self.show()

    def button_clicked(self):
        print('clicked')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create the main window and display it
    window = MainWindow()

    # start the event loop
    sys.exit(app.exec())