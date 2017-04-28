# -*- coding: utf-8 -*-
 
"""
    【简介】
    打印图像例子
    
    
"""
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage , QIcon, QPixmap
from PyQt5.QtWidgets import QApplication  , QMainWindow, QLabel,  QSizePolicy , QAction
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
import sys  
      
class MainWindow(QMainWindow):  
	def __init__(self,parent=None):  
		super(MainWindow,self).__init__(parent)  
		self.setWindowTitle(self.tr("打印图片"))  
       # 创建一个放置图像的QLabel对象imageLabel，并将该QLabel对象设置为中心窗体。 
		self.imageLabel=QLabel()  
		self.imageLabel.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)  
		self.setCentralWidget(self.imageLabel)  

		self.image=QImage()  
		  
       # 创建菜单，工具条等部件 
		self.createActions()  
		self.createMenus()  
		self.createToolBars()  

       # 在imageLabel对象中放置图像
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
       # 新建一个QPrinter对象 
		printer=QPrinter()  
       # 创建一个QPrintDialog对象，参数为QPrinter对象 
		printDialog=QPrintDialog(printer,self)  

		'''
       判断打印对话框显示后用户是否单击“打印”按钮，若单击“打印”按钮，
       则相关打印属性可以通过创建QPrintDialog对象时使用的QPrinter对象获得，
       若用户单击“取消”按钮，则不执行后续的打印操作。 
		''' 		
		if printDialog.exec_():  
           # 创建一个QPainter对象，并指定绘图设备为一个QPrinter对象。
			painter=QPainter(printer)  
			# 获得QPainter对象的视口矩形
			rect=painter.viewport()  
			# 获得图像的大小
			size=self.image.size()  
			# 按照图形的比例大小重新设置视口矩形
			size.scale(rect.size(),Qt.KeepAspectRatio)  
			painter.setViewport(rect.x(),rect.y(),size.width(),size.height())  
			# 设置QPainter窗口大小为图像的大小
			painter.setWindow(self.image.rect()) 
			# 打印			
			painter.drawImage(0,0,self.image)  

if __name__ == "__main__":                    
	app=QApplication(sys.argv)  
	main=MainWindow()  
	main.show()  
	sys.exit(app.exec_()) 
