# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EvaluateUI(object):
    def setupUi(self, EvaluateUI):
        EvaluateUI.setObjectName("EvaluateUI")
        EvaluateUI.resize(703, 767)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        EvaluateUI.setFont(font)
        EvaluateUI.setFocusPolicy(QtCore.Qt.TabFocus)
        EvaluateUI.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.label = QtWidgets.QLabel(EvaluateUI)
        self.label.setGeometry(QtCore.QRect(20, 440, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.dis_picture = QtWidgets.QLabel(EvaluateUI)
        self.dis_picture.setGeometry(QtCore.QRect(0, 480, 711, 281))
        self.dis_picture.setStyleSheet("background-color: rgb(226, 226, 226);")
        self.dis_picture.setText("")
        self.dis_picture.setObjectName("dis_picture")
        self.index_tab = QtWidgets.QTableWidget(EvaluateUI)
        self.index_tab.setGeometry(QtCore.QRect(10, 300, 671, 91))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(13)
        self.index_tab.setFont(font)
        self.index_tab.setShowGrid(True)
        self.index_tab.setObjectName("index_tab")
        self.index_tab.setColumnCount(7)
        self.index_tab.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.index_tab.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.index_tab.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.index_tab.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.index_tab.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.index_tab.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.index_tab.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.index_tab.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.index_tab.setHorizontalHeaderItem(6, item)
        self.index_tab.horizontalHeader().setVisible(True)
        self.index_tab.horizontalHeader().setDefaultSectionSize(95)
        self.index_tab.verticalHeader().setVisible(False)
        self.index_tab.verticalHeader().setCascadingSectionResizes(False)
        self.index_tab.verticalHeader().setDefaultSectionSize(40)
        self.index_tab.verticalHeader().setHighlightSections(True)
        self.index_tab.verticalHeader().setMinimumSectionSize(21)
        self.radio_pre = QtWidgets.QRadioButton(EvaluateUI)
        self.radio_pre.setGeometry(QtCore.QRect(140, 450, 61, 20))
        self.radio_pre.setIconSize(QtCore.QSize(11, 11))
        self.radio_pre.setObjectName("radio_pre")
        self.radio_tem = QtWidgets.QRadioButton(EvaluateUI)
        self.radio_tem.setGeometry(QtCore.QRect(220, 450, 61, 20))
        self.radio_tem.setObjectName("radio_tem")
        self.radio_moi = QtWidgets.QRadioButton(EvaluateUI)
        self.radio_moi.setGeometry(QtCore.QRect(290, 450, 51, 20))
        self.radio_moi.setObjectName("radio_moi")
        self.radio_fli = QtWidgets.QRadioButton(EvaluateUI)
        self.radio_fli.setGeometry(QtCore.QRect(430, 450, 91, 20))
        self.radio_fli.setObjectName("radio_fli")
        self.radio_TEC = QtWidgets.QRadioButton(EvaluateUI)
        self.radio_TEC.setGeometry(QtCore.QRect(360, 450, 61, 20))
        self.radio_TEC.setObjectName("radio_TEC")
        self.line = QtWidgets.QFrame(EvaluateUI)
        self.line.setGeometry(QtCore.QRect(20, 430, 661, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(EvaluateUI)
        self.label_2.setGeometry(QtCore.QRect(10, 260, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.file_info = QtWidgets.QTableWidget(EvaluateUI)
        self.file_info.setGeometry(QtCore.QRect(10, 120, 671, 91))
        self.file_info.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.file_info.setLineWidth(3)
        self.file_info.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.file_info.setShowGrid(False)
        self.file_info.setRowCount(0)
        self.file_info.setObjectName("file_info")
        self.file_info.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.file_info.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.file_info.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.file_info.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.file_info.setHorizontalHeaderItem(3, item)
        self.file_info.horizontalHeader().setVisible(True)
        self.file_info.horizontalHeader().setCascadingSectionResizes(False)
        self.file_info.horizontalHeader().setDefaultSectionSize(167)
        self.file_info.horizontalHeader().setMinimumSectionSize(28)
        self.file_info.verticalHeader().setVisible(False)
        self.file_info.verticalHeader().setDefaultSectionSize(45)
        self.file_info.verticalHeader().setMinimumSectionSize(37)
        self.scan_file = QtWidgets.QPushButton(EvaluateUI)
        self.scan_file.setGeometry(QtCore.QRect(460, 220, 93, 32))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scan_file.setFont(font)
        self.scan_file.setStyleSheet("background-color: rgb(32, 140, 255);\n"
"color: rgb(255, 255, 255);")
        self.scan_file.setObjectName("scan_file")
        self.delete_file = QtWidgets.QPushButton(EvaluateUI)
        self.delete_file.setGeometry(QtCore.QRect(590, 220, 93, 32))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.delete_file.setFont(font)
        self.delete_file.setStyleSheet("background-color: rgb(32, 140, 255);\n"
"color: rgb(255, 255, 255);")
        self.delete_file.setObjectName("delete_file")
        self.line_2 = QtWidgets.QFrame(EvaluateUI)
        self.line_2.setGeometry(QtCore.QRect(20, 250, 661, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.comfirm_evaluate = QtWidgets.QPushButton(EvaluateUI)
        self.comfirm_evaluate.setGeometry(QtCore.QRect(460, 400, 93, 32))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comfirm_evaluate.setFont(font)
        self.comfirm_evaluate.setStyleSheet("background-color: rgb(32, 140, 255);\n"
"color: rgb(255, 255, 255);")
        self.comfirm_evaluate.setObjectName("comfirm_evaluate")
        self.cancel_evaluate = QtWidgets.QPushButton(EvaluateUI)
        self.cancel_evaluate.setGeometry(QtCore.QRect(590, 400, 93, 32))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_evaluate.setFont(font)
        self.cancel_evaluate.setStyleSheet("background-color: rgb(32, 140, 255);\n"
"color: rgb(255, 255, 255);")
        self.cancel_evaluate.setObjectName("cancel_evaluate")
        self.label_3 = QtWidgets.QLabel(EvaluateUI)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.widget = QtWidgets.QWidget(EvaluateUI)
        self.widget.setGeometry(QtCore.QRect(0, 0, 701, 81))
        self.widget.setStyleSheet("background-color: rgb(32, 140, 255);")
        self.widget.setObjectName("widget")
        self.btn_com = QtWidgets.QPushButton(self.widget)
        self.btn_com.setGeometry(QtCore.QRect(20, 0, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_com.setFont(font)
        self.btn_com.setStyleSheet("border-radius:100px;")
        self.btn_com.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/10.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_com.setIcon(icon)
        self.btn_com.setIconSize(QtCore.QSize(50, 50))
        self.btn_com.setAutoRepeat(False)
        self.btn_com.setObjectName("btn_com")
        self.btn_dis = QtWidgets.QPushButton(self.widget)
        self.btn_dis.setGeometry(QtCore.QRect(120, 0, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_dis.setFont(font)
        self.btn_dis.setStyleSheet("border-radius:100px;")
        self.btn_dis.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/image/11.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_dis.setIcon(icon1)
        self.btn_dis.setIconSize(QtCore.QSize(50, 50))
        self.btn_dis.setObjectName("btn_dis")
        self.btn_eva = QtWidgets.QPushButton(self.widget)
        self.btn_eva.setGeometry(QtCore.QRect(220, 0, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_eva.setFont(font)
        self.btn_eva.setStyleSheet("border-radius:100px;")
        self.btn_eva.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/image/12.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_eva.setIcon(icon2)
        self.btn_eva.setIconSize(QtCore.QSize(50, 50))
        self.btn_eva.setAutoRepeat(False)
        self.btn_eva.setObjectName("btn_eva")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(10, 50, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"background：transparent；")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(110, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"background：transparent；")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(210, 50, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"background：transparent；")
        self.label_9.setObjectName("label_9")

        self.retranslateUi(EvaluateUI)
        self.scan_file.clicked.connect(EvaluateUI.select_evafile)
        self.delete_file.clicked.connect(EvaluateUI.delete_evafile)
        self.radio_pre.clicked.connect(EvaluateUI.handle_type)
        self.radio_tem.clicked.connect(EvaluateUI.handle_type)
        self.radio_moi.clicked.connect(EvaluateUI.handle_type)
        self.radio_TEC.clicked.connect(EvaluateUI.handle_type)
        self.radio_fli.clicked.connect(EvaluateUI.handle_type)
        self.comfirm_evaluate.clicked.connect(EvaluateUI.comfirm_evaluate)
        self.cancel_evaluate.clicked.connect(EvaluateUI.cancel_evaluate)
        self.btn_com.clicked.connect(EvaluateUI.to_comUI)
        self.btn_dis.clicked.connect(EvaluateUI.to_decomUI)
        QtCore.QMetaObject.connectSlotsByName(EvaluateUI)

    def retranslateUi(self, EvaluateUI):
        _translate = QtCore.QCoreApplication.translate
        EvaluateUI.setWindowTitle(_translate("EvaluateUI", "评估界面"))
        self.label.setText(_translate("EvaluateUI", "请选择维度："))
        item = self.index_tab.verticalHeaderItem(0)
        item.setText(_translate("EvaluateUI", "1"))
        item = self.index_tab.horizontalHeaderItem(0)
        item.setText(_translate("EvaluateUI", "元素缺失率"))
        item = self.index_tab.horizontalHeaderItem(1)
        item.setText(_translate("EvaluateUI", "记录缺失率"))
        item = self.index_tab.horizontalHeaderItem(2)
        item.setText(_translate("EvaluateUI", "时间违法率"))
        item = self.index_tab.horizontalHeaderItem(3)
        item.setText(_translate("EvaluateUI", "数据越界率"))
        item = self.index_tab.horizontalHeaderItem(4)
        item.setText(_translate("EvaluateUI", "离群值率"))
        item = self.index_tab.horizontalHeaderItem(5)
        item.setText(_translate("EvaluateUI", "毛刺异常率"))
        item = self.index_tab.horizontalHeaderItem(6)
        item.setText(_translate("EvaluateUI", "等级偏移率"))
        self.radio_pre.setText(_translate("EvaluateUI", "压强"))
        self.radio_tem.setText(_translate("EvaluateUI", "温度"))
        self.radio_moi.setText(_translate("EvaluateUI", "湿度"))
        self.radio_fli.setText(_translate("EvaluateUI", "闪烁指数"))
        self.radio_TEC.setText(_translate("EvaluateUI", "TEC"))
        self.label_2.setText(_translate("EvaluateUI", "评估指标："))
        item = self.file_info.horizontalHeaderItem(0)
        item.setText(_translate("EvaluateUI", "名称"))
        item = self.file_info.horizontalHeaderItem(1)
        item.setText(_translate("EvaluateUI", "大小"))
        item = self.file_info.horizontalHeaderItem(2)
        item.setText(_translate("EvaluateUI", "路径"))
        item = self.file_info.horizontalHeaderItem(3)
        item.setText(_translate("EvaluateUI", "修改时间"))
        self.scan_file.setText(_translate("EvaluateUI", "添加"))
        self.delete_file.setText(_translate("EvaluateUI", "删除"))
        self.comfirm_evaluate.setText(_translate("EvaluateUI", "确定评估"))
        self.cancel_evaluate.setText(_translate("EvaluateUI", "取消评估"))
        self.label_3.setText(_translate("EvaluateUI", "选择评估文件："))
        self.label_7.setText(_translate("EvaluateUI", "  压缩文件"))
        self.label_8.setText(_translate("EvaluateUI", "解压缩文件"))
        self.label_9.setText(_translate("EvaluateUI", "  质量评估"))

from dcmp import picture_rc
