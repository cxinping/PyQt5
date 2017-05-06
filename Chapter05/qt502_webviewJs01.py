# -*- coding: utf-8 -*- 

'''
    【简介】
	QWebView中网页调用JavaScript 
  
'''


from PyQt5.QtWidgets  import QApplication , QWidget , QVBoxLayout , QPushButton
from PyQt5 import QtWebEngineWidgets
import sys


# 创建一个 application实例
app = QApplication(sys.argv)  
win = QWidget()
win.setWindowTitle('QWebView Interactive Demo')

# 创建一个垂直布局器
layout = QVBoxLayout()
win.setLayout(layout)

# 创建一个  QWebEngineView 对象
view = QtWebEngineWidgets.QWebEngineView()
view.setHtml('''
  <html>
    <head>
      <title>A Demo Page</title>

      <script language="javascript">
        // Completes the full-name control and
        // shows the submit button
        function completeAndReturnName() {
          var fname = document.getElementById('fname').value;
          var lname = document.getElementById('lname').value;
          var full = fname + ' ' + lname;

          document.getElementById('fullname').value = full;
          document.getElementById('submit-btn').style.display = 'block';

          return full;
        }
      </script>
    </head>

    <body>
      <form>
        <label for="fname">First name:</label>
        <input type="text" name="fname" id="fname"></input>
        <br />
        <label for="lname">Last name:</label>
        <input type="text" name="lname" id="lname"></input>
        <br />
        <label for="fullname">Full name:</label>
        <input disabled type="text" name="fullname" id="fullname"></input>
        <br />
        <input style="display: none;" type="submit" id="submit-btn"></input>
      </form>
    </body>
  </html>
''')

# A button to call our JavaScript
button = QPushButton('设置全名')

def js_callback(result):
    print(result)
    
def complete_name():
   view.page().runJavaScript('completeAndReturnName();', js_callback)

# Connect 'complete_name' to the button's 'clicked' signal
button.clicked.connect(complete_name)

# Add the QWebView and button to the layout
layout.addWidget(view)
layout.addWidget(button)

# Show the window and run the app
win.show()
sys.exit(app.exec_())
