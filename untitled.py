# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menu)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionermam = QtWidgets.QAction(MainWindow)
        self.actionermam.setObjectName("actionermam")
        self.actionni = QtWidgets.QAction(MainWindow)
        self.actionni.setObjectName("actionni")
        self.menu_2.addAction(self.actionni)
        self.menu.addAction(self.menu_2.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.actionermam)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.menubar.triggered['QAction*'].connect(MainWindow.close)
        self.menubar.triggered['QAction*'].connect(MainWindow.hide)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.menu_2.setTitle(_translate("MainWindow", "耳机"))
        self.actionermam.setText(_translate("MainWindow", "ermam "))
        self.actionni.setText(_translate("MainWindow", "ni"))

