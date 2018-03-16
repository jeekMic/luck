# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lucky.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(996, 580)
        font = QtGui.QFont()
        font.setPointSize(12)
        Form.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(829, 10, 131, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.roll = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.roll.setObjectName("roll")
        self.verticalLayout.addWidget(self.roll)
        self.stop = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.stop.setObjectName("stop")
        self.verticalLayout.addWidget(self.stop)
        self.add = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add.setObjectName("add")
        self.verticalLayout.addWidget(self.add)
        self.setting = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.setting.setObjectName("setting")
        self.verticalLayout.addWidget(self.setting)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.introdution = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.introdution.setObjectName("introdution")
        self.verticalLayout.addWidget(self.introdution)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(130, 40, 581, 321))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.show_name = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(92)
        self.show_name.setFont(font)
        self.show_name.setAutoFillBackground(True)
        self.show_name.setAlignment(QtCore.Qt.AlignCenter)
        self.show_name.setObjectName("show_name")
        self.verticalLayout_2.addWidget(self.show_name)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 380, 771, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAutoFillBackground(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.roll.setText(_translate("Form", "滚动"))
        self.stop.setText(_translate("Form", "停止"))
        self.add.setText(_translate("Form", "添加信息"))
        self.setting.setText(_translate("Form", "设置"))
        self.pushButton_3.setText(_translate("Form", "PushButton"))
        self.introdution.setText(_translate("Form", "说明介绍"))
        self.show_name.setText(_translate("Form", "姓名"))
        self.label_2.setText(_translate("Form", "测试demo"))

