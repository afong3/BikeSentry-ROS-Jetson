#!/usr/bin/python2.7

import rospy
from std_msgs.msg import Float32
import imp

STEPS = 0

CDM = imp.load_source('module.name', '/home/sentry/catkin_ws/src/BikeSentryROS/scripts/CameraDataManager.py')
MM = imp.load_source('module.name', '/home/sentry/catkin_ws/src/BikeSentryROS/scripts/MotorManager.py')

CameraDataManager = CDM.CameraDataManager(1280, 720)
Motor = MM.MotorManager(STEPS)

def listener_x():
    rospy.Subscriber("x_center", Float32, pan_callback)

def pan_callback(pixels_x):

    x = int(pixels_x.data)
    rospy.loginfo("x center: {}".format(x))
    instr = CameraDataManager.create_motor_instructions_pan(x) 

    Motor.actuate(instr)


def main():
    rospy.init_node("motor_pan")
    listener_x()
    rospy.spin()

if __name__ == "__main__":
    main()