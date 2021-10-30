from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton, QPlainTextEdit, QLabel, QTextEdit
from PyQt5 import uic
import sys
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("demo.ui",self)
        #define widgets
        self.Button = self.findChild(QPushButton,"pushButton")
        self.myText = self.findChild(QTextEdit,"textEdit")
        self.myLabel = self.findChild(QLabel,"label")
        #coonect with functions
        self.Button.clicked.connect(self.myFunction)
        self.show()
    #function
    def myFunction(self):
        text = self.myText.toPlainText()
        self.myLabel.setText(f'Hello!, {text}')

#initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()

