# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\maybe\Desktop\软件体系结构\link.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowOpacity(0.9)
        MainWindow.resize(815, 396)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.linkList = QtWidgets.QTableWidget(self.centralwidget)
        self.linkList.setMinimumSize(QtCore.QSize(500, 250))
        self.linkList.setMaximumSize(QtCore.QSize(500, 250))
        self.linkList.setObjectName("linkList")
        self.linkList.setColumnCount(2)
        self.linkList.setRowCount(1)
        self.linkList.setHorizontalHeaderLabels(["姓名","联系方式"])
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.linkList)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Save = QtWidgets.QPushButton(self.centralwidget)
        self.Save.setMinimumSize(QtCore.QSize(100, 50))
        self.Save.setObjectName("Save")
        self.gridLayout.addWidget(self.Save, 2, 0, 1, 1)
        self.closeWinBtn = QtWidgets.QPushButton(self.centralwidget)
        self.closeWinBtn.setMinimumSize(QtCore.QSize(100, 50))
        self.closeWinBtn.setObjectName("closeWinBtn")
        self.gridLayout.addWidget(self.closeWinBtn, 3, 0, 1, 1)
        self.addLink = QtWidgets.QPushButton(self.centralwidget)
        self.addLink.setMinimumSize(QtCore.QSize(100, 50))
        self.addLink.setObjectName("addLink")
        self.gridLayout.addWidget(self.addLink, 0, 0, 1, 1)
        self.deleteLink = QtWidgets.QPushButton(self.centralwidget)
        self.deleteLink.setMinimumSize(QtCore.QSize(100, 50))
        self.deleteLink.setObjectName("deleteLink")
        self.gridLayout.addWidget(self.deleteLink, 1, 0, 1, 1)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 815, 23))
        self.menubar.setObjectName("menubar")
        self.menuLink = QtWidgets.QMenu(self.menubar)
        self.menuLink.setObjectName("menuLink")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuLink.menuAction())

        self.retranslateUi(MainWindow)
        self.closeWinBtn.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Save.setText(_translate("MainWindow", "查找联系人"))
        self.closeWinBtn.setText(_translate("MainWindow", "退出"))
        self.addLink.setText(_translate("MainWindow", "添加联系人"))
        self.deleteLink.setText(_translate("MainWindow", "删除联系人"))
        self.menuLink.setTitle(_translate("MainWindow", "Link"))
