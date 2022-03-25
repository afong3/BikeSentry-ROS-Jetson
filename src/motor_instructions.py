#!/usr/bin/python2.7
from pickle import GLOBAL
import RPi.GPIO as GPIO 
import rospy
from std_msgs.msg import Empty, Float32
from CameraDataManager import CameraDataManager


INPUT_PIN = 18 # pin 12 on the real board

def pin_setup():
    # Pin Setup:
    GPIO.setmode(GPIO.BCM)  # BCM pin-numbering scheme from Raspberry Pi
    GPIO.setup(INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # set pin as an input pin

def read_pin():
    global PREV_VALUE
    value = GPIO.input(INPUT_PIN)
    return value # 1 or 0

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

        # We dont want motors to move when Tower has not detected a theft.
        if read_pin() == 0:
            self.stop_tilt_pub.publish(msg)
            self.stop_pan_pub.publish(msg)
            return

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


cameraDataManager = CameraDataManager(1280, 720)
motor = MotorInstructionHandler()


def init_subscribers():
    rospy.Subscriber("x_center", Float32, pan_callback)
    rospy.Subscriber("y_center", Float32, tilt_callback)


def pan_callback(pixels_x):
    x = int(pixels_x.data)
    instr = cameraDataManager.create_motor_instructions_pan(x)
    motor.send_instruction(instr)
    rospy.loginfo("x_center: {}   direction:{}".format(x, instr))


def tilt_callback(pixels_y):
    y = int(pixels_y.data)
    instr = cameraDataManager.create_motor_instructions_tilt(y)
    motor.send_instruction(instr)
    rospy.loginfo("y_center: {}   direction:{}".format(y, instr))


def main():
    rospy.init_node("motor_intructions")
    motor.init_publishers()
    init_subscribers()
    pin_setup()
    rospy.spin()


if __name__ == "__main__":
    main()
