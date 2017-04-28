# -*- coding: utf-8 -*-
 
"""
    【简介】
    打印图像例子
    
    
"""
 
from PyQt5.QtGui import QImage , QIcon, QPixmap
from PyQt5.QtWidgets import QApplication  , QMainWindow, QLabel,  QSizePolicy , QAction
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
import sys  
      
class MainWindow(QMainWindow):  
	def __init__(self,parent=None):  
		super(MainWindow,self).__init__(parent)  
		self.setWindowTitle(self.tr("打印图片"))  
		self.imageLabel=QLabel()  
		self.imageLabel.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)  
		self.setCentralWidget(self.imageLabel)  

		self.image=QImage()  
		  
		self.createActions()  
		self.createMenus()  
		self.createToolBars()  

		if self.image.load("./images/screen.png"):  
			self.imageLabel.setPixmap(QPixmap.fromImage(self.image))  
			self.resize(self.image.width(),self.image.height())  
									
	def createActions(self):  
		self.PrintAction=QAction(QIcon("./images/printer.png"),self.tr("打印"),self)  
		self.PrintAction.setShortcut("Ctrl+P")  
		self.PrintAction.setStatusTip(self.tr("打印"))  
		self.PrintAction.triggered.connect(self.slotPrint) 

	def createMenus(self):  
		PrintMenu=self.menuBar().addMenu(self.tr("打印"))  
		PrintMenu.addAction(self.PrintAction)  

	def createToolBars(self):  
		fileToolBar=self.addToolBar("Print")  
		fileToolBar.addAction(self.PrintAction)  

	def slotPrint(self):  
		printer=QPrinter()  
		printDialog=QPrintDialog(printer,self)  
		if printDialog.exec_():  
			painter=QPainter(printer)  
			rect=painter.viewport()  
			size=self.image.size()  
			size.scale(rect.size(),Qt.KeepAspectRatio)  
			painter.setViewport(rect.x(),rect.y(),size.width(),size.height())  
			painter.setWindow(self.image.rect())  
			painter.drawImage(0,0,self.image)  

if __name__ == "__main__":                    
	app=QApplication(sys.argv)  
	main=MainWindow()  
	main.show()  
	sys.exit(app.exec_()) 
