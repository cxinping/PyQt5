# -*- coding: utf-8 -*-

"""
    【简介】信号/槽的装饰器实现方式
   


"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Calc(object):
    
    def setupUi(self, Form):
        self.inputSpinBox1 = QtWidgets.QSpinBox(Form)
        self.inputSpinBox1.setGeometry(QtCore.QRect(1, 26, 46, 25))
        self.inputSpinBox1.setObjectName("inputSpinBox1") # 必须
        
        self.inputSpinBox2 = QtWidgets.QSpinBox(Form)
        self.inputSpinBox2.setGeometry(QtCore.QRect(70, 26, 46, 25))
        self.inputSpinBox2.setObjectName("inputSpinBox2") # 必须
        
        self.outputWidget = QtWidgets.QLabel(Form)
        self.outputWidget.setGeometry(QtCore.QRect(140, 24, 36, 27))
        self.outputWidget.setObjectName("outputWidget") # 必须
        
        QtCore.QMetaObject.connectSlotsByName(Form) # 必须