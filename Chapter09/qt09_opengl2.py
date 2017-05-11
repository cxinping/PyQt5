# -*- coding: utf-8 -*-


"""
    【简介】
    QtOpenGL  例子
    
    
"""

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PyQt5.QtOpenGL import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ShapeWidget( QGLWidget ):
	def __init__(self, parent=None):
		super(ShapeWidget,self).__init__(parent)
		#self.setMinimumSize(600, 600)
    
	def paintGL(self):
		print('111--- paintGL ---')
        
		#使用glut初始化OpenGL
		glutInit()
		
		#glLoadIdentity();  
		#gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
		#glutWireTeapot(2);
	
		#显示模式:GLUT_SINGLE无缓冲直接显示|GLUT_RGBA采用RGB(A非alpha)
		glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
		#窗口位置及大小-生成
		#glutInitWindowPosition(0,0)
		#glutInitWindowSize(400,400)
		#参数为b类型而不是string  
		#glutCreateWindow(b"second OpenGL")
		#调用函数绘制图像
		#glutDisplayFunc(self.drawFunc)
		#glutIdleFunc(self.drawFunc)
   
		self.initializeGL1() 
		glFlush()
		#主循环
		#glutMainLoop()                  
        
	def initializeGL1(self):	 
		#Initialize GL
		# set viewing projection
		print('222--- initializeGL ---')
		#清除之前画面
		glClear(GL_COLOR_BUFFER_BIT)
		#(角度,x,y,z)
		#glRotatef(0.1, 5, 5, 0)  
		glutWireTeapot(0.5)
		#刷新显示
		glFlush()
		
    
class ShapeWidgetDemo( QMainWindow):
	def __init__(self , parent=None):
		super(ShapeWidgetDemo,self).__init__(parent)
		self.setMinimumSize(600, 600)

		widget = ShapeWidget(self)    
		self.setCentralWidget(widget) 
    
if __name__ == '__main__':
	app =  QApplication(sys.argv)
	window = ShapeWidgetDemo()
	window.show()
	sys.exit(app.exec_())





