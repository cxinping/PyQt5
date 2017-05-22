# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'comboselect.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_select(object):
    def setupUi(self, select):
        select.setObjectName("select")
        select.resize(520, 237)
        self.groupBox_pro_city = QtWidgets.QGroupBox(select)
        self.groupBox_pro_city.setGeometry(QtCore.QRect(30, 30, 421, 111))
        self.groupBox_pro_city.setObjectName("groupBox_pro_city")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox_pro_city)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 411, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_province = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_province.setObjectName("label_province")
        self.horizontalLayout.addWidget(self.label_province)
        self.comboBox_province = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_province.setObjectName("comboBox_province")
        self.comboBox_province.addItem("")
        self.comboBox_province.addItem("")
        self.comboBox_province.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_province)
        self.label_city = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_city.setObjectName("label_city")
        self.horizontalLayout.addWidget(self.label_city)
        self.comboBox_city = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_city.setObjectName("comboBox_city")
        self.comboBox_city.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_city)
        self.label_town = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_town.setObjectName("label_town")
        self.horizontalLayout.addWidget(self.label_town)
        self.comboBox_town = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_town.setObjectName("comboBox_town")
        self.comboBox_town.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_town)
        self.pushButton_ok = QtWidgets.QPushButton(select)
        self.pushButton_ok.setGeometry(QtCore.QRect(350, 180, 75, 23))
        self.pushButton_ok.setObjectName("pushButton_ok")

        self.retranslateUi(select)
        QtCore.QMetaObject.connectSlotsByName(select)

    def retranslateUi(self, select):
        _translate = QtCore.QCoreApplication.translate
        select.setWindowTitle(_translate("select", "Form"))
        self.groupBox_pro_city.setTitle(_translate("select", "省市区县联动"))
        self.label_province.setText(_translate("select", "省份："))
        self.comboBox_province.setItemText(0, _translate("select", "请选择"))
        self.comboBox_province.setItemText(1, _translate("select", "陕西"))
        self.comboBox_province.setItemText(2, _translate("select", "河南"))
        self.label_city.setText(_translate("select", "城市："))
        self.comboBox_city.setItemText(0, _translate("select", "请选择"))
        self.label_town.setText(_translate("select", "区县："))
        self.comboBox_town.setItemText(0, _translate("select", "请选择"))
        self.pushButton_ok.setText(_translate("select", "确定"))

