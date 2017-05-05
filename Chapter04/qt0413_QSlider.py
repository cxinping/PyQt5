# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QSlider 例子
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class sliderdemo(QWidget):
	def __init__(self, parent=None):
		super(sliderdemo, self).__init__(parent)
		layout = QVBoxLayout()
		self.l1=QLabel("Hello")
		self.l1.setAlignment(Qt.AlignCenter)
		layout.addWidget(self.l1)
		self.sl=QSlider(Qt.Horizontal)
		self.sl.setMinimum(10)
		self.sl.setMaximum(30)
		self.sl.setValue(20)
		self.sl.setTickPosition(QSlider.TicksBelow)
		self.sl.setTickInterval(5)
		layout.addWidget(self.sl)
		self.sl.valueChanged.connect(self.valuechange)
		self.setLayout(layout)
		self.setWindowTitle("QSlider demo")

	def valuechange(self):
		size=self.sl.value()
		self.l1.setFont(QFont("Arial",size))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = sliderdemo()
	ex.show()
	sys.exit(app.exec_())
