# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(749, 377)
        Form.setAutoFillBackground(True)
        self.btn_restart = QtWidgets.QPushButton(Form)
        self.btn_restart.setGeometry(QtCore.QRect(10, 12, 81, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.btn_restart.setFont(font)
        self.btn_restart.setObjectName("btn_restart")
        self.lst_item = QtWidgets.QListView(Form)
        self.lst_item.setGeometry(QtCore.QRect(10, 220, 211, 151))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lst_item.setFont(font)
        self.lst_item.setObjectName("lst_item")
        self.btn_map1 = QtWidgets.QPushButton(Form)
        self.btn_map1.setGeometry(QtCore.QRect(430, 70, 81, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.btn_map1.setFont(font)
        self.btn_map1.setObjectName("btn_map1")
        self.btn_map2 = QtWidgets.QPushButton(Form)
        self.btn_map2.setGeometry(QtCore.QRect(430, 150, 81, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.btn_map2.setFont(font)
        self.btn_map2.setObjectName("btn_map2")
        self.btn_map3 = QtWidgets.QPushButton(Form)
        self.btn_map3.setGeometry(QtCore.QRect(430, 240, 81, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.btn_map3.setFont(font)
        self.btn_map3.setObjectName("btn_map3")
        self.lst_sub_map = QtWidgets.QListView(Form)
        self.lst_sub_map.setGeometry(QtCore.QRect(520, 60, 221, 311))
        self.lst_sub_map.setObjectName("lst_sub_map")
        self.lst_skill = QtWidgets.QListView(Form)
        self.lst_skill.setGeometry(QtCore.QRect(220, 60, 201, 311))
        self.lst_skill.setObjectName("lst_skill")
        self.lbl_time = QtWidgets.QLabel(Form)
        self.lbl_time.setGeometry(QtCore.QRect(620, 20, 121, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.lbl_time.setFont(font)
        self.lbl_time.setObjectName("lbl_time")
        self.lst_property = QtWidgets.QListView(Form)
        self.lst_property.setEnabled(True)
        self.lst_property.setGeometry(QtCore.QRect(10, 60, 211, 161))
        font = QtGui.QFont()
        font.setFamily("华文琥珀")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lst_property.setFont(font)
        self.lst_property.setMouseTracking(False)
        self.lst_property.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lst_property.setAutoFillBackground(False)
        self.lst_property.setAlternatingRowColors(False)
        self.lst_property.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.lst_property.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.lst_property.setObjectName("lst_property")
        self.btn_test_1 = QtWidgets.QPushButton(Form)
        self.btn_test_1.setGeometry(QtCore.QRect(130, 10, 81, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.btn_test_1.setFont(font)
        self.btn_test_1.setObjectName("btn_test_1")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "神秘修炼"))
        self.btn_restart.setText(_translate("Form", "重头来过"))
        self.btn_map1.setText(_translate("Form", "树林"))
        self.btn_map2.setText(_translate("Form", "山地"))
        self.btn_map3.setText(_translate("Form", "洞穴"))
        self.lbl_time.setText(_translate("Form", "修炼时间："))
        self.btn_test_1.setText(_translate("Form", "测试专用"))

