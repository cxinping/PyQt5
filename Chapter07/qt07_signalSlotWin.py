# -*- coding: utf-8 -*-

"""
    【简介】
    多线程更新跟新数据，pyqt5界面实时刷新例子 


"""

from PyQt5.QtCore import QThread ,  pyqtSignal,  QDateTime 
from PyQt5.QtWidgets import QApplication,  QDialog,  QLineEdit
import time
import sys

class Backend(QThread):
	update_date = pyqtSignal(str)
	
	def run(self):
		while True:
			data = QDateTime.currentDateTime()
			currTime = data.toString("yyyy-MM-dd hh:mm:ss")
			self.update_date.emit( str(currTime) )
			time.sleep(1)

class Window(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		self.setWindowTitle('pyqt5界面实时更新例子')
		self.resize(400, 100)
		self.input = QLineEdit(self)
		self.input.resize(400, 100)

	def handleDisplay(self, data):
		self.input.setText(data)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	backend = Backend()
	win = Window()
	backend.update_date.connect(win.handleDisplay)
	backend.start()
	win.show() 
	sys.exit(app.exec_())
