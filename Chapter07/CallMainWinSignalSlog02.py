# -*- coding: utf-8 -*-

import sys 	
from PyQt5.QtWidgets import QApplication , QMainWindow
from MainWinSignalSlog02 import Ui_Form
from PyQt5.QtCore import pyqtSignal , Qt 

class MyMainWindow(QMainWindow, Ui_Form):
	helpSignal = pyqtSignal(str)
	printSignal = pyqtSignal(list)
	# 声明一个多重载版本的信号，包括了一个带int和str类型参数的信号，以及带str参数的信号
	previewSignal = pyqtSignal([int,str],[str])
	
	def __init__(self, parent=None):    
		super(MyMainWindow, self).__init__(parent)
		self.setupUi(self)
		self.initUI()
		
	def initUI(self):  	
		self.helpSignal.connect(self.showHelpMessage)
		self.printSignal.connect(self.printPaper)
		self.previewSignal[str].connect(self.previewPaper)
		self.previewSignal[int,str].connect(self.previewPaperWithArgs)  
		
		self.printButton.clicked.connect(self.emitPrintSignal)
		self.previewButton.clicked.connect(self.emitPreviewSignal)

	# 发射预览信号
	def emitPreviewSignal(self):
		if self.previewStatus.isChecked() == True:
			self.previewSignal[int,str].emit(1080," Full Screen")
		elif self.previewStatus.isChecked() == False:
			self.previewSignal[str].emit("Preview")

	# 发射打印信号
	def emitPrintSignal(self):
		pList = []
		pList.append(self.numberSpinBox.value() )
		pList.append(self.styleCombo.currentText())
		self.printSignal.emit(pList)
		
	def printPaper(self,list):
		self.resultLabel.setText("打印: "+"份数："+ str(list[0]) +" 纸张："+str(list[1]))

	def previewPaperWithArgs(self,style,text):
		self.resultLabel.setText(str(style)+text)		

	def previewPaper(self,text):
		self.resultLabel.setText(text)  
		
    # 重载点击键盘事件    
	def keyPressEvent(self, event):
		if event.key() == Qt.Key_F1:
			self.helpSignal.emit("help message")

    # 显示帮助消息
	def showHelpMessage(self,message):
		self.resultLabel.setText(message)
		self.statusBar().showMessage(message)
	     		
if __name__=="__main__":  
	app = QApplication(sys.argv)  
	win = MyMainWindow()  
	win.show()  
	sys.exit(app.exec_())  
