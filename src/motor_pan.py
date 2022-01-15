#!/usr/bin/python2.7

import rospy
from std_msgs.msg import Float32
import imp
import rospkg

rospack = rospkg.RosPack()
pck_path = rospack.get_path('bike_sentry')

CDM = imp.load_source('module.name', pck_path + '/scripts/CameraDataManager.py')
MM = imp.load_source('module.name', pck_path + '/scripts/MotorManager.py')

STEPS = 0

CameraDataManager = CDM.CameraDataManager(1280, 720)
Motor = MM.MotorManager(STEPS)

def listener_x():
    rospy.Subscriber("x_center", Float32, pan_callback)

def pan_callback(pixels_x):

    x = int(pixels_x.data)
    instr = CameraDataManager.create_motor_instructions_pan(x) 

    movement = Motor.actuate(instr)
    rospy.loginfo("x_center: {}   direction:{}".format(x, movement))

def main():
    rospy.init_node("motor_pan")
    listener_x()
    rospy.spin()

if __name__ == "__main__":
    main()