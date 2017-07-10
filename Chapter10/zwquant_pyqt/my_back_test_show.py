# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem

from Ui_my_back_test_show import Ui_MainWindow
import pickle
import numpy as np
import os


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, qx=None, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        if qx != None: # 与zwquant结合，qx是zwquant的一个类实例
            self.qx = qx
            self.show_result(self.qx)
            self.matplotlibwidget_static.mpl.start_static_plot(self.qx)
        else: # 用于测试，不需要zwquant也能运行，方面快速开发自己的GUI界面。
            self.show_result()
            self.matplotlibwidget_static.mpl.start_static_plot()

    def show_result(self, qx=None):

        if qx != None: # 跑回测的话就传入回测的数据
            list_result = qx.result_info
            pickle_file = open('my_list.pkl', 'wb')  # 以 wb 方式写入
            pickle.dump(list_result, pickle_file)  # 向pickle_file中写入my_list
            pickle_file.close()
        else: # 不跑回测的话就读取测试数据
            pickle_file = open('my_list.pkl', 'rb')  # 以 rb 方式读取
            list_result = pickle.load(pickle_file)  # 读取以pickle方式写入的文件pickle_file
            pickle_file.close()

        list_result.append(['', ''])  # 为了能够凑够24*2（原来23*2），
        len_index = 6
        len_col = 8
        list0, list1, list2, list3 = [list_result[6 * i:6 * i + 6] for i in range(0, 4)]
        arr_result = np.concatenate([list0, list1, list2, list3], axis=1)
        self.tableWidget.setRowCount(len_index) # 设置行的数量
        self.tableWidget.setColumnCount(len_col) # 设置列的数量
        self.tableWidget.setHorizontalHeaderLabels(['回测内容', '回测结果'] * 4) # 设置垂直方向上的标题
        self.tableWidget.setVerticalHeaderLabels([str(i) for i in range(1, len_index + 1)]) # 设置水平方向上的标题


        for index in range(len_index):
            for col in range(len_col):
                self.tableWidget.setItem(index, col, QTableWidgetItem(arr_result[index, col]))
        self.tableWidget.resizeColumnsToContents() # 根据内容来调整列的宽度

    @pyqtSlot()
    def on_pushButton_show_dataPre_clicked(self):
        """
        Slot documentation goes here.
        """
        if hasattr(self, 'qx'):# 与zwquant结合，才进行下一步
            if hasattr(self.qx,'path_dataPre'):
                os.system(np.random.choice(self.qx.path_dataPre)) # 随机的选取数据预处理的文件结果，并打开

    @pyqtSlot()
    def on_pushButton_show_money_flow_clicked(self):
        """
        Slot documentation goes here.
        """
        if hasattr(self, 'qx'):# 与zwquant结合，才进行下一步
            os.system(self.qx.fn_qxLib)

    @pyqtSlot()
    def on_pushButton_show_trade_flow_clicked(self):
        """
        Slot documentation goes here.
        """
        if hasattr(self, 'qx'):# 与zwquant结合，才进行下一步
            os.system(self.qx.fn_xtrdLib)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.showMaximized()
    # ui.show()
    sys.exit(app.exec_())
