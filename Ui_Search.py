# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\maybe\Desktop\软件体系结构\Search.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(430, 334)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMaximumSize(QtCore.QSize(50, 20))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.SearchText = QtWidgets.QLineEdit(Dialog)
        self.SearchText.setMaximumSize(QtCore.QSize(200, 20))
        self.SearchText.setObjectName("SearchText")
        self.horizontalLayout_3.addWidget(self.SearchText)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(1)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SearchButton = QtWidgets.QPushButton(Dialog)
        self.SearchButton.setMaximumSize(QtCore.QSize(50, 20))
        self.SearchButton.setObjectName("SearchButton")
        self.horizontalLayout_2.addWidget(self.SearchButton)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setMaximumSize(QtCore.QSize(50, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        self.pushButton_2.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "查询姓名"))
        self.SearchButton.setText(_translate("Dialog", "查询"))
        self.pushButton_2.setText(_translate("Dialog", "取消"))
