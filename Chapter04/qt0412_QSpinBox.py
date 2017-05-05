# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QSpinBox 例子
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class spindemo(QWidget):
	def __init__(self, parent=None):
		super(spindemo, self).__init__(parent)
		layout = QVBoxLayout()
		self.l1=QLabel("current value:")
		self.l1.setAlignment(Qt.AlignCenter)
		layout.addWidget(self.l1)
		self.sp = QSpinBox()
		layout.addWidget(self.sp)
		self.sp.valueChanged.connect(self.valuechange)
		self.setLayout(layout)
		self.setWindowTitle("SpinBox demo")

	def valuechange(self):	
		self.l1.setText("current value:"+str(self.sp.value()))

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = spindemo()
	ex.show()
	sys.exit(app.exec_())
