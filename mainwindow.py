# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from instructions import Ui_Instructions
from bomberman import *

class Ui_MainWindow(object):

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Instructions()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(758, 538)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-80, -140, 831, 781))
        self.label.setStyleSheet("image: url(:/newPrefix/background.png);")
        self.label.setObjectName("label")

        self.Player_VS_IA = QtWidgets.QPushButton(self.centralwidget)
        self.Player_VS_IA.setGeometry(QtCore.QRect(310, 80, 121, 51))
        self.Player_VS_IA.setObjectName("Player_VS_IA")

        self.Player_VS_Player = QtWidgets.QPushButton(self.centralwidget)
        self.Player_VS_Player.setGeometry(QtCore.QRect(310, 170, 121, 51))
        self.Player_VS_Player.setObjectName("Player_VS_Player")

        self.Instructions = QtWidgets.QPushButton(self.centralwidget)
        self.Instructions.setGeometry(QtCore.QRect(310, 260, 121, 51))
        self.Instructions.setObjectName("Instructions")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)

        self.Instructions.clicked.connect(self.openWindow)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 758, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.Player_VS_IA.setText(_translate("MainWindow", "1P VS IA"))
        self.Player_VS_Player.setText(_translate("MainWindow", "1P VS 2P"))
        self.Instructions.setText(_translate("MainWindow", "INSTRUCTIONS"))
import source


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
