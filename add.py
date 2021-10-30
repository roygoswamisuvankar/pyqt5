from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QPlainTextEdit, QTextEdit
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("addition.ui",self)

        #define widgets
        self.a = self.findChild(QTextEdit, "input1")
        self.b = self.findChild(QTextEdit,"input2")
        self.label = self.findChild(QLabel,"Ans")
        self.button = self.findChild(QPushButton, "add")

        #connect with functions
        self.button.clicked.connect(self.myfunction)

        self.show()

    def myfunction(self):
        a = self.a.toPlainText()
        b = self.b.toPlainText()
        sum = int(a)+int(b)
        self.label.setText(str(sum))


#initialization main app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
