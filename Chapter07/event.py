
import sys
from PyQt5.QtCore import (QEvent, QTimer, Qt)
from PyQt5.QtWidgets import (QApplication, QMenu, QWidget)
from PyQt5.QtGui import QPainter


class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.justDoubleClicked = False
        self.key = ""
        self.text = ""
        self.message = ""
        self.resize(400, 300)
        self.move(100, 100)
        self.setWindowTitle("Events")
        QTimer.singleShot(0, self.giveHelp)  # 避免窗口大小重绘事件的影响，可以把参数0改变成3000（3秒），然后在运行，就可以明白这行代码的意思。

    def giveHelp(self):
        self.text = "请点击这里触发追踪鼠标功能"
        self.update() # 重绘事件，也就是触发paintEvent函数。

    '''重新实现关闭事件'''
    def closeEvent(self, event):
        print("Closed")

    '''重新实现上下文菜单事件'''
    def contextMenuEvent(self, event):
        menu = QMenu(self)
        oneAction = menu.addAction("&One")
        twoAction = menu.addAction("&Two")
        oneAction.triggered.connect(self.one)
        twoAction.triggered.connect(self.two)
        if not self.message:
            menu.addSeparator()
            threeAction = menu.addAction("Thre&e")
            threeAction.triggered.connect(self.three)
        menu.exec_(event.globalPos())

    '''上下文菜单槽函数'''
    def one(self):
        self.message = "Menu option One"
        self.update()

    def two(self):
        self.message = "Menu option Two"
        self.update()

    def three(self):
        self.message = "Menu option Three"
        self.update()

    '''重新实现绘制事件'''
    def paintEvent(self, event):
        text = self.text
        i = text.find("\n\n")
        if i >= 0:
            text = text[0:i]
        if self.key: # 若触发了键盘按钮，则在文本信息中记录这个按钮信息。
            text += "\n\n你按下了: {0}".format(self.key)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.TextAntialiasing)
        painter.drawText(self.rect(), Qt.AlignCenter, text) # 绘制信息文本的内容
        if self.message: # 若消息文本存在则在底部居中绘制消息，5秒钟后清空消息文本并重绘。
            painter.drawText(self.rect(), Qt.AlignBottom | Qt.AlignHCenter,
                             self.message)
            QTimer.singleShot(5000, self.clearMessage)
            QTimer.singleShot(5000, self.update)

    '''清空消息文本的槽函数'''
    def clearMessage(self):
        self.message = ""

    '''重新实现调整窗口大小事件'''
    def resizeEvent(self, event):
        self.text = "调整窗口大小为： QSize({0}, {1})".format(
            event.size().width(), event.size().height())
        self.update()

    '''重新实现鼠标释放事件'''
    def mouseReleaseEvent(self, event):
        # 若鼠标释放为双击释放，则不跟踪鼠标移动
        # 若鼠标释放为单击释放，则需要改变跟踪功能的状态，如果开启跟踪功能的话就跟踪，不开启跟踪功能就不跟踪
        if self.justDoubleClicked:
            self.justDoubleClicked = False
        else:
            self.setMouseTracking(not self.hasMouseTracking()) # 单击鼠标
            if self.hasMouseTracking():
                self.text = "开启鼠标跟踪功能.\n" + \
                            "请移动一下鼠标！\n" + \
                            "单击鼠标可以关闭这个功能"
            else:
                self.text = "关闭鼠标跟踪功能.\n" + \
                            "单击鼠标可以开启这个功能"
            self.update()

    '''重新实现鼠标移动事件'''
    def mouseMoveEvent(self, event):
        if not self.justDoubleClicked:
            globalPos = self.mapToGlobal(event.pos()) # 窗口坐标转换为屏幕坐标
            self.text = """鼠标位置：
            窗口坐标为：QPoint({0}, {1}) 
            屏幕坐标为：QPoint({2}, {3}) """.format(event.pos().x(), event.pos().y(), globalPos.x(), globalPos.y())
            self.update()

    '''重新实现鼠标双击事件'''
    def mouseDoubleClickEvent(self, event):
        self.justDoubleClicked = True
        self.text = "你双击了鼠标"
        self.update()

    '''重新实现键盘按下事件'''
    def keyPressEvent(self, event):
        self.key = ""
        if event.key() == Qt.Key_Home:
            self.key = "Home"
        elif event.key() == Qt.Key_End:
            self.key = "End"
        elif event.key() == Qt.Key_PageUp:
            if event.modifiers() & Qt.ControlModifier:
                self.key = "Ctrl+PageUp"
            else:
                self.key = "PageUp"
        elif event.key() == Qt.Key_PageDown:
            if event.modifiers() & Qt.ControlModifier:
                self.key = "Ctrl+PageDown"
            else:
                self.key = "PageDown"
        elif Qt.Key_A <= event.key() <= Qt.Key_Z:
            if event.modifiers() & Qt.ShiftModifier:
                self.key = "Shift+"
            self.key += event.text()
        if self.key:
            self.key = self.key
            self.update()
        else:
            QWidget.keyPressEvent(self, event)

    '''重新实现其他事件，适用于PyQt没有提供该事件的处理函数的情况，Tab键由于涉及焦点切换，不会传递给keyPressEvent，因此，需要在这里重新定义。'''
    def event(self, event):
        if (event.type() == QEvent.KeyPress and
                    event.key() == Qt.Key_Tab):
            self.key = "在event()中捕获Tab键"
            self.update()
            return True
        return QWidget.event(self, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Widget()
    form.show()
    app.exec_()