#!/usr/bin/env python3

'''
    【简介】
	PyQT5中 QTreeWidget 例子
   
  
'''

import sys
from PyQt5.QtWidgets import *
#from PyQt5.QtGui import QIcon ,  QBrush , QColor
#from PyQt5.QtCore import Qt 

class TreeWidgetDemo(QWidget):   
	def __init__(self,parent=None):
		super(TreeWidgetDemo,self).__init__(parent)
		self.setWindowTitle('TreeWidget 例子')
        
		operatorLayout = QHBoxLayout()
		addBtn = QPushButton("添加节点")
		updateBtn =  QPushButton("修改节点")
		delBtn = QPushButton("删除节点")		
		operatorLayout.addWidget(addBtn)
		operatorLayout.addWidget(updateBtn)
		operatorLayout.addWidget(delBtn)
		# 按钮的信号槽连接
		addBtn.clicked.connect(self.addTreeNodeBtn )
		updateBtn.clicked.connect(self.updateTreeNodeBtn )
		delBtn.clicked.connect(self.delTreeNodeBtn )		
		
		self.tree = QTreeWidget(self)
        # 设置列数
		self.tree.setColumnCount(2)
        # 设置头的标题
		self.tree.setHeaderLabels(['Key','Value'])
		root= QTreeWidgetItem(self.tree)
		root.setText(0,'root')
		root.setText(1,'0')
		
		child1 = QTreeWidgetItem(root)
		child1.setText(0,'child1')
		child1.setText(1,'1')
		
		child2 = QTreeWidgetItem(root)
		child2.setText(0,'child2')
		child2.setText(1,'2')
		
		child3 = QTreeWidgetItem(root)
		child3.setText(0,'child3')
		child3.setText(1,'3')		
		
		child4 = QTreeWidgetItem(child3)
		child4.setText(0,'child4')
		child4.setText(1,'4')

		child5 = QTreeWidgetItem(child3)
		child5.setText(0,'child5')
		child5.setText(1,'5')
        
		self.tree.addTopLevelItem(root)
		self.tree.clicked.connect( self.onTreeClicked )
        		
		mainLayout = QVBoxLayout(self);
		mainLayout.addLayout(operatorLayout);
		mainLayout.addWidget(self.tree);		
		self.setLayout(mainLayout)		

	def onTreeClicked(self, qmodelindex):
		item = self.tree.currentItem()
		print("key=%s ,value=%s" % (item.text(0), item.text(1)))
		
	def addTreeNodeBtn(self):
		print('--- addTreeNodeBtn ---')
		item = self.tree.currentItem()
		node = QTreeWidgetItem(item)
		node.setText(0,'newNode')
		node.setText(1,'10')	


	def updateTreeNodeBtn(self):
		print('--- updateTreeNodeBtn ---')
		item = self.tree.currentItem()
		item.setText(0,'updateNode')
		item.setText(1,'20')		


	def delTreeNodeBtn(self):
		print('--- delTreeNodeBtn ---')
		item = self.tree.currentItem()
		root = self.tree.invisibleRootItem()
		for item in self.tree.selectedItems():
			(item.parent() or root).removeChild(item)
        		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	tree = TreeWidgetDemo()
	tree.show()
	sys.exit(app.exec_())
