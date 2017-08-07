# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWinSignalSlog02.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(715, 225)
        self.controlsGroup = QtWidgets.QGroupBox(Form)
        self.controlsGroup.setGeometry(QtCore.QRect(10, 20, 451, 151))
        self.controlsGroup.setObjectName("controlsGroup")
        self.widget = QtWidgets.QWidget(self.controlsGroup)
        self.widget.setGeometry(QtCore.QRect(10, 40, 411, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.numberSpinBox = QtWidgets.QSpinBox(self.widget)
        self.numberSpinBox.setObjectName("numberSpinBox")
        self.horizontalLayout.addWidget(self.numberSpinBox)
        self.styleCombo = QtWidgets.QComboBox(self.widget)
        self.styleCombo.setObjectName("styleCombo")
        self.styleCombo.addItem("")
        self.styleCombo.addItem("")
        self.styleCombo.addItem("")
        self.horizontalLayout.addWidget(self.styleCombo)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.printButton = QtWidgets.QPushButton(self.widget)
        self.printButton.setObjectName("printButton")
        self.horizontalLayout.addWidget(self.printButton)
        self.widget1 = QtWidgets.QWidget(self.controlsGroup)
        self.widget1.setGeometry(QtCore.QRect(10, 100, 201, 30))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.previewStatus = QtWidgets.QCheckBox(self.widget1)
        self.previewStatus.setObjectName("previewStatus")
        self.horizontalLayout_2.addWidget(self.previewStatus)
        self.previewButton = QtWidgets.QPushButton(self.widget1)
        self.previewButton.setObjectName("previewButton")
        self.horizontalLayout_2.addWidget(self.previewButton)
        self.resultGroup = QtWidgets.QGroupBox(Form)
        self.resultGroup.setGeometry(QtCore.QRect(470, 20, 231, 151))
        self.resultGroup.setObjectName("resultGroup")
        self.resultLabel = QtWidgets.QLabel(self.resultGroup)
        self.resultLabel.setGeometry(QtCore.QRect(20, 30, 191, 101))
        self.resultLabel.setObjectName("resultLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "打印控件"))
        self.controlsGroup.setTitle(_translate("Form", "打印控制"))
        self.label.setText(_translate("Form", "打印份数:"))
        self.styleCombo.setItemText(0, _translate("Form", "A3"))
        self.styleCombo.setItemText(1, _translate("Form", "A4"))
        self.styleCombo.setItemText(2, _translate("Form", "A5"))
        self.label_2.setText(_translate("Form", "纸张类型:"))
        self.printButton.setText(_translate("Form", "打印"))
        self.previewStatus.setText(_translate("Form", "全屏预览"))
        self.previewButton.setText(_translate("Form", "预览"))
        self.resultGroup.setTitle(_translate("Form", "操作结果"))
        self.resultLabel.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))

