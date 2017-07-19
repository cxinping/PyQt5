# -*- coding: utf-8 -*-

"""
    【简介】
    自定义信号和内置槽示例


"""

from PyQt5.QtWidgets import  QApplication ,QWidget, QPushButton
from PyQt5.QtCore import pyqtSignal
import sys

class WinForm(QWidget):
	button_clicked_signal = pyqtSignal() # 自定义信号，不带参

	def __init__(self, parent = None):
		super(WinForm,self).__init__(parent)
		self.resize(330,  50 ) 
		self.setWindowTitle('自定义信号和内置槽示例')

		btn = QPushButton('关闭', self)
		# 连接信号/槽
		btn.clicked.connect(self.btn_clicked) 
		# 接收信号，连接到槽
		self.button_clicked_signal.connect(self.close) 
		
	def btn_clicked(self):
		# 发送无参数的自定义信号
		self.button_clicked_signal.emit() 
                
if __name__ == '__main__':  
	app = QApplication(sys.argv)
	win = WinForm()
	win.show()
	sys.exit(app.exec_())
