from PyQt5 import QtCore, QtGui, QtWidgets


class Popup(object):
    def __init__(self, parent):
        self.Dialog = QtWidgets.QDialog(parent)
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(400, 300)
        self.Dialog.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #86A8E7, stop:1 #91EAE4);")
        self.gridLayout = QtWidgets.QGridLayout(self.Dialog)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.Dialog)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setStyleSheet("background: none;\n"
"color: white;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Hello"))

    def show(self):
        self.Dialog.exec()