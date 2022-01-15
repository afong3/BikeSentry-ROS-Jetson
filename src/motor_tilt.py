#!/usr/bin/python2.7

# Written by Adam Fong
# January 2022
# Node which controls the tilt motor

import rospy
from std_msgs.msg import Float32
import imp

STEPS = 0

CDM = imp.load_source('module.name', '../scripts/CameraDataManager.py')
MM = imp.load_source('module.name', '../scripts/MotorManager.py')

CameraDataManager = CDM.CameraDataManager(1280, 720)
Motor = MM.MotorManager(STEPS)

def listener_y():
    rospy.Subscriber("y_center", Float32, tilt_callback)

def tilt_callback(pixels_y):

    y = int(pixels_y.data)
    
    instr = CameraDataManager.create_motor_instructions_tilt(y) 

    Motor.actuate(instr)


def main():
    rospy.init_node("motor_tilt")
    listener_y()
    rospy.spin()

if __name__ == "__main__":
    main()