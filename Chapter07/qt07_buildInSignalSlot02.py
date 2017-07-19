# -*- coding: utf-8 -*-

"""
    【简介】
    自定义信号和内置槽函数 示例


"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
import sys

class Winform(QWidget):
	# 自定义信号，不带参数
	button_clicked_signal = pyqtSignal()

	def __init__(self,parent=None):
		super().__init__(parent)
		self.setWindowTitle('自定义信号和内置槽函数示例')
		self.resize(330,  50 ) 
		btn = QPushButton('关闭', self)
		# 连接 信号和槽
		btn.clicked.connect(self.btn_clicked)
		# 接收信号，连接到槽
		self.button_clicked_signal.connect(self.close) 

	def btn_clicked(self):
		# 发送自定义信号，无参数
		self.button_clicked_signal.emit()
		                    		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = Winform()
	win.show()
	sys.exit(app.exec_())
