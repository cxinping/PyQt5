# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication
import pyqtgraph as pg
from Ui_pyqtgraph_pyqt import Ui_MainWindow
import numpy as np


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)

        pg.setConfigOption('background', '#f0f0f0')  # 设置背景为灰色
        pg.setConfigOption('foreground', 'd')  # 设置前景（包括坐标轴，线条，文本等等）为黑色。

        pg.setConfigOptions(antialias=True) # 使曲线看起来更光滑，而不是锯齿状
        # pg.setConfigOption('antialias',True) # 等价于上一句，所不同之处在于setconfigOptions可以传递多个参数进行多个设置，而setConfigOption一次只能接受一个参数进行一个设置。
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.pyqtgraph1.clear() # 清空里面的内容，否则会发生重复绘图的结果

        '''第一种绘图方式'''
        self.pyqtgraph1.addPlot(title="绘图单条线", y=np.random.normal(size=100), pen=pg.mkPen(color='b', width=2))

        '''第二种绘图方式'''
        plt2 = self.pyqtgraph1.addPlot(title='绘制多条线')

        plt2.plot(np.random.normal(size=150), pen=pg.mkPen(color='r', width=2), name="Red curve") # pg.mkPen的使用方法，设置线条颜色为红色，宽度为2。
        plt2.plot(np.random.normal(size=110) + 5, pen=(0, 255, 0), name="Green curve")
        plt2.plot(np.random.normal(size=120) + 10, pen=(0, 0, 255), name="Blue curve")


    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        '''如果没有进行第一次绘图，就开始绘图，然后做绘图标记，否则就什么都不做'''
        try:
            self.first_plot_flag # 检测是否进行过第一次绘图。
        except:

            plt = self.pyqtgraph2.addPlot(title='绘制条状图')
            x = np.arange(10)
            y1 = np.sin(x)
            y2 = 1.1 * np.sin(x + 1)
            y3 = 1.2 * np.sin(x + 2)

            bg1 = pg.BarGraphItem(x=x, height=y1, width=0.3, brush='r')
            bg2 = pg.BarGraphItem(x=x + 0.33, height=y2, width=0.3, brush='g')
            bg3 = pg.BarGraphItem(x=x + 0.66, height=y3, width=0.3, brush='b')

            plt.addItem(bg1)
            plt.addItem(bg2)
            plt.addItem(bg3)

            self.pyqtgraph2.nextRow()

            p4 = self.pyqtgraph2.addPlot(title="参数图+显示网格")
            x = np.cos(np.linspace(0, 2 * np.pi, 1000))
            y = np.sin(np.linspace(0, 4 * np.pi, 1000))
            p4.plot(x, y, pen=pg.mkPen(color='d', width=2))
            p4.showGrid(x=True, y=True) # 显示网格

            self.first_plot_flag = True # 第一次绘图后进行标记

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
