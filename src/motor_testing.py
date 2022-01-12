#!/usr/bin/python2.7

# Written by Adam Fong
# January 2022
# Run this node with motors attached to Jetson Nano to 

import tf2_ros
import rospy
from std_msgs.msg import String 
import threading
import imp

# importing MotorManager library
MotorManager = imp.load_source('module.name', '../scripts/MotorManager.py')

STEP_COUNT = 360 #TODO: replace with true step count

def test_motor_pan_node(event=None):
    rospy.init_node("motor_pan")
    motor_pan = MotorManager.MotorManager(STEP_COUNT)

    rate = rospy.Rate(1) # 1 Hz
    
    # test by having motor rotate both directions with all instructions
    motor_pan.actuate("left")
    rospy.sleep()
    motor_pan.actuate("up")
    rospy.sleep()
    motor_pan.actuate("right")
    rospy.sleep()
    motor_pan.actuate("down")
    rospy.sleep()
    motor_pan.actuate("none")

def test_motor_tilt_node(event=None):
    rospy.init_node("motor_tilt")
    motor_tilt = MotorManager.MotorManager(STEP_COUNT)

    rate = rospy.Rate(1) # 1 Hz
    
    # test by having motor rotate both directions with all instructions
    motor_tilt.actuate("left")
    rospy.sleep()
    motor_tilt.actuate("up")
    rospy.sleep()
    motor_tilt.actuate("right")
    rospy.sleep()
    motor_tilt.actuate("down")
    rospy.sleep()
    motor_tilt.actuate("none")

def main():
    
    thread_pan = threading.Thread(target = test_motor_pan_node)
    thread_tilt = threading.Thread(target = test_motor_tilt_node)  

    thread_pan.start()
    thread_tilt.start()

    rospy.spin()


if __name__ == "__main__":
    main()


