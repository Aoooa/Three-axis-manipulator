from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from functools import partial
from myui import Ui_MainWindow

import motor_control as arm
import sys
import string

zoom_angle_para = 5
zoom_xyz_para = 5

class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def  __init__ (self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.lineEdit.setText(str(arm.big_arm_angle))
        self.lineEdit_2.setText(str(arm.small_arm_angle))
        self.lineEdit_3.setText(str(arm.base_angle))
        
def log(mes):
    ui.textBrowser.append(mes)
    ui.textBrowser.moveCursor(ui.textBrowser.textCursor().End)

def arm_angle_reset():
    log("Reset!")
    arm.big_arm_angle = arm.big_arm_angle_reset;
    arm.small_arm_angle = arm.small_arm_angle_reset;
    arm.base_angle = arm.base_angle_reset;

def flashNum():
    ui.lineEdit.setText(str(round(arm.big_arm_angle, 2)))
    ui.lineEdit_2.setText(str(round(arm.small_arm_angle, 2)))
    ui.lineEdit_3.setText(str(round(arm.base_angle, 2)))
    ui.lineEdit_4.setText(str(round(arm.arm_coordinate_x, 2)))
    ui.lineEdit_5.setText(str(round(arm.arm_coordinate_y, 2)))
    ui.lineEdit_6.setText(str(round(arm.arm_coordinate_z, 2)))
    
def setAngle(id):
    if(id == 1):
        big_arm_step, small_arm_step, base_step, mes = arm.setArmAngle(arm.big_arm_angle + zoom_angle_para, arm.small_arm_angle, arm.base_angle)
    elif(id == 2):
        big_arm_step, small_arm_step, base_step, mes = arm.setArmAngle(arm.big_arm_angle - zoom_angle_para, arm.small_arm_angle, arm.base_angle)
    elif(id == 3):
        big_arm_step, small_arm_step, base_step, mes = arm.setArmAngle(arm.big_arm_angle, arm.small_arm_angle + zoom_angle_para, arm.base_angle)
    elif(id == 4):
        big_arm_step, small_arm_step, base_step, mes = arm.setArmAngle(arm.big_arm_angle, arm.small_arm_angle - zoom_angle_para, arm.base_angle)
    elif(id == 5):
        big_arm_step, small_arm_step, base_step, mes = arm.setArmAngle(arm.big_arm_angle, arm.small_arm_angle, arm.base_angle + zoom_angle_para)
    elif(id == 6):
        big_arm_step, small_arm_step, base_step, mes = arm.setArmAngle(arm.big_arm_angle, arm.small_arm_angle, arm.base_angle - zoom_angle_para)
    log(mes)
    arm.getArmXYZ()
    flashNum()
        
def setXYZ(id):
    log("set XY")

def inputAngle():
    arm.setArmAngle(float(ui.lineEdit.text()), float(ui.lineEdit_2.text()), float(ui.lineEdit_3.text()))
    arm.getArmXYZ()
    flashNum()
  
def inputXYZ():
    big_arm_angle_temp, small_arm_angle_temp, base_angle_temp = arm.setArmXYZ(float(ui.lineEdit_4.text()), float(ui.lineEdit_5.text()), float(ui.lineEdit_6.text()))
    arm.setArmAngle(big_arm_angle_temp, small_arm_angle_temp, base_angle_temp)
    
def reset():
    print("reset")
    
def adsorbent():
    print("adsorbent")
    
def setAngleZoom(value):
    global zoom_angle_para
    zoom_angle_para =  value / 10
    ui.label_13.setText(str(zoom_angle_para))
    
def setXYZZoom(value):
    global zoom_xyz_para  
    zoom_xyz_para =  value / 10
    ui.label_12.setText(str(zoom_xyz_para))

def setSpeed(value):
    print(value)
    ui.label_15.setText(str(value))
    
def setCalibration():
    print("calibration")

def inputCalibrationXYZ():
    print("")

app=QtWidgets.QApplication(sys.argv)
ui = mywindow()
log("Start")
arm_angle_reset()
arm.getArmXYZ()
flashNum()
ui.show()
ui.lineEdit.editingFinished.connect(inputAngle) # type: ignore
ui.lineEdit_2.editingFinished.connect(inputAngle) # type: ignore
ui.lineEdit_3.editingFinished.connect(inputAngle) # type: ignore
ui.horizontalSlider.valueChanged[int].connect(setAngleZoom) # type: ignore
ui.horizontalSlider_2.valueChanged[int].connect(setSpeed) # type: ignore
ui.horizontalSlider_3.valueChanged[int].connect(setXYZZoom) # type: ignore
ui.pushButton.clicked.connect(partial(setAngle, 1)) # type: ignore
ui.pushButton_3.clicked.connect(partial(setAngle, 3)) # type: ignore
ui.pushButton_5.clicked.connect(partial(setAngle, 5)) # type: ignore
ui.pushButton_2.clicked.connect(partial(setAngle, 2)) # type: ignore
ui.pushButton_4.clicked.connect(partial(setAngle, 4)) # type: ignore
ui.pushButton_6.clicked.connect(partial(setAngle, 6)) # type: ignore
ui.pushButton_7.clicked.connect(partial(setXYZ, 7)) # type: ignore
ui.pushButton_9.clicked.connect(partial(setXYZ, 9)) # type: ignore
ui.pushButton_11.clicked.connect(partial(setXYZ, 11)) # type: ignore
ui.pushButton_8.clicked.connect(partial(setXYZ, 8)) # type: ignore
ui.pushButton_10.clicked.connect(partial(setXYZ, 10)) # type: ignore
ui.pushButton_12.clicked.connect(partial(setXYZ, 12)) # type: ignore
ui.lineEdit_4.editingFinished.connect(inputXYZ) # type: ignore
ui.lineEdit_5.editingFinished.connect(inputXYZ) # type: ignore
ui.lineEdit_6.editingFinished.connect(inputXYZ) # type: ignore
ui.lineEdit_7.editingFinished.connect(inputCalibrationXYZ) # type: ignore
ui.lineEdit_8.editingFinished.connect(inputCalibrationXYZ) # type: ignore
ui.lineEdit_9.editingFinished.connect(inputCalibrationXYZ) # type: ignore
ui.pushButton_13.clicked.connect(setCalibration) # type: ignore
ui.pushButton_14.clicked.connect(reset) # type: ignore
sys.exit(app.exec_())



