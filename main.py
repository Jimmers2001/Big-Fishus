from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()

    def button_clicked(self):
        sys.exit()

    def initUI(self):
        self.setGeometry(0, 0, 1200, 600)
        self.setWindowTitle("Big Fishus")

        self.b1 = QPushButton(self)
        self.b1.move(550,400)
        self.b1.setText("Quit")
        self.b1.clicked.connect(self.button_clicked)

        self.label = QLabel(self)
        self.label.setText("Wet")
        self.label.move(50,50)

        

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()