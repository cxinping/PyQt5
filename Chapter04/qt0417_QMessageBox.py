# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QMessage 例子
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
	app = QApplication(sys.argv)
	w = QWidget()
	b= QPushButton(w)
	b.setText("Show message!")
	b.move(50,50)
	b.clicked.connect(showdialog)
	w.setWindowTitle("PyQt Dialog 例子") 
	w.show()
	sys.exit(app.exec_())
	
def showdialog():
	msg=QMessageBox()
	msg.setIcon(QMessageBox.Information)
	msg.setText("This is a message box")
	msg.setInformativeText("This is additional information")
	msg.setWindowTitle("MessageBox demo")
	msg.setDetailedText("The details are as follows:")
	msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
	msg.buttonClicked.connect(msgbtn)
	retval=msg.exec_()
	print("value of pressed message box button:", retval )
	
def msgbtn(i):
	print( "Button pressed is:",i.text() )
	
if __name__ == '__main__':
	window()
