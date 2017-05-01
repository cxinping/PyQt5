# -*- coding: utf-8 -*-
 
"""
    【简介】
     嵌套布局
    
    
"""


from PyQt5.QtWidgets import *
 
 
class MyWindow(QWidget):  

    def __init__(self):  
        super().__init__()
        self.setWindowTitle('PyQt5布局示例')
        self.resize(400, 300)
        
        # 全局部件（注意参数 self），用于"承载"全局布局
        wwg = QWidget(self)
        
        wl = QVBoxLayout(wwg) # 全局布局（注意参数 wwg）

        vl = QVBoxLayout() # 三个局部布局
        hl = QHBoxLayout()
        gl = QGridLayout()
        
        pass # 这里向局部布局内添加部件

        wl.addLayout(vl) # 加到全局布局
        wl.addLayout(gl)
        wl.addLayout(hl)
       

if __name__=="__main__":    
    import sys    
    
    app = QApplication(sys.argv)    
    win = MyWindow()  
    win.show()  
    sys.exit(app.exec_())
    
