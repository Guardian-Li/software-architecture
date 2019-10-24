#from PyQt5 import QtCore, QtGui, QtWidgets,QMainWindow,QApplication
import sys
from Ui_link import *
from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QTableWidgetItem,QDialog
from PyQt5.QtCore import pyqtSignal
import pymysql
import pysql
from Ui_addLink import *
from Ui_Search import * 


'''
database phone
table link
no.1 name
no.2 phone_number
'''



class MyMainWindow(QMainWindow,Ui_MainWindow):


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.phone = pysql.phone()
        phonelist = self.phone.phoneListShow()
        self.linkList.setRowCount(len(phonelist))
        row = 0
        for x in phonelist:
            itName = QTableWidgetItem(x[0])
            itNum = QTableWidgetItem(x[1])
            self.linkList.setItem(row,0,itName)
            self.linkList.setItem(row,1,itNum)
            row = row + 1
        self.phone.closeSql()
        

    



class addLink(QDialog,Ui_AddLink):
    
    def __init__(self):
        QDialog.__init__(self)
        
        self.setupUi(self)
        btn1 = self.yes
        btn1.clicked.connect(lambda: self.sendMessage(self.lineEdit.text(),self.lineEdit_2.text()))

    
    def sendMessage(self,name,number):

        phone = pysql.phone()
        if name != None and number != None:
            phone.insert(name,number)
        phone.closeSql()
        self.close()
        
    
class deleteLink(QDialog,Ui_AddLink):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        btn1 = self.yes
        btn1.clicked.connect(lambda: self.deleteOneLink(self.lineEdit.text(),self.lineEdit_2.text()))


    def deleteOneLink(self,name = None,number = None):
        phone = pysql.phone()
        if name!= None and number != None:
            phone.deleteLink(name,number)
        phone.closeSql()
        self.close()


class SearchLink(QDialog, Ui_Dialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        btn = self.SearchButton
        btn.clicked.connect(lambda : self.search(self.SearchText.text()))


    def search(self,name = None):


        phone = pysql.phone()
        x = phone.search(name)
        '''
        查找返回值可能为None
        如果None情况下会发生访问X[0] X[1]错误
        '''
        if x != None:
            itName = QTableWidgetItem(x[0])
            itNum = QTableWidgetItem(x[1])
            self.tableWidget.setItem(0,0,itName)
            self.tableWidget.setItem(0,1,itNum)
    
        
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = MyMainWindow()
    a = addLink()
    b = deleteLink()
    
    btn = demo.addLink
    btn.clicked.connect(a.show)
    btn2 = demo.deleteLink
    btn2.clicked.connect(b.show)
    c = SearchLink()
    btn3 = demo.Save
    btn3.clicked.connect(c.show)
    demo.show()
    sys.exit(app.exec_())
    
    
