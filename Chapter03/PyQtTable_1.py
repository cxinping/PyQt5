import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem )
from PyQt5.QtWidgets   import  QComboBox 

class Table(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget demo")
        self.resize(400,300);
        conLayout = QHBoxLayout()
        tableWidget=QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        conLayout.addWidget(tableWidget )
        
        tableWidget.setHorizontalHeaderLabels(['姓名','性别','体重(kg)'])  
          
        #tableWidget.verticalHeader().setVisible(False)
        #tableWidget.horizontalHeader().setVisible(False)
                        
        print( 'colCount=' + str( tableWidget.columnCount())   )
        print( 'rowCount='+ str( tableWidget.rowCount() ) )
        
        newItem = QTableWidgetItem("张三")  
        tableWidget.setItem(0, 0, newItem)  
          
        newItem = QTableWidgetItem("男")  
        tableWidget.setItem(0, 1, newItem)  
        
        comBox = QComboBox();
        comBox.addItem("男");
        comBox.addItem("女");
        tableWidget.setCellWidget(0,1,comBox);
                
        newItem = QTableWidgetItem("80")  
        tableWidget.setItem(0, 2, newItem)   
        
       
                
        self.setLayout(conLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Table()  
    example.show()   
    sys.exit(app.exec_())
