# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication,  QLabel  ,QWidget, QVBoxLayout 
from PyQt5 import QtCore  
from PyQt5.QtGui import QPixmap 
import sys  
    
class Absolute(QWidget):  
    def __init__(self ):  
        super().__init__()
                
        l1=QLabel(self)
        l2=QLabel(self)
        l3=QLabel(self)
        l4=QLabel(self)
        l1.setText("Hello World123")
        l4.setText("<A href='www.TutorialsPoint.com'>TutorialsPoint</a>")
        l2.setText("<a href='#'>welcome to Python GUI Programming</a>")
        l1.setAlignment(QtCore.Qt.AlignCenter)
        l3.setAlignment(QtCore.Qt.AlignCenter)
        l4.setAlignment(QtCore.Qt.AlignRight)
        l3.setPixmap(QPixmap("./images/python.jpg"))
        
        vbox=QVBoxLayout()
        vbox.addWidget(l1)
        vbox.addStretch()
        vbox.addWidget(l2)
        vbox.addStretch()
        vbox.addWidget(l3)
        vbox.addStretch()
        vbox.addWidget(l4)
        
        l1.setOpenExternalLinks(True)
        #l4.linkActivated.connect( clicked1 )
        #l2.linkHovered.connect(hovered)
        l1.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

        self.setLayout(vbox)
        self.setWindowTitle("QLabel Demo")
        
    def hovered():
        print( "hovering")
        
    def clicked1():
        print( "clicked" )
  
if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    qb = Absolute()  
    qb.show()  
    sys.exit(app.exec_())