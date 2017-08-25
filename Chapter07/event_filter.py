# -*- coding: utf-8 -*-
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class EventFilter(QDialog):
    def __init__(self, parent=None):
        super(EventFilter, self).__init__(parent)
        self.setWindowTitle("事件过滤器")

        self.label1 = QLabel("请点击")
        self.label2 = QLabel("请点击")
        self.label3 = QLabel("请点击")
        self.LabelState = QLabel("test")

        self.image1 = QImage("images/cartoon1.ico")
        self.image2 = QImage("images/cartoon1.ico")
        self.image3 = QImage("images/cartoon1.ico")

        self.width = 600
        self.height = 300

        self.resize(self.width, self.height)

        self.label1.installEventFilter(self)
        self.label2.installEventFilter(self)
        self.label3.installEventFilter(self)

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(self.label1, 500, 0)
        mainLayout.addWidget(self.label2, 500, 1)
        mainLayout.addWidget(self.label3, 500, 2)
        mainLayout.addWidget(self.LabelState, 600, 1)
        self.setLayout(mainLayout)

    def eventFilter(self, watched, event):
        if watched == self.label1: # 只对label1的点击事件进行过滤，重写其行为，其他的事件会被忽略
            if event.type() == QEvent.MouseButtonPress: # 这里对鼠标按下事件进行过滤，重写其行为
                mouseEvent = QMouseEvent(event)
                if mouseEvent.buttons() == Qt.LeftButton:
                    self.LabelState.setText("按下鼠标左键")
                elif mouseEvent.buttons() == Qt.MidButton:
                    self.LabelState.setText("按下鼠标中间键")
                elif mouseEvent.buttons() == Qt.RightButton:
                    self.LabelState.setText("按下鼠标右键")

                '''转换图片大小'''
                transform = QTransform()
                transform.scale(0.5, 0.5)
                tmp = self.image1.transformed(transform)
                self.label1.setPixmap(QPixmap.fromImage(tmp))
            if event.type() == QEvent.MouseButtonRelease: # 这里对鼠标释放事件进行过滤，重写其行为
                self.LabelState.setText("释放鼠标按钮")
                self.label1.setPixmap(QPixmap.fromImage(self.image1))
        return QDialog.eventFilter(self, watched, event) # 其他情况会返回系统默认的事件处理方法。


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = EventFilter()
    dialog.show()
    sys.exit(app.exec_())
