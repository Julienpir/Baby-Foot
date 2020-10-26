# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fen_terrain.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Score_rouge = QtWidgets.QLCDNumber(self.centralwidget)
        self.Score_rouge.setGeometry(QtCore.QRect(230, 10, 131, 141))
        self.Score_rouge.setObjectName("Score_rouge")
        self.Score_bleu = QtWidgets.QLCDNumber(self.centralwidget)
        self.Score_bleu.setGeometry(QtCore.QRect(390, 10, 131, 141))
        self.Score_bleu.setObjectName("Score_bleu")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(410, 40, 47, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.conteneur = QtWidgets.QWidget(self.centralwidget)
        self.conteneur.setGeometry(QtCore.QRect(110, 170, 691, 411))
        self.conteneur.setObjectName("conteneur")
        self.label_2 = QtWidgets.QLabel(self.conteneur)
        self.label_2.setGeometry(QtCore.QRect(10, -10, 621, 421))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../IHM/terrain.gif"))
        self.label_2.setObjectName("label_2")
        self.simuler = QtWidgets.QPushButton(self.centralwidget)
        self.simuler.setGeometry(QtCore.QRect(570, 70, 171, 71))
        self.simuler.setObjectName("simuler")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.label.setText(_translate("MainWindow", ":"))
        self.simuler.setText(_translate("MainWindow", "simuler"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

