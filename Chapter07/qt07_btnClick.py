# -*- coding: utf-8 -*-

"""
    【简介】
     按钮传递鼠标按下事件例子


"""

import sys
from PyQt5.QtCore import  QSize
from PyQt5.QtWidgets import QApplication  ,QWidget  , QVBoxLayout, QMessageBox, QToolButton
from PyQt5.QtCore import Qt 

### 自定义窗口类  
class MyWindow( QWidget):
    '''自定义窗口类''' 
    def __init__(self,parent=None):
        '''构造函数'''
        # 调用父类构造函数
        super(MyWindow,self).__init__(parent)
        #设置窗体标题
        self.setWindowTitle("按钮传递鼠标按下事件例子") 
        # 设置窗口固定尺寸
        self.setFixedSize( QSize(820,600))
        # 创建主控件
        bodyWidget = QWidget(self)
        # 创建主布局
        mainLayout = QVBoxLayout(bodyWidget)
        # 遍历创建按钮
        for i in range(4):
            # 创建自定义按钮
            button = MyButton(self)
            # 设置文本内容
            button.setText("测试-%s" % i)
            # 添加控件
            mainLayout.addWidget(button)
            # 设置按钮点击连接槽函数
            button.clicked.connect(self.OnClick)
			
    def OnClick(self):
        '''响应点击'''
        QMessageBox.about(self,"测试","点击弹出窗口成功")

    def mousePressEvent(self,event):
        '''鼠标按下事件'''
        # 判断是否为鼠标左键按下
        if event.button() ==  Qt.LeftButton:
            # 设置窗口背景颜色
            self.setStyleSheet('''background-color:cyan;''')
        
### 自定义按钮类 
class MyButton( QToolButton):
    '''自定义按钮类'''
    def __init__(self,parent=None):
        '''构造函数'''
        # 调用父类构造函数
        super(MyButton,self).__init__(parent)
        # 设置按钮尺寸
        self.setFixedSize( QSize(800,120))
        # 设置按钮背景颜色
        self.setStyleSheet('''background-color:red;''')

    def mousePressEvent(self,event):
        '''鼠标按下事件'''
        # 判断是否为鼠标左键按下
        if event.button() ==  Qt.LeftButton:
            # 发射点击信号
            self.clicked.emit(True)
            # 传递至父窗口响应鼠标按下事件
            self.parent().mousePressEvent(event)
        
###  主函数 ####
if __name__ == "__main__":
    '''主函数'''
    # 声明变量
    app =QApplication(sys.argv)
    # 创建窗口
    window = MyWindow()
    # 设置窗口显示
    window.show()
    #应用程序事件循环
    sys.exit(app.exec_())
    
    
