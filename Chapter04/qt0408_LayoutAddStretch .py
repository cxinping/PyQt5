# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QApplication ,QWidget, QVBoxLayout ,QPushButton
import sys  
    
class WindowDemo(QWidget):  
    def __init__(self ):  
        super().__init__()
                
        #1
        btn1 = QPushButton(self)
        btn2 = QPushButton(self)
        btn3 = QPushButton(self)
      
        btn1.setText('button 1')
        btn2.setText('button 2')
        btn3.setText('button 3')
        
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


