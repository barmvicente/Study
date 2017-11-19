# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'problemafor.ui'
#
# Created: Sat Nov 18 14:12:51 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setObjectName("b1")
        self.verticalLayout.addWidget(self.b1)
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setObjectName("b2")
        self.verticalLayout.addWidget(self.b2)
        self.b3 = QtWidgets.QPushButton(self.centralwidget)
        self.b3.setObjectName("b3")
        self.verticalLayout.addWidget(self.b3)
        self.b4 = QtWidgets.QPushButton(self.centralwidget)
        self.b4.setObjectName("b4")
        self.verticalLayout.addWidget(self.b4)
        self.b5 = QtWidgets.QPushButton(self.centralwidget)
        self.b5.setObjectName("b5")
        self.verticalLayout.addWidget(self.b5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
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
        self.b1.setText(_translate("MainWindow", "1"))
        self.b2.setText(_translate("MainWindow", "2"))
        self.b3.setText(_translate("MainWindow", "3"))
        self.b4.setText(_translate("MainWindow", "4"))
        self.b5.setText(_translate("MainWindow", "5"))

