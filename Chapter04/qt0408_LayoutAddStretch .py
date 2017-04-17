# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QApplication,  QLabel  ,QWidget, QVBoxLayout ,QPushButton
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QPixmap ,QPalette
import sys  
    
class WindowDemo(QWidget):  
    def __init__(self ):  
        super().__init__()
                
        #1
        btn1 = QPushButton(self)
        btn2 = QPushButton(self)
        btn3 = QPushButton(self)
      
        btn1.setText('btn1')
        btn2.setText('btn2')
        btn3.setText('btn3')
        
        #2
        vbox=QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(btn1)
        vbox.addStretch(1)
        vbox.addWidget(btn2)
        vbox.addStretch(1)
        vbox.addWidget( btn3 )
        vbox.addStretch(1)        

        self.setLayout(vbox)
        self.setWindowTitle("addStretch 例子")
        

if __name__ == "__main__":  
    app = QApplication(sys.argv)  
    win = WindowDemo()  
    win.show()  
    sys.exit(app.exec_())


