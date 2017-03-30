import sys
from PyQt5.QtWidgets import QMainWindow , QApplication
from PyQt5.QtGui import QIcon 

class MainWidget(QMainWindow):
	def __init__(self,parent=None):
		super(MainWidget,self).__init__(parent)
		self.resize(400, 200) 
		self.status = self.statusBar()
		self.status.showMessage("ÕâÊÇ×´Ì¬À¸",5000)
		self.setWindowTitle("PyQt MainWindowÀý×Ó") 

if __name__ == "__main__": 
	app = QApplication(sys.argv)
	app.setWindowIcon(QIcon("./images/cartoon1.ico"))
	main = MainWidget()
	main.show()
	sys.exit(app.exec_())
