import RPi.GPIO as GPIO
import time
import math
big_arm_gpio = 18
small_arm_gpio = 23
big_arm_dir_gpio = 25
small_arm_dir_gpio = 24
base_gpio = 2
base_dir_gpio = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(big_arm_gpio, GPIO.OUT)
GPIO.setup(small_arm_gpio, GPIO.OUT)
GPIO.setup(big_arm_dir_gpio, GPIO.OUT)
GPIO.setup(small_arm_dir_gpio, GPIO.OUT)
GPIO.setup(base_gpio, GPIO.OUT)
GPIO.setup(base_dir_gpio, GPIO.OUT)

step_angle = 360/1600
motor_speed = 0.01
big_arm_angle_reset = 103
small_arm_angle_reset = -56
base_angle_reset = 0

big_arm_angle = 103
small_arm_angle = -56
base_angle = 0

big_arm_max_limit = 103
big_arm_mid_limit = 72
small_arm_max_limit = 30
small_arm_min_limit = -56

big_arm_length = 10
small_arm_length = 10
arm_coordinate_x = 0
arm_coordinate_y = 0
arm_coordinate_z = 0

def armMove(big_arm_step, small_arm_step, base_step):
    if(big_arm_step >= small_arm_step):
        step = big_arm_step - small_arm_step
        while step:
            GPIO.output(big_arm_gpio, GPIO.HIGH)
            if(small_arm_step > 0):
                GPIO.output(small_arm_gpio, GPIO.HIGH)
            time.sleep(motor_speed)
            GPIO.output(big_arm_gpio, GPIO.LOW)
            if(small_arm_step > 0):
                GPIO.output(small_arm_gpio, GPIO.LOW)
                small_arm_step -=1
            time.sleep(motor_speed)
            step -= 1
    if(big_arm_step < small_arm_step):
        step = small_arm_step - big_arm_step
        while step:
            if(big_arm_step > 0):
                GPIO.output(big_arm_gpio, GPIO.HIGH)
            GPIO.output(small_arm_gpio, GPIO.HIGH)
            time.sleep(motor_speed)
            if(big_arm_step > 0):
                GPIO.output(big_arm_gpio, GPIO.LOW)
                big_arm_step -=1
            GPIO.output(small_arm_gpio, GPIO.LOW)
            time.sleep(motor_speed)
            step -= 1
    while base_step:
        GPIO.output(base_gpio, GPIO.HIGH)
        time.sleep(motor_speed)
        GPIO.output(base_gpio, GPIO.LOW)
        time.sleep(motor_speed)
        base_step -= 1
            
