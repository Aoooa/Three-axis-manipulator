# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(639, 447)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 6, 61, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 46, 71, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 86, 61, 31))
        self.label_3.setObjectName("label_3")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(70, 140, 121, 16))
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setPageStep(10)
        self.horizontalSlider.setProperty("value", 50)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 41, 31))
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(50, 130, 118, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 330, 16, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 290, 16, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 250, 16, 31))
        self.label_7.setObjectName("label_7")
        self.horizontalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(70, 380, 121, 16))
        self.horizontalSlider_3.setMaximum(100)
        self.horizontalSlider_3.setProperty("value", 50)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 370, 41, 31))
        self.label_8.setObjectName("label_8")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(50, 370, 118, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 190, 231, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(220, 0, 20, 391))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(520, 340, 51, 41))
        self.pushButton_13.setStyleSheet("Background-color:rgb(239, 41, 41)")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(290, 150, 89, 25))
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(280, 10, 21, 31))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(330, 10, 31, 31))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(380, 10, 31, 31))
        self.label_11.setObjectName("label_11")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(290, 100, 89, 25))
        self.pushButton_14.setObjectName("pushButton_14")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(270, 40, 41, 25))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(320, 40, 41, 25))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(370, 40, 41, 25))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(140, 240, 81, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_2.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_2.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_2.addWidget(self.lineEdit_6)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(230, 120, 221, 21))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(230, 190, 221, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(450, 30, 191, 281))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(200, 370, 31, 31))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(200, 130, 31, 31))
        self.label_13.setObjectName("label_13")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(140, 0, 81, 131))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(10, 160, 41, 31))
        self.label_14.setObjectName("label_14")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(70, 170, 121, 16))
        self.horizontalSlider_2.setMinimum(1)
        self.horizontalSlider_2.setMaximum(10)
        self.horizontalSlider_2.setProperty("value", 1)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(200, 160, 31, 31))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(510, 0, 65, 31))
        self.label_16.setObjectName("label_16")
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(80, 10, 21, 111))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(110, 10, 21, 111))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_4.addWidget(self.pushButton_4)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_4.addWidget(self.pushButton_6)
        self.layoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(80, 250, 21, 111))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_5.addWidget(self.pushButton_7)
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_5.addWidget(self.pushButton_9)
        self.pushButton_11 = QtWidgets.QPushButton(self.layoutWidget4)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_5.addWidget(self.pushButton_11)
        self.layoutWidget5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget5.setGeometry(QtCore.QRect(110, 250, 21, 111))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget5)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_6.addWidget(self.pushButton_8)
        self.pushButton_10 = QtWidgets.QPushButton(self.layoutWidget5)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_6.addWidget(self.pushButton_10)
        self.pushButton_12 = QtWidgets.QPushButton(self.layoutWidget5)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_6.addWidget(self.pushButton_12)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(360, 240, 81, 131))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_7.addWidget(self.lineEdit_10)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout_7.addWidget(self.lineEdit_11)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout_7.addWidget(self.lineEdit_12)
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(299, 250, 21, 111))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pushButton_16 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_16.setObjectName("pushButton_16")
        self.verticalLayout_8.addWidget(self.pushButton_16)
        self.pushButton_18 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_18.setObjectName("pushButton_18")
        self.verticalLayout_8.addWidget(self.pushButton_18)
        self.pushButton_22 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_22.setObjectName("pushButton_22")
        self.verticalLayout_8.addWidget(self.pushButton_22)
        self.layoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(330, 250, 20, 111))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pushButton_17 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.pushButton_17.setObjectName("pushButton_17")
        self.verticalLayout_9.addWidget(self.pushButton_17)
        self.pushButton_20 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.pushButton_20.setObjectName("pushButton_20")
        self.verticalLayout_9.addWidget(self.pushButton_20)
        self.pushButton_21 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.pushButton_21.setObjectName("pushButton_21")
        self.verticalLayout_9.addWidget(self.pushButton_21)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(240, 330, 16, 31))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(240, 250, 16, 31))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(240, 290, 16, 31))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(240, 370, 41, 31))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(430, 370, 31, 31))
        self.label_21.setObjectName("label_21")
        self.horizontalSlider_4 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_4.setGeometry(QtCore.QRect(300, 380, 121, 16))
        self.horizontalSlider_4.setMaximum(100)
        self.horizontalSlider_4.setProperty("value", 50)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(50, 210, 111, 17))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(250, 210, 161, 17))
        self.label_23.setObjectName("label_23")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(440, 0, 20, 391))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(490, 320, 118, 3))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 639, 28))
        self.menubar.setObjectName("menubar")
        self.menuMainWindow = QtWidgets.QMenu(self.menubar)
        self.menuMainWindow.setObjectName("menuMainWindow")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMainWindow.menuAction())

        self.retranslateUi(MainWindow)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mechine Arm by chenjb"))
        self.label.setText(_translate("MainWindow", "Big arm"))
        self.label_2.setText(_translate("MainWindow", "Small arm"))
        self.label_3.setText(_translate("MainWindow", "Base"))
        self.label_4.setText(_translate("MainWindow", "Zoom"))
        self.label_5.setText(_translate("MainWindow", "Z"))
        self.label_6.setText(_translate("MainWindow", "Y"))
        self.label_7.setText(_translate("MainWindow", "X"))
        self.label_8.setText(_translate("MainWindow", "Zoom"))
        self.pushButton_13.setText(_translate("MainWindow", "X"))
        self.pushButton_15.setText(_translate("MainWindow", "Reset"))
        self.label_9.setText(_translate("MainWindow", "X"))
        self.label_10.setText(_translate("MainWindow", "Y"))
        self.label_11.setText(_translate("MainWindow", "Z"))
        self.pushButton_14.setText(_translate("MainWindow", "calibration"))
        self.lineEdit_7.setText(_translate("MainWindow", "0"))
        self.lineEdit_8.setText(_translate("MainWindow", "0"))
        self.lineEdit_9.setText(_translate("MainWindow", "0"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:3pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "5"))
        self.label_13.setText(_translate("MainWindow", "5"))
        self.label_14.setText(_translate("MainWindow", "Speed"))
        self.label_15.setText(_translate("MainWindow", "1"))
        self.label_16.setText(_translate("MainWindow", "Messege"))
        self.pushButton.setText(_translate("MainWindow", "+"))
        self.pushButton_3.setText(_translate("MainWindow", "+"))
        self.pushButton_5.setText(_translate("MainWindow", "+"))
        self.pushButton_2.setText(_translate("MainWindow", "-"))
        self.pushButton_4.setText(_translate("MainWindow", "-"))
        self.pushButton_6.setText(_translate("MainWindow", "-"))
        self.pushButton_7.setText(_translate("MainWindow", "+"))
        self.pushButton_9.setText(_translate("MainWindow", "+"))
        self.pushButton_11.setText(_translate("MainWindow", "+"))
        self.pushButton_8.setText(_translate("MainWindow", "-"))
        self.pushButton_10.setText(_translate("MainWindow", "-"))
        self.pushButton_12.setText(_translate("MainWindow", "-"))
        self.pushButton_16.setText(_translate("MainWindow", "+"))
        self.pushButton_18.setText(_translate("MainWindow", "+"))
        self.pushButton_22.setText(_translate("MainWindow", "+"))
        self.pushButton_17.setText(_translate("MainWindow", "-"))
        self.pushButton_20.setText(_translate("MainWindow", "-"))
        self.pushButton_21.setText(_translate("MainWindow", "-"))
        self.label_17.setText(_translate("MainWindow", "Z"))
        self.label_18.setText(_translate("MainWindow", "X"))
        self.label_19.setText(_translate("MainWindow", "Y"))
        self.label_20.setText(_translate("MainWindow", "Zoom"))
        self.label_21.setText(_translate("MainWindow", "5"))
        self.label_22.setText(_translate("MainWindow", "Arm Coordinate"))
        self.label_23.setText(_translate("MainWindow", "Workpiece coordinates"))
        self.menuMainWindow.setTitle(_translate("MainWindow", "Mechine Arm"))