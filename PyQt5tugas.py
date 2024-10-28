# QtGui QtCore QtWidgets
# from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget,QApplication,QPushButton,QLabel
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# from PyQt5. import Qtwidgets as qtw

class MyWindow(QMainWindow):
    def __ini__(self):
        super().__init__()        
        self.label = QLabel(self)
        self.label.setText("Label1")
        self.label.move(200,0)
        self.button = QPushButton(self)
        self.button.setText("Button1")
        self.setGeometry(0,0,500,500)
        self.setWindowTitle("Belajar PyQt5")

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()