def setArmAngle(big_arm_target_angle, small_arm_target_angle, base_target_angle):
    big_angle_def = 0
    small_angle_def = 0
    base_angle_def = 0
    big_arm_step = 0
    small_arm_step = 0
    base_step = 0
    log = ""
    global big_arm_angle #big arm current angle
    global small_arm_angle #small arm current angle
    global base_angle
    if(big_arm_target_angle > big_arm_max_limit):
        big_arm_target_angle = big_arm_max_limit
        log = log + "Warning:big arm out of range!\n"
    if(big_arm_angle >= big_arm_mid_limit): # 1
        if(big_arm_target_angle >= big_arm_mid_limit):# 1.1
            if(small_arm_target_angle > small_arm_max_limit):
                small_arm_target_angle = small_arm_max_limit
            if(small_arm_target_angle < small_arm_min_limit):
                small_arm_target_angle = small_arm_min_limit
                log = log + "Warning:small arm below minimun range!\n"
            if(small_arm_angle < small_arm_target_angle):   
                small_angle_def = small_arm_target_angle - small_arm_angle
                GPIO.output(small_arm_dir_gpio, 1)
                small_arm_step = small_angle_def // step_angle
                small_arm_angle += small_arm_step * step_angle
            else:
                small_angle_def = small_arm_angle - small_arm_target_angle
                GPIO.output(small_arm_dir_gpio, 0)
                small_arm_step = small_angle_def // step_angle
                small_arm_angle -= small_arm_step * step_angle
        if(big_arm_target_angle < big_arm_mid_limit):# 1.2
            small_arm_limit = small_arm_max_limit - (big_arm_mid_limit - big_arm_target_angle)
            if(small_arm_target_angle > small_arm_limit):
                    small_arm_target_angle = small_arm_limit
                    log = log + "Warning:small arm out of range!\n"
            if(small_arm_angle < small_arm_target_angle):
                small_angle_def = small_arm_target_angle - small_arm_angle
                GPIO.output(small_arm_dir_gpio, 1)
                small_arm_step = small_angle_def // step_angle
                small_arm_angle += small_arm_step * step_angle
            else:
                small_angle_def = small_arm_angle - small_arm_target_angle
                GPIO.output(small_arm_dir_gpio, 0)
                small_arm_step = small_angle_def // step_angle
                small_arm_angle -= small_arm_step * step_angle
    else:# 2
        if(small_arm_target_angle > (small_arm_max_limit - (big_arm_mid_limit - big_arm_target_angle))):
            small_arm_target_angle = small_arm_max_limit - (big_arm_mid_limit - big_arm_target_angle)
            log = log + "Warning:small arm out of range!\n"
        if(small_arm_angle > small_arm_target_angle):# 2.1
            small_angle_def = small_arm_angle - small_arm_target_angle
            GPIO.output(small_arm_dir_gpio, 0)
            small_arm_step = small_angle_def // step_angle
            small_arm_angle -= small_arm_step * step_angle
        else:# 2.2
            small_angle_def = small_arm_target_angle - small_arm_angle
            GPIO.output(small_arm_dir_gpio, 1)
            small_arm_step = small_angle_def // step_angle
            small_arm_angle += small_arm_step * step_angle
    if(big_arm_angle >= big_arm_target_angle):
        big_angle_def = big_arm_angle - big_arm_target_angle
        big_arm_step = big_angle_def // step_angle
        big_arm_angle -= big_arm_step * step_angle
        GPIO.output(big_arm_dir_gpio, 1)
    else:
        big_angle_def = big_arm_target_angle - big_arm_angle
        big_arm_step = big_angle_def // step_angle
        big_arm_angle += big_arm_step * step_angle
        GPIO.output(big_arm_dir_gpio, 0)
    if(base_target_angle >= base_angle):
        base_angle_def = base_target_angle - base_angle
        base_step = base_angle_def // step_angle
        if(base_angle_def >180):
            GPIO.output(base_dir_gpio, 0)
            base_angle -= base_step * step_angle
        else:
            GPIO.output(base_dir_gpio, 1)
            base_angle += base_step * step_angle
    else:
        base_angle_def = base_angle - base_target_angle
        base_step = base_angle_def // step_angle
        if(base_angle_def >180):
            GPIO.output(base_dir_gpio, 1)
            base_angle += base_step * step_angle
        else:
            GPIO.output(base_dir_gpio, 0)
            base_angle -= base_step * step_angle
    if(base_angle >= 360):
        base_angle = base_angle - 360
    log = log + "Succeeded!"
    return big_arm_step, small_arm_step, base_step, log

def getArmXYZ():
    global big_arm_angle
    global small_arm_angle
    global base_angle
    global arm_coordinate_x
    global arm_coordinate_y
    global arm_coordinate_z
    l = big_arm_length * math.cos(math.radians(big_arm_angle)) + small_arm_length * math.cos(math.radians(small_arm_angle))
    arm_coordinate_x = l * math.cos(math.radians(base_angle))
    arm_coordinate_y = l * math.sin(math.radians(base_angle))
    arm_coordinate_z = big_arm_length * math.sin(math.radians(big_arm_angle)) + small_arm_length * math.sin(math.radians(small_arm_angle))

def setArmXYZ(x, y, z):
    big_arm_angle_temp = math.acos((big_arm_length**2 + x**2 + y**2 + z**2 - small_arm_length**2) / (2 * big_arm_length * math.sqrt(x**2 + y**2 + z**2))) + math.atan2(z, math.sqrt(x**2 + y**2))
    small_arm_angle_temp = math.asin((z - big_arm_length * math.sin(big_arm_angle_temp)) / small_arm_length)
    base_angle_temp = math.atan2(y, x)
    return math.degrees(big_arm_angle_temp), math.degrees(small_arm_angle_temp), math.degrees(base_angle_temp)
    