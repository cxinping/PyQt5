# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QFontDialog 例子
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class FontDialogDemo(QWidget):
	def __init__(self, parent=None):
		super(FontDialogDemo, self).__init__(parent)
		layout = QVBoxLayout()
		self.btn=QPushButton("choose font")
		self.btn.clicked.connect(self.getFont)
		layout.addWidget(self.btn)
		self.le=QLabel("Hello,测试字体例子")
		layout.addWidget(self.le)
		self.setLayout(layout)
		self.setWindowTitle("Font Dialog 例子")
		
	def getFont(self):
		font, ok = QFontDialog.getFont()
		if ok:
			self.le.setFont(font)
					
if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = FontDialogDemo()
	demo.show()
	sys.exit(app.exec_())
