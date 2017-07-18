# -*- coding: utf-8 -*- 
'''
    【简介】
    PyQT5中关闭窗体例子
 
  
'''

from PyQt5.QtWidgets import QMainWindow,QHBoxLayout, QPushButton ,  QApplication, QWidget  
import sys 

class WinForm(QMainWindow):  
	
	def __init__(self, parent=None):  
		super(WinForm, self).__init__(parent)
		self.resize(330,  100)  
		self.setWindowTitle('关闭主窗口例子') 		
		self.button1 = QPushButton('关闭主窗口')  		
		self.button1.clicked.connect(self.onButtonClick) 
        
		layout = QHBoxLayout()  
		layout.addWidget(self.button1)  
        
		main_frame = QWidget()  
		main_frame.setLayout(layout)    
		self.setCentralWidget(main_frame)  
  
	def onButtonClick(self ):  
        #sender 是发送信号的对象，此处发送信号的对象是button1按钮 
		sender = self.sender()         
		print( sender.text() + ' 被按下了' )  
		qApp = QApplication.instance()
		qApp.quit()
		
if __name__ == "__main__":  
	app = QApplication(sys.argv)  
	form = WinForm()  
	form.show()  
	sys.exit(app.exec_())
