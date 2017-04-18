# -*- coding: utf-8 -*-

'''
    【简介】
     PyQT5中坐标系统

'''

from PyQt5.QtWidgets import QApplication  ,QWidget  ,QPushButton
import sys  
              
app = QApplication(sys.argv)
widget = QWidget()
btn = QPushButton( widget )
btn.setText("Button")
#以QWidget左上角为(0, 0)点
btn.move(20, 20)   
#不同操作系统可能对窗口最小宽度有规定，若设置宽度小于规定值，则会以规定值进行显示
widget.resize(300, 200) 
#以屏幕左上角为(0, 0)点
widget.move(250, 200)

widget.setWindowTitle('PyQt坐标系统例子')
widget.show()
print("QWidget:")
print("w.x()=%d" % widget.x() )
print("w.y()=%d" % widget.y() )
print("w.width()=%d" % widget.width() )
print("w.height()=%d" % widget.height() )
print("QWidget.geometry")
print("widget.geometry().x()=%d" %  widget.geometry().x() )
print("widget.geometry().y()=%d" %  widget.geometry().y() )
print("widget.geometry().width()=%d" %  widget.geometry().width() )
print("widget.geometry().height()=%d" %  widget.geometry().height() )

sys.exit(app.exec_())  



    
