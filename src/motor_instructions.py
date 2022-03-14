#!/usr/bin/python2.7

import rospy
from std_msgs.msg import Empty, Float32
import imp
import rospkg

rospack = rospkg.RosPack()
pck_path = rospack.get_path("bike_sentry")

CDM = imp.load_source("module.name", pck_path + "/scripts/CameraDataManager.py")


class MotorInstructionHandler:
    def __init__(self):
        pass

    def init_publishers(self):
        self.up_pub = rospy.Publisher("go_up", Empty, queue_size=10)
        self.down_pub = rospy.Publisher("go_down", Empty, queue_size=10)
        self.left_pub = rospy.Publisher("go_left", Empty, queue_size=10)
        self.right_pub = rospy.Publisher("go_right", Empty, queue_size=10)
        self.stop_tilt_pub = rospy.Publisher("stop_tilt", Empty, queue_size=10)
        self.stop_pan_pub = rospy.Publisher("stop_pan", Empty, queue_size=10)

    def send_instruction(self, instr):
        msg = Empty()
        if instr == "up":
            self.up_pub.publish(msg)
        elif instr == "down":
            self.down_pub.publish(msg)
        elif instr == "left":
            self.left_pub.publish(msg)
        elif instr == "right":
            self.right_pub.publish(msg)
        elif instr == "stop_pan":
            self.stop_pan_pub.publish(msg)
        elif instr == "stop_tilt":
            self.stop_tilt_pub.publish(msg)
        else:
            self.stop_tilt_pub.publish(msg)
            self.stop_pan_pub.publish(msg)


CameraDataManager = CDM.CameraDataManager(1280, 720)
Motor = MotorInstructionHandler()


def init_subscribers():
    rospy.Subscriber("x_center", Float32, pan_callback)
    rospy.Subscriber("y_center", Float32, tilt_callback)


def pan_callback(pixels_x):
    x = int(pixels_x.data)
    instr = CameraDataManager.create_motor_instructions_pan(x)
    Motor.send_instruction(instr)
    rospy.loginfo("x_center: {}   direction:{}".format(x, instr))


def tilt_callback(pixels_y):
    y = int(pixels_y.data)
    instr = CameraDataManager.create_motor_instructions_tilt(y)
    Motor.send_instruction(instr)
    rospy.loginfo("y_center: {}   direction:{}".format(y, instr))


def main():
    rospy.init_node("motor_intructions")
    Motor.init_publishers()
    init_subscribers()
    rospy.spin()


if __name__ == "__main__":
    main()
