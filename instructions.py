# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'instructions.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Instructions(object):

    def setupUi(self, Instructions):
        Instructions.setObjectName("Instructions")
        Instructions.resize(1153, 698)
        self.centralwidget = QtWidgets.QWidget(Instructions)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-100, -240, 1291, 1091))
        self.label.setStyleSheet("image: url(:/newPrefix/background.png);")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 40, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Miriam CLM")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 90, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setLineWidth(1)
        self.label_3.setMidLineWidth(0)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 130, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(340, 170, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(340, 230, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(340, 260, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(240, 290, 771, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(300, 320, 421, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")

        self.Back_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Back_Button.setGeometry(QtCore.QRect(20, 20, 71, 31))
        self.Back_Button.setObjectName("Back_Button")
        Instructions.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Instructions)
        self.statusbar.setObjectName("statusbar")
        Instructions.setStatusBar(self.statusbar)

        self.retranslateUi(Instructions)
        QtCore.QMetaObject.connectSlotsByName(Instructions)

    def retranslateUi(self, Instructions):
        _translate = QtCore.QCoreApplication.translate
        Instructions.setWindowTitle(_translate("Instructions", "MainWindow"))
        self.label.setText(_translate("Instructions", "TextLabel"))
        self.label_2.setText(_translate("Instructions", "1P vs IA instructions"))
        self.label_3.setText(_translate("Instructions", "\"Z Q S D\" - se déplacer"))
        self.label_4.setText(_translate("Instructions", "Espace - pose une bombe"))
        self.label_5.setText(_translate("Instructions", "1P vs 2P"))
        self.label_6.setText(_translate("Instructions", "1P : \"Z Q S D\" - se déplacer"))
        self.label_7.setText(_translate("Instructions", "Espace - pose une bombe"))
        self.label_8.setText(_translate("Instructions", "2P : \"flèche haut; flèche droite; flèche gauche; flèche bas\" - se deplacer"))
        self.label_9.setText(_translate("Instructions", "B - pose une bombe"))
        self.Back_Button.setText(_translate("Instructions", "Retour"))
import source_instru


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Instructions = QtWidgets.QMainWindow()
    ui = Ui_Instructions()
    ui.setupUi(Instructions)
    Instructions.show()
    sys.exit(app.exec_())
