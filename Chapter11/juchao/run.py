# -*- coding: utf-8 -*-

"""
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Ui_run import Ui_MainWindow

from craw import get_one_page_data
import requests
import pandas as pd
import numpy as np
from pandas import Series
from pandas import DataFrame
import datetime
import os
import re

import threading
import copy


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    signal_status = pyqtSignal(str, list)  # 自定义的信号，用来显示状态栏。

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.total_pages_content = 1
        self.total_pages_title = 1
        self.current_page_num_title = 1
        self.current_page_num_content = 1
        self.sort_type = 'desc'
        self.sort_name = 'nothing'
        self.comboBox_dict = {'相关度': 'nothing', '时间': 'pubdate', '代码': 'stockcode_cat', '升序': 'asc', '降序': 'desc'}
        self.frame_advanced.hide() # 默认隐藏 frame
        self.download_info_list = []  # 存储要下载的信息，每个元素是字典形式，存储了要下载的标题，url等等信息。
        self.download_path = os.path.abspath(r'./下载')
        self.label_show_path.setText('当前保存目录为：' + self.download_path)
        self.tableWidget_title_checked = Qt.Unchecked  # 设置tableWidget的默认选择方式。
        self.tableWidget_content_checked = Qt.Unchecked
        self.select_title_page_info = set()  # 记录checkBox_select选择的页面信息。
        self.select_content_page_info = set()# 记录checkBox_select选择的页面信息。
        self.filter_title_list = [] # 用来显示过滤title的list
        self.filter_content_list = [] # 用来显示过滤content的list


        '''下面四行代码一定要按照顺序执行，否则self.start_time,与self.end_time这两行代码会无效'''
        self.dateEdit.setDateTime(datetime.datetime.now())
        self.dateEdit_2.setDateTime(datetime.datetime.now())
        self.start_time = ''
        self.end_time = ''

        self.dateEdit.setEnabled(False)
        self.dateEdit_2.setEnabled(False)
        self.comboBox_type.setEnabled(False)
        self.comboBox_name.setEnabled(False)
        self.lineEdit_filter_content.setEnabled(False)
        self.lineEdit_filter_title.setEnabled(False)

        '''连接信号与槽'''
        '显示 or 隐藏高级选项'
        self.pushButton_setting_advanced.toggled['bool'].connect(self.frame_advanced.setHidden)
        '下载'
        self.pushButton_download_select_title.clicked.connect(self.download_pdf)
        self.pushButton_download_select_content.clicked.connect(self.download_pdf)
        download_thread.signal.connect(self.show_status)  # 子线程的信号连接主线程的槽
        '修改存储路径'
        self.pushButton_change_save_path.clicked.connect(self.change_save_path)
        'tableWidget相关'
        self.tableWidget_title.itemChanged.connect(self.select_item)
        self.tableWidget_content.itemChanged.connect(self.select_item)
        self.tableWidget_title.cellClicked.connect(self.view_one_new)
        self.tableWidget_content.cellClicked.connect(self.view_one_new)
        '状态条显示'
        self.signal_status.connect(self.show_status)  # 状态栏信号绑定槽
        '在lineEdit控件上按下Enter就可以触发搜索或跳转到页码'
        self.lineEdit.returnPressed.connect(self.on_pushButton_search_clicked)
        self.lineEdit_filter_title.returnPressed.connect(self.on_pushButton_search_clicked)
        self.lineEdit_filter_content.returnPressed.connect(self.on_pushButton_search_clicked)
        self.lineEdit_content_page.returnPressed.connect(self.pushButton_content_jump_to.click)
        self.lineEdit_title_page.returnPressed.connect(lambda: self.page_go('title_jump_to'))
        '页码跳转函数'
        self.pushButton_title_down.clicked.connect(lambda: self.page_go('title_down'))
        self.pushButton_content_down.clicked.connect(lambda: self.page_go('content_down'))
        self.pushButton_title_up.clicked.connect(lambda: self.page_go('title_up'))
        self.pushButton_content_up.clicked.connect(lambda: self.page_go('content_up'))
        self.pushButton_title_jump_to.clicked.connect(lambda: self.page_go('title_jump_to'))
        self.pushButton_content_jump_to.clicked.connect(lambda: self.page_go('content_jump_to'))
        '选择标题 or 内容'
        self.checkBox_select_title.clicked['bool'].connect(self.select_checkBox)
        self.checkBox_select_content.clicked['bool'].connect(self.select_checkBox)
        '显示/下载过滤操作'
        self.checkBox_filter_title.clicked['bool'].connect(self.filter_enable)
        self.checkBox_filter_content.clicked['bool'].connect(self.filter_enable)

        '初始化下载目录'
        if not os.path.isdir(self.download_path):
            os.mkdir(self.download_path)

    def filter_df(self, df, filter_title_list=[],filter_content_list=[]):
        '''
        过滤df的主函数。
        :param df: df.columns
                Out[10]: 
                Index(['content', 'download_url', 'time', 'title'], dtype='object')

        :param filter_title_list: filter_title_list=['成都','年度'|'季度']
        filter_content_list: filter_content_list=['成都','年度'|'季度']
        :return: df_filter
        '''
        for each in filter_title_list:
            ser = df.title
            df = df[ser.str.contains(each)]
        filter_content_list = [each + '|None' for each in filter_content_list] # 处理内容返回为None的情况，作用是若没有文章内容返回，则不进行过滤。
        for each in filter_content_list:
            ser = df.content
            df = df[ser.str.contains(each)]
        return df

    def get_filter_list(self,filter_text):
        filter_text = re.sub(r'[\s()（）]','',filter_text) #剔除空格，(,),（,）,换行符等元素。
        filter_list = filter_text.split('&')
        return filter_list

    def filter_enable(self, bool):
        sender = self.sender()
        if sender.objectName() == 'checkBox_filter_title':
            if bool == True:
                self.lineEdit_filter_title.setEnabled(True)
            else:
                self.lineEdit_filter_title.setEnabled(False)
        elif sender.objectName() == 'checkBox_filter_content':
            if bool == True:
                self.lineEdit_filter_content.setEnabled(True)
            else:
                self.lineEdit_filter_content.setEnabled(False)


    def select_tableWidget(self, tableWidget):
        '''选择tableWidget的函数'''
        row_count = tableWidget.rowCount()
        for index in range(row_count):
            item = tableWidget.item(index, 0)
            if item.checkState() == Qt.Unchecked:
                item.setCheckState(Qt.Checked)

    def select_tableWidget_clear(self, tableWidget):
        '''清除选择tableWidget的槽函数'''
        row_count = tableWidget.rowCount()
        for index in range(row_count):
            item = tableWidget.item(index, 0)
            if item.checkState() == Qt.Checked:
                item.setCheckState(Qt.Unchecked)

    def select_checkBox_one(self, sender, tableWidget):
        if sender.checkState() == Qt.Checked:
            self.select_tableWidget(tableWidget)
            if tableWidget.objectName() == 'tableWidget_title':
                self.select_title_page_info.add(self.current_page_num_title)
            elif tableWidget.objectName() == 'tableWidget_content':
                self.select_content_page_info.add(self.current_page_num_content)
        else:
            self.select_tableWidget_clear(tableWidget)
            if tableWidget.objectName() == 'tableWidget_title':
                if self.current_page_num_title in self.select_title_page_info:
                    self.select_title_page_info.remove(self.current_page_num_title)
            elif tableWidget.objectName() == 'tableWidget_content':
                if self.current_page_num_content in self.select_content_page_info:
                    self.select_content_page_info.remove(self.current_page_num_content)

    def select_checkBox(self, bool):
        sender = self.sender() # sender()返回的是触发了这个信号的哪个部件
        if sender.objectName() == 'checkBox_select_title':
            self.select_checkBox_one(sender, self.tableWidget_title)
        elif sender.objectName() == 'checkBox_select_content':
            self.select_checkBox_one(sender, self.tableWidget_content)


    def page_go(self, go_type):
        '''页面跳转主函数'''
        if go_type == 'title_down': # 触发下一页按钮
            _temp = self.current_page_num_title
            self.current_page_num_title += 1
            if 1 <= self.current_page_num_title <= self.total_pages_title: # 如果待跳转的页面真实有效，则继续。否则不进行跳转
                self.update_tablewidget_title(page_num=self.current_page_num_title)
            else:
                self.current_page_num_title = _temp
        elif go_type == 'title_up':
            _temp = self.current_page_num_title
            self.current_page_num_title -= 1
            # print(self.current_page_num_title)
            if 1 <= self.current_page_num_title <= self.total_pages_title:
                self.update_tablewidget_title(page_num=self.current_page_num_title)
            else:
                self.current_page_num_title = _temp
        elif go_type == 'content_up':
            _temp = self.current_page_num_content
            self.current_page_num_content -= 1
            if 1 <= self.current_page_num_content <= self.total_pages_content:
                self.update_tablewidget_content(page_num=self.current_page_num_content)
            else:
                self.current_page_num_content = _temp
        elif go_type == 'content_down':
            _temp = self.current_page_num_content
            self.current_page_num_content += 1
            if 1 <= self.current_page_num_content <= self.total_pages_content:
                self.update_tablewidget_content(page_num=self.current_page_num_content)
            else:
                self.current_page_num_content = _temp
        elif go_type == 'title_jump_to':
            _temp = self.current_page_num_title
            self.current_page_num_title = int(self.lineEdit_title_page.text())
            if 1 <= self.current_page_num_title <= self.total_pages_title:
                self.update_tablewidget_title(page_num=self.current_page_num_title)
            else:
                self.current_page_num_title = _temp
        elif go_type == 'content_jump_to':
            _temp = self.current_page_num_content
            self.current_page_num_content = int(self.lineEdit_content_page.text())
            if 1 <= self.current_page_num_content <= self.total_pages_content:
                self.update_tablewidget_content(page_num=self.current_page_num_content)
            else:
                self.current_page_num_content = _temp


    # def select(self, select_type):
    #     '''
    #     :param select_type:is a string: title,content, two
    #     :return:
    #     '''
    #     if select_type == 'title':
    #         self.select_tableWidget(self.tableWidget_title)
    #     elif select_type == 'content':
    #         self.select_tableWidget(self.tableWidget_content)



    # def select_clear(self):
    #     '''清除选择的槽函数'''
    #     self.select_tableWidget_clear(self.tableWidget_content)
    #     self.select_tableWidget_clear(self.tableWidget_title)


    def download_pdf(self):
        '''下载pdf的主函数'''
        if download_thread.isRunning() == True:
            QMessageBox.warning(self, '警告!', '检测到下载程序正在运行，请不要重复运行', QMessageBox.Yes)
            return None

        download_thread.download_list = self.download_info_list.copy()
        download_thread.download_path = copy.copy(self.download_path)
        download_thread.start()

    def view_one_new(self, row, column):
        '''查看新闻的主函数'''
        sender = self.sender()
        if column == 2:  # 只针对第三列--->查看
            if sender.objectName() == 'tableWidget_title':
                download_one = self.list_target_title[row]
            else:
                download_one = self.list_target_content[row]
            download_path = copy.copy(self.download_path)
            view_thread = threading.Thread(target=self.view_one_new_thread, args=(download_path, download_one),
                                           daemon=True)
            view_thread.start()

    def view_one_new_thread(self, download_path, download_one):
        '''查看功能的多线程程序'''
        download_url = download_one['download_url']
        title = download_one['title']
        title = title.replace(':', '：')
        title = title.replace('?', '？')
        title = title.replace('*', '★')

        path = download_path + os.sep + '%s.pdf' % title
        if not os.path.isfile(path):
            try:
                r = requests.get(download_url, stream=True)
                data = r.raw.read()
            except:
                return
            f = open(path, "wb")
            f.write(data)
            f.close()
        os.system(path)


    def show_status(self, type, list_args):
        if type == 'download_status':
            count_num, count_all, count_right, count_err, title = list_args
            self.statusBar().showMessage(
                '完成:{0}/{3}，正确:{1}，错误：{2}，本次下载：{4}'.format(count_num, count_right, count_err, count_all, title))
        if type == 'download_status_err':
            count_num, count_all, count_right, count_err, title = list_args
            self.statusBar().showMessage(
                '重新下载失败：完成:{0}/{3}，正确:{1}，错误：{2}，本次下载：{4}'.format(count_num, count_right, count_err, count_all, title))
        if type == 'select_status':
            self.statusBar().showMessage('已选择：%d' % len(self.download_info_list))
        if type == 'change_save_path_status':
            self.statusBar().showMessage('保存目录修改为：%s' % self.download_path)
        if type == 'clear':
            self.statusBar().showMessage(' ')

    def change_save_path(self):
        '''修改保存目录
        '''

        if not os.path.isdir(self.download_path):
            os.mkdir(self.download_path)
        directory1 = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      self.download_path)  # 起始路径
        self.download_path = QDir.toNativeSeparators(directory1)  # 路径以windows支持的显示方式进行显示。
        self.label_show_path.setText('当前保存目录为： ' + self.download_path)
        self.signal_status.emit('change_save_path_status', [])

    def show_tablewidget(self, dict_data, tableWidget, clear_fore=True):
        '''传入dict_data 与 tableWidget，以实现在tablewidget上面呈现dict_data'''
        '''提取自己需要的信息：'''
        if clear_fore == True:  # 检测搜索之前是否要清空下载购物车信息。
            self.download_info_list = []

        '更新状态栏信息'
        self.signal_status.emit('clear', []) # 清空状态栏

        '检测checkBox之前是否已经被选中过，若选中过则设置为选中，否则设置为不选中'
        if tableWidget.objectName() == 'tableWidget_title':
            if self.current_page_num_title in self.select_title_page_info:
                self.checkBox_select_title.setCheckState(Qt.Checked)
            else:
                self.checkBox_select_title.setCheckState(Qt.Unchecked)
            flag = 'title'
        else:
            if self.current_page_num_content in self.select_content_page_info:
                self.checkBox_select_content.setCheckState(Qt.Checked)
            else:
                self.checkBox_select_content.setCheckState(Qt.Unchecked)
            flag = 'content'

        '''检测过滤显示的信息'''
        if self.lineEdit_filter_title.isEnabled() == True:
            filter_text = self.lineEdit_filter_title.text()
            self.filter_title_list = self.get_filter_list(filter_text)
        else:
            self.filter_title_list=[]
        if self.lineEdit_filter_content.isEnabled() == True:
            filter_text = self.lineEdit_filter_content.text()
            self.filter_content_list = self.get_filter_list(filter_text)
        else:
            self.filter_content_list=[]

        '''从传入的网络爬虫抓取的数据中提取自己需要的数据'''
        if len(dict_data) > 0:
            # key_word = self.lineEdit.text()
            len_index = len(dict_data)
            list_target = []  # 从dict_data中提取目标数据，基本元素是下面的dict_target
            for index in range(len_index):
                dict_temp = dict_data[index] # 提取从服务器中返回的其中一行信息。
                dict_target = {} # 从dict_temp中提取自己需要的信息，主要包括title,content,time,download_url等等
                '提取标题与内容'
                _temp_title = dict_temp['announcementTitle']
                _temp_content = dict_temp['announcementContent']
                for i in ['<em>', '</em>']: # <em>, </em>是服务器对搜索关键字添加的标记，这里对它们剔除
                    _temp_title = _temp_title.replace(i, '')
                    _temp_content = str(_temp_content).replace(i, '')

                dict_target['title'] = _temp_title
                dict_target['content'] = _temp_content

                '提取时间'
                _temp = dict_temp['adjunctUrl']
                dict_target['time'] = _temp.split(r'/')[1]

                '提取url'
                id = _temp.split(r'/')[2].split('.')[0]
                download_url = 'http://www.cninfo.com.cn/cninfo-new/disclosure/fulltext/download/{}?announceTime={}'.format(
                    id, dict_target['time'])
                dict_target['download_url'] = download_url
                dict_target['flag'] = flag
                # print(download_url)
                '添加处理的结果'
                list_target.append(dict_target)

            '''根据过滤规则，进行自定义过滤，默认是不过滤'''
            df = DataFrame(list_target)
            df = self.filter_df(df,filter_title_list=self.filter_title_list,filter_content_list = self.filter_content_list)

            '''过滤后，更新list_target'''
            _temp = df.to_dict('index')
            list_target = list(_temp.values())

        else:  # '处理没有数据的情况'
            list_target = []

        '''tableWidget的初始化'''
        list_col = ['time', 'title', 'download_url']
        len_col = len(list_col)
        len_index = len(list_target)  # list_target可能有所改变，需要重新计算一下长度。
        if tableWidget.objectName() == 'tableWidget_title':
            self.list_target_title = list_target
        else:
            self.list_target_content = list_target
        tableWidget.setRowCount(len_index) # 设置行数
        tableWidget.setColumnCount(len_col) # 设置列数
        tableWidget.setHorizontalHeaderLabels(['时间', '标题', '查看']) # 设置垂直方向上的名字
        tableWidget.setVerticalHeaderLabels([str(i) for i in range(1, len_index + 1)]) # 设置水平方向上的名字
        tableWidget.setCornerButtonEnabled(True) # 左上角一点击就全选

        '''填充tableWidget的数据'''
        for index in range(len_index):
            for col in range(len_col):
                name_col = list_col[col]
                if name_col == 'download_url':
                    item = QTableWidgetItem('查看')
                    item.setTextAlignment(Qt.AlignCenter)
                    font = QFont()
                    font.setBold(True)
                    font.setWeight(75)
                    item.setFont(font)
                    item.setBackground(QColor(218, 218, 218))
                    item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                    tableWidget.setItem(index, col, item)
                elif name_col == 'time':
                    item = QTableWidgetItem(list_target[index][name_col])
                    item.setFlags(Qt.ItemIsUserCheckable |
                                  Qt.ItemIsEnabled)
                    '''查看当前行所代表的内容是否已经在下载购物车里面，如过在的话就设置为选中'''
                    if list_target[index] in self.download_info_list:
                        item.setCheckState(Qt.Checked)
                    else:
                        item.setCheckState(Qt.Unchecked)
                    tableWidget.setItem(index, col, item)
                else:
                    tableWidget.setItem(index, col, QTableWidgetItem(list_target[index][name_col]))
        # tableWidget.resizeColumnsToContents()
        tableWidget.setColumnWidth(1, 500)

    def select_item(self, item):
        '''处理选择item的主函数'''
        # print('item+change')
        column = item.column()
        row = item.row()
        if column == 0:  # 只针对第一列
            if item.checkState() == Qt.Checked:
                if item.tableWidget().objectName() == 'tableWidget_title':
                    download_one = self.list_target_title[row]
                else:
                    download_one = self.list_target_content[row]
                if download_one not in self.download_info_list:
                    self.download_info_list.append(download_one)
                    self.signal_status.emit('select_status', [])
            else:
                if item.tableWidget().objectName() == 'tableWidget_title':
                    download_one = self.list_target_title[row]
                else:
                    download_one = self.list_target_content[row]
                if download_one in self.download_info_list:
                    self.download_info_list.remove(download_one)
                    self.signal_status.emit('select_status', [])

    def update_tablewidget_title(self, page_num=1):
        '''更新tablewidget_title'''
        key_word = self.lineEdit.text()
        '''从网络爬虫中获取数据'''
        total_pages_title, dict_data_title = get_one_page_data(key_word, fulltext_str_flag='false', page_num=page_num,
                                                               date_start=self.start_time, date_end=self.end_time,
                                                               sortName=self.sort_name, sortType=self.sort_type)
        '''把数据显示到表格上'''
        if total_pages_title != None:
            self.total_pages_title = total_pages_title
            self.show_tablewidget(dict_data_title, self.tableWidget_title, clear_fore=False)
            self.label_page_info_title.setText('%d/%d' % (self.current_page_num_title, self.total_pages_title)) # 更新当前页码信息

    def update_tablewidget_content(self, page_num=1):
        '''更新tablewidget_content'''
        key_word = self.lineEdit.text()
        total_pages_content, dict_data_content = get_one_page_data(key_word, fulltext_str_flag='true',
                                                                   page_num=page_num, date_start=self.start_time,
                                                                   date_end=self.end_time, sortName=self.sort_name,
                                                                   sortType=self.sort_type)
        if total_pages_content != None:
            self.total_pages_content = total_pages_content
            self.show_tablewidget(dict_data_content, self.tableWidget_content, clear_fore=False)
            self.label_page_info_content.setText('%d/%d' % (self.current_page_num_content, self.total_pages_content))

    def get_dateEdit_time(self, dateEdit):
        dateEdit_day = dateEdit.text().replace('/', '-')
        datetime_day = datetime.datetime.strptime(dateEdit_day, '%Y-%m-%d')
        return datetime_day.strftime('%Y-%m-%d')

    @pyqtSlot()
    def on_pushButton_search_clicked(self):
        """
        Slot documentation goes here.
        """
        self.download_info_list = [] # 每一次重新搜索都要清空下载购物车
        self.current_page_num_title = 1 # 初始化搜索，默认当前页码为1
        self.current_page_num_content = 1
        self.update_tablewidget_title() # 更新标题搜索
        self.update_tablewidget_content() # 更新内容搜索

    @pyqtSlot(bool)
    def on_checkBox_unlimite_time_flag_clicked(self, checked):
        """
        Slot documentation goes here.

        @param checked DESCRIPTION
        @type bool
        """

        if checked == True:
            self.dateEdit.setEnabled(False)
            self.dateEdit_2.setEnabled(False)
            self.end_time = ''
            self.start_time = ''
        else:
            self.dateEdit.setEnabled(True)
            self.dateEdit_2.setEnabled(True)
            self.start_time = self.get_dateEdit_time(self.dateEdit)
            self.end_time = self.get_dateEdit_time(self.dateEdit_2)
            # print(self.start_time,self.end_time)

    @pyqtSlot(QDate)
    def on_dateEdit_dateChanged(self, date):
        self.start_time = self.get_dateEdit_time(self.dateEdit)

    @pyqtSlot(QDate)
    def on_dateEdit_2_dateChanged(self, date):
        self.end_time = self.get_dateEdit_time(self.dateEdit_2)

    @pyqtSlot(bool)
    def on_checkBox_sort_flag_clicked(self, checked):
        if checked == True: # 恢复默认的排序
            self.comboBox_name.setEnabled(False)
            self.comboBox_type.setEnabled(False)
            self.sort_name = 'nothing'
            self.sort_type = 'desc'
        elif self.comboBox_name.currentText() == '相关度': # 对于相关度，有些特殊
            self.comboBox_name.setEnabled(True)
            self.comboBox_type.setEnabled(False) # 上面comboBox_name.currentText()=="相关度"则这个控件不可以用。这个是模拟官网的操作。
            self.sort_name = 'nothing'
            self.sort_type = 'desc'
        else:# 对于其他，则设置对应参数
            self.comboBox_name.setEnabled(True)
            self.comboBox_type.setEnabled(True)
            sort_name = self.comboBox_name.currentText()
            sort_type = self.comboBox_type.currentText()

            self.sort_name = self.comboBox_dict[sort_name]
            self.sort_type = self.comboBox_dict[sort_type]

    @pyqtSlot(str)
    def on_comboBox_name_currentTextChanged(self, p0):
        if p0 == '相关度':
            self.comboBox_name.setEnabled(True)
            self.comboBox_type.setEnabled(False)
            self.sort_name = 'nothing'
            self.sort_type = 'desc'
        else:
            self.comboBox_name.setEnabled(True)
            self.comboBox_type.setEnabled(True)
            sort_name = self.comboBox_name.currentText()
            self.sort_name = self.comboBox_dict[sort_name]

    @pyqtSlot(str)
    def on_comboBox_type_currentTextChanged(self, p0):
        sort_type = self.comboBox_type.currentText()
        self.sort_type = self.comboBox_dict[sort_type]


class WorkThread(QThread):
    #声明一个包括str和list类型参数的信号
    signal = pyqtSignal(str, list)

    def __int__(self):
        self.download_list = self.download_path = []
        self.download_list_err = []
        self.filter_content_list = self.filter_title_list = []
        super(WorkThread, self).__init__()

    def main_download(self, download_list, download_path, download_status='download_status'):
        count_all = len(download_list)
        count_err = count_right = count_num = 0
        self.download_list_err = []
        for key_dict in download_list:
            count_num += 1
            download_url = key_dict['download_url']
            time = key_dict['time']
            title = key_dict['title']
            total_title = time + '_' + title
            total_title = total_title.replace(':', '：')
            total_title = total_title.replace('?', '？')
            total_title = total_title.replace('*', '★')

            file_path = download_path + os.sep + '%s.pdf' % total_title
            if os.path.isfile(file_path) == True: # 若文件已经存在，则默认为下载成功。
                count_right += 1
                signal_list = [count_num, count_all, count_right, count_err, title]
                self.signal.emit(download_status, signal_list)  # 循环完毕后发出信号
                continue
            else:
                f = open(file_path, "wb")  # 先建立一个文件，以免其他线程重复建立这个文件
                try:
                    r = requests.get(download_url, stream=True)
                    data = r.raw.read()
                except:
                    self.download_list_err.append(key_dict)
                    count_err += 1
                    f.close()
                    os.remove(file_path)  # 文件下载失败，要先关闭open函数，然后删除文件
                    signal_list = [count_num, count_all, count_right, count_err, title]
                    self.signal.emit(download_status, signal_list)  # 循环完毕后发出信号
                    continue
                f.write(data)
                f.close()
                count_right += 1
                signal_list = [count_num, count_all, count_right, count_err, title]
                self.signal.emit(download_status, signal_list)  # 循环完毕后发出信号

    def run(self):
        self.main_download(self.download_list, self.download_path, download_status='download_status')
        self.main_download(self.download_list_err, self.download_path, download_status='download_status_err')
        self.main_download(self.download_list_err, self.download_path, download_status='download_status_err')


if __name__ == "__main__":
    import sys

    download_thread = WorkThread()
    app = QApplication(sys.argv)
    ui = MainWindow()
    # ui.showMaximized()
    ui.show()

    sys.exit(app.exec_())
