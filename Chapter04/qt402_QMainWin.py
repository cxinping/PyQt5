# -*- coding: utf-8 -*- 

'''
    【简介】
	PyQT5中主窗口例子
  
  
'''

import sys
from PyQt5.QtWidgets import QMainWindow , QApplication
from PyQt5.QtGui import QIcon 

class MainWidget(QMainWindow):
	def __init__(self,parent=None):
		super(MainWidget,self).__init__(parent)
        # 设置主窗体标签
		self.setWindowTitle("QMainWindow 例子")         
		self.resize(400, 200) 
		self.status = self.statusBar()
		self.status.showMessage("这是状态栏提示",5000)


if __name__ == "__main__": 
	app = QApplication(sys.argv)
	app.setWindowIcon(QIcon("./images/cartoon1.ico"))
	main = MainWidget()
	main.show()
	sys.exit(app.exec_())
