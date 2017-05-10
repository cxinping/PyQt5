#!/usr/bin/env python3

'''
    【简介】
	PyQT5中 QTreeWidget 例子
   
  
'''

from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        dogs = [["Molly", "Labrador"],
                ["Max", "Siberian Husky"],
                ["Benny", "Alsation"]]

        self.treewidget = QTreeWidget()
        self.treewidget.setHeaderLabels(["Name", "Breed"])

        for item in dogs:
            dog = QTreeWidgetItem(item)
            self.treewidget.addTopLevelItem(dog)

        self.treewidget.clicked.connect(self.on_tree_widget_clicked)
        layout.addWidget(self.treewidget)

    def on_tree_widget_clicked(self, qmodelindex):
        item = self.treewidget.currentItem()
        print("%s is a %s breed" % (item.text(0), item.text(1)))

app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())
