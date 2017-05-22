# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MatrixWinUi.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MatrixWin(object):
    def setupUi(self, MatrixWin):
        MatrixWin.setObjectName("MatrixWin")
        MatrixWin.resize(801, 418)
        self.tequilaScrollBar = QtWidgets.QScrollBar(MatrixWin)
        self.tequilaScrollBar.setEnabled(True)
        self.tequilaScrollBar.setGeometry(QtCore.QRect(210, 30, 361, 21))
        self.tequilaScrollBar.setMaximum(11)
        self.tequilaScrollBar.setProperty("value", 8)
        self.tequilaScrollBar.setSliderPosition(8)
        self.tequilaScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.tequilaScrollBar.setObjectName("tequilaScrollBar")
        self.label = QtWidgets.QLabel(MatrixWin)
        self.label.setGeometry(QtCore.QRect(20, 30, 151, 21))
        self.label.setObjectName("label")
        self.buttonBox = QtWidgets.QDialogButtonBox(MatrixWin)
        self.buttonBox.setGeometry(QtCore.QRect(20, 350, 250, 28))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_2 = QtWidgets.QLabel(MatrixWin)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 151, 21))
        self.label_2.setObjectName("label_2")
        self.tripleSecSpinBox = QtWidgets.QSpinBox(MatrixWin)
        self.tripleSecSpinBox.setGeometry(QtCore.QRect(210, 60, 250, 21))
        self.tripleSecSpinBox.setMaximum(11)
        self.tripleSecSpinBox.setProperty("value", 4)
        self.tripleSecSpinBox.setObjectName("tripleSecSpinBox")
        self.label_3 = QtWidgets.QLabel(MatrixWin)
        self.label_3.setGeometry(QtCore.QRect(490, 60, 151, 21))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(MatrixWin)
        QtCore.QMetaObject.connectSlotsByName(MatrixWin)

    def retranslateUi(self, MatrixWin):
        _translate = QtCore.QCoreApplication.translate
        MatrixWin.setWindowTitle(_translate("MatrixWin", "Form"))
        self.tequilaScrollBar.setToolTip(_translate("MatrixWin", "Jiggers of tequila"))
        self.label.setText(_translate("MatrixWin", "龙舌兰酒"))
        self.buttonBox.setToolTip(_translate("MatrixWin", "Press OK to make the drinks"))
        self.label_2.setText(_translate("MatrixWin", "三重蒸馏酒"))
        self.tripleSecSpinBox.setToolTip(_translate("MatrixWin", "Jiggers of triple sec"))
        self.label_3.setText(_translate("MatrixWin", "毫升"))

