# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\maybe\Desktop\软件体系结构\addLink.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddLink(object):
    def setupUi(self, AddLink):
        AddLink.setObjectName("AddLink")
        AddLink.resize(400, 300)
        AddLink.setMaximumSize(QtCore.QSize(400, 300))
        self.verticalLayout = QtWidgets.QVBoxLayout(AddLink)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(AddLink)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(AddLink)
        self.lineEdit.setMinimumSize(QtCore.QSize(100, 18))
        self.lineEdit.setMaximumSize(QtCore.QSize(100, 18))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(AddLink)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(AddLink)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(100, 18))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(100, 18))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.yes = QtWidgets.QPushButton(AddLink)
        self.yes.setObjectName("yes")
        self.horizontalLayout_3.addWidget(self.yes)
        self.pushButton_2 = QtWidgets.QPushButton(AddLink)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(AddLink)
        self.pushButton_2.clicked.connect(AddLink.close)
        QtCore.QMetaObject.connectSlotsByName(AddLink)

    def retranslateUi(self, AddLink):
        _translate = QtCore.QCoreApplication.translate
        AddLink.setWindowTitle(_translate("AddLink", "Dialog"))
        self.label.setText(_translate("AddLink", "请输入联系人："))
        self.label_2.setText(_translate("AddLink", "请输入电话号码："))
        self.yes.setText(_translate("AddLink", "确认"))
        self.pushButton_2.setText(_translate("AddLink", "取消"))
