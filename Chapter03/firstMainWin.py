# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstMainWin.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

# 导入模块
from PyQt5 import QtCore, QtGui, QtWidgets

#创建窗口类，继承object
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # 设置窗口名
        MainWindow.setObjectName("MainWindow")
        # 设置窗口大小
        MainWindow.resize(726, 592)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #创建一个按钮，并将按钮加入到窗口Form中
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        # 设置按钮大小与位置
        self.pushButton.setGeometry(QtCore.QRect(490, 110, 93, 28))
        # 设置按钮名
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 726, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        # 关联信号槽
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # 设置窗口标题
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # 设置按钮显示文字
        self.pushButton.setText(_translate("MainWindow", "按钮"))

if __name__=="__main__":
	import sys
	from PyQt5.QtWidgets import QApplication , QMainWindow
	app = QApplication(sys.argv)
	mainWindow = QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(mainWindow)
	mainWindow.show()
	sys.exit(app.exec_())

