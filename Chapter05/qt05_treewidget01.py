#!/usr/bin/env python3

'''
    【简介】
	PyQT5中 QTreeWidget 例子
   
  
'''

from PyQt5.QtWidgets import *
import sys

class TreeWidgetDemo(QMainWindow):   
	def __init__(self,parent=None):
		super(TreeWidgetDemo,self).__init__(parent)
		self.setWindowTitle('TreeWidget 例子')
		self.tree = QTreeWidget()
		self.tree.setColumnCount(2)
		self.tree.setHeaderLabels(['Key','Value'])
		root= QTreeWidgetItem(self.tree)
		root.setText(0,'root')
		child1 = QTreeWidgetItem(root)
		child1.setText(0,'child1')
		child1.setText(1,'name1')
		child2 = QTreeWidgetItem(root)
		child2.setText(0,'child2')
		child2.setText(1,'name2')
		child3 = QTreeWidgetItem(root)
		child3.setText(0,'child3')
		child4 = QTreeWidgetItem(child3)
		child4.setText(0,'child4')
		child4.setText(1,'name4')

		child5 = QTreeWidgetItem(child3)
		child5.setText(0,'child5')
		child5.setText(1,'name5')
        
		self.tree.addTopLevelItem(root)
		self.tree.clicked.connect( self.onTreeClicked )
		self.setCentralWidget(self.tree)  

	def onTreeClicked(self, qmodelindex):
		item = self.tree.currentItem()
		print("key=%s ,value=%s" % (item.text(0), item.text(1)))
        
if __name__ == '__main__':
	app = QApplication(sys.argv)
	tree = TreeWidgetDemo()
	tree.show()
	sys.exit(app.exec_())
