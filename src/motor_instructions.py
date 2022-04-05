#!/usr/bin/python2.7
import rospy
from std_msgs.msg import Empty, Float32, Int32
from CameraDataManager import CameraDataManager

SENTRY_MODE = 0

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
        self.start_flywheel_spin_pub = rospy.Publisher("start_flywheel", Empty, queue_size=10)
        self.stop_flywheel_spin_pub = rospy.Publisher("stop_flywheel", Empty, queue_size=10)
        #Servo UP means balls will shoot
        self.servo_up_pub = rospy.Publisher("servo_up", Empty, queue_size=10)
        self.servo_down_pub = rospy.Publisher("servo_down", Empty, queue_size=10)

    def send_instruction(self, instr):
        msg = Empty()

        # We dont want motors to move when Tower has not detected a theft.
        if SENTRY_MODE == 0:
            self.stop_tilt_pub.publish(msg)
            self.stop_pan_pub.publish(msg)
            self.stop_flywheel_spin_pub.publish(msg)
            return
        
        self.start_flywheel_spin_pub.publish(msg)

        if instr == "stop_pan":
            #Shoot balls
            self.servo_up_pub.publish(msg)
            self.stop_pan_pub.publish(msg)
        else:
            # Stop shooting
            self.servo_down_pub.publish(msg)
            
        if instr == "up":
            self.up_pub.publish(msg)
        elif instr == "down":
            self.down_pub.publish(msg)
        elif instr == "left":
            self.left_pub.publish(msg)
        elif instr == "right":
            self.right_pub.publish(msg)
        elif instr == "stop_tilt":
            self.stop_tilt_pub.publish(msg)

    


cameraDataManager = CameraDataManager(1280, 720)
motor = MotorInstructionHandler()


def init_subscribers():
    rospy.Subscriber("x_center", Float32, pan_callback)
    rospy.Subscriber("y_center", Float32, tilt_callback)
    rospy.Subscriber("state", Int32, state_callback)

def state_callback(state):
    global SENTRY_MODE
    SENTRY_MODE = state.data

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
    rospy.spin()


if __name__ == "__main__":
    main()
