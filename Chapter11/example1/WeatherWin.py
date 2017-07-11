# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WeatherWin.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 347)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 431, 251))
        self.groupBox.setObjectName("groupBox")
        self.weatherComboBox = QtWidgets.QComboBox(self.groupBox)
        self.weatherComboBox.setGeometry(QtCore.QRect(80, 30, 221, 21))
        self.weatherComboBox.setObjectName("weatherComboBox")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.resultText = QtWidgets.QTextEdit(self.groupBox)
        self.resultText.setGeometry(QtCore.QRect(10, 60, 411, 181))
        self.resultText.setObjectName("resultText")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 72, 21))
        self.label.setObjectName("label")
        self.queryBtn = QtWidgets.QPushButton(Form)
        self.queryBtn.setGeometry(QtCore.QRect(90, 300, 93, 28))
        self.queryBtn.setObjectName("queryBtn")
        self.clearBtn = QtWidgets.QPushButton(Form)
        self.clearBtn.setGeometry(QtCore.QRect(230, 300, 93, 28))
        self.clearBtn.setObjectName("clearBtn")

        self.retranslateUi(Form)
        self.clearBtn.clicked.connect(Form.clearResult)
        self.queryBtn.clicked.connect(Form.queryWeather)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "查询城市天气"))
        self.weatherComboBox.setItemText(0, _translate("Form", "北京"))
        self.weatherComboBox.setItemText(1, _translate("Form", "天津"))
        self.weatherComboBox.setItemText(2, _translate("Form", "上海"))
        self.label.setText(_translate("Form", "城市"))
        self.queryBtn.setText(_translate("Form", "查询"))
        self.clearBtn.setText(_translate("Form", "清空"))

