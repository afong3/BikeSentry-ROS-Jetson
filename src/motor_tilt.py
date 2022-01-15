#!/usr/bin/python2.7

# Written by Adam Fong
# January 2022
# Node which controls the tilt motor

import rospy
from std_msgs.msg import Float32
import imp
import os

curr_dir = os.path.abspath(os.getcwd()) #'/home/sentry/catkin_ws/src/BikeSentryROS/src
rospy.loginfo(curr_dir)
repositry_root = curr_dir.split("/BikeSentryROS",1)[0]
rospy.loginfo(repositry_root)
lib_path = repositry_root + "/BikeSentryROS/scripts"
rospy.loginfo(lib_path)

CDM = imp.load_source('module.name', lib_path + '/CameraDataManager.py')
MM = imp.load_source('module.name', lib_path + '/MotorManager.py')

STEPS = 0

CameraDataManager = CDM.CameraDataManager(1280, 720)
Motor = MM.MotorManager(STEPS)

def listener_y():
    rospy.Subscriber("y_center", Float32, tilt_callback)
    
def tilt_callback(pixels_y):
    y = int(pixels_y.data)
    rospy.loginfo("y_center: {}".format(y))
    
    instr = CameraDataManager.create_motor_instructions_tilt(y) 

    Motor.actuate(instr)


def main():
    rospy.init_node("motor_tilt")
    listener_y()
    rospy.spin()

if __name__ == "__main__":
    main()