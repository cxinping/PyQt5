# -*- coding: utf-8 -*-
 
"""
    【简介】
     嵌套布局
    
    
"""

import sys
from PyQt5.QtWidgets import QApplication  ,QWidget , QHBoxLayout,  QVBoxLayout,  QGridLayout ,  QFormLayout, QPushButton 
  
class MyWindow( QWidget):  

    def __init__(self):  
        super().__init__()
        self.setWindowTitle('嵌套布局示例')
       
        # 全局布局（1个）：水平
        wlayout =  QHBoxLayout() 
         # 局部布局（4个）：水平、竖直、网格、表单
        hlayout =  QHBoxLayout()
        vlayout =  QVBoxLayout()
        glayout = QGridLayout()
        formlayout =  QFormLayout()
        
        # 局部布局添加部件（例如：按钮）
        hlayout.addWidget( QPushButton(str(1)) ) 
        hlayout.addWidget( QPushButton(str(2)) )
        vlayout.addWidget( QPushButton(str(3)) )
        vlayout.addWidget( QPushButton(str(4)) )
        glayout.addWidget( QPushButton(str(5)) , 0, 0 )
        glayout.addWidget( QPushButton(str(6)) , 0, 1 )
        glayout.addWidget( QPushButton(str(7)) , 1, 0)
        glayout.addWidget( QPushButton(str(8)) , 1, 1)
        formlayout.addWidget( QPushButton(str(9))  )
        formlayout.addWidget( QPushButton(str(10)) )
        formlayout.addWidget( QPushButton(str(11)) )
        formlayout.addWidget( QPushButton(str(12)) )
        
        # 准备四个部件
        hwg =  QWidget() 
        vwg =  QWidget()
        gwg =  QWidget()
        fwg =  QWidget()
                
        # 四个部件设置局部布局
        hwg.setLayout(hlayout) 
        vwg.setLayout(vlayout)
        gwg.setLayout(glayout)
        fwg.setLayout(formlayout)
        
         # 四个部件加至全局布局
        wlayout.addWidget(hwg)
        wlayout.addWidget(vwg)
        wlayout.addWidget(gwg)
        wlayout.addWidget(fwg)
        
        # 窗体本体设置全局布局
        self.setLayout(wlayout) 
  
if __name__=="__main__":    
    app =  QApplication(sys.argv)    
    win = MyWindow()  
    win.show()  
    sys.exit(app.exec_())
    
