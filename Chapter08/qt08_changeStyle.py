# -*- coding: utf-8 -*-

'''
    【简介】
     界面风格例子
    
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore 
from PyQt5.QtGui  import *

class AppWidget( QWidget):
	def __init__(self, parent=None):
		super(AppWidget, self).__init__(parent)
		self.setWindowTitle("界面风格例子")
		horizontalLayout =  QHBoxLayout()
		self.styleLabel =  QLabel("Set Style:")
		self.styleComboBox =  QComboBox()
		# 增加 styles 从 QStyleFactory
		self.styleComboBox.addItems( QStyleFactory.keys())
		# 选择当前界面风格
		index = self.styleComboBox.findText(
					 QApplication.style().objectName(),
					QtCore.Qt.MatchFixedString)
		# 设置当前界面风格
		self.styleComboBox.setCurrentIndex(index)
		# 通过comboBox选择界面分割
		self.styleComboBox.activated[str].connect(self.handleStyleChanged)
		horizontalLayout.addWidget(self.styleLabel)
		horizontalLayout.addWidget(self.styleComboBox)
		self.setLayout(horizontalLayout)

	# 改变界面风格
	def handleStyleChanged(self, style):
		QApplication.setStyle(style)

if __name__ == "__main__":
	app =  QApplication(sys.argv)
	widgetApp = AppWidget()
	widgetApp.show()
	sys.exit(app.exec_())

