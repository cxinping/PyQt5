# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MatrixWinUi.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MatrixWin(object):
    def setupUi(self, MatrixWin):
        MatrixWin.setObjectName("MatrixWin")
        MatrixWin.resize(801, 418)
        self.tequilaScrollBar = QtWidgets.QScrollBar(MatrixWin)
        self.tequilaScrollBar.setEnabled(True)
        self.tequilaScrollBar.setGeometry(QtCore.QRect(270, 30, 361, 21))
        self.tequilaScrollBar.setMaximum(11)
        self.tequilaScrollBar.setProperty("value", 8)
        self.tequilaScrollBar.setSliderPosition(8)
        self.tequilaScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.tequilaScrollBar.setObjectName("tequilaScrollBar")
        self.label = QtWidgets.QLabel(MatrixWin)
        self.label.setGeometry(QtCore.QRect(20, 30, 250, 21))
        self.label.setObjectName("label")

        self.retranslateUi(MatrixWin)
        QtCore.QMetaObject.connectSlotsByName(MatrixWin)

    def retranslateUi(self, MatrixWin):
        _translate = QtCore.QCoreApplication.translate
        MatrixWin.setWindowTitle(_translate("MatrixWin", "Form"))
        self.tequilaScrollBar.setToolTip(_translate("MatrixWin", "Jiggers of tequila"))
        self.label.setText(_translate("MatrixWin", "滚动条"))

