# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pandas_pyqt.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 60, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 170, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pandastablewidget = DataTableWidget(self.centralWidget)
        self.pandastablewidget.setGeometry(QtCore.QRect(10, 30, 591, 331))
        self.pandastablewidget.setStyleSheet("")
        self.pandastablewidget.setObjectName("pandastablewidget")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "数据初始化"))
        self.pushButton_2.setText(_translate("MainWindow", "保存数据"))

from qtpandas.views.DataTableView import DataTableWidget
