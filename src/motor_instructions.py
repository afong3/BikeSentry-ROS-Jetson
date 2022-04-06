#!/usr/bin/python2.7
import rospy
from std_msgs.msg import Empty, Float32, Int32, Float64
from CameraDataManager import CameraDataManager

SENTRY_MODE = 0
SHOOT_IN_PROGESS = False

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
        self.servo_shoot_pub = rospy.Publisher("servo_shoot", Empty, queue_size=10)

    def send_instruction(self, instr):
        global SHOOT_IN_PROGESS
        msg = Empty()

        # We dont want motors to move when Tower has not detected a theft.
        if SENTRY_MODE == 0:
            self.stop_tilt_pub.publish(msg)
            self.stop_pan_pub.publish(msg)
            self.stop_flywheel_spin_pub.publish(msg)
            return

        # While a ball is shooting stop sending instructions now while it shoots.
        # See the done_shot callback which flips this variable.
        if SHOOT_IN_PROGESS:
            rospy.loginfo("Skipping instructions")
            # NEVER send instructions while it shooting!
            return
        
        # TILT is always sending as stop so lets just always send stop tilt and be done with it.
        self.stop_tilt_pub.publish(msg)

        # Fly wheel is always spinning in sentry mode
        self.start_flywheel_spin_pub.publish(msg)

        if instr == "stop_pan":
            SHOOT_IN_PROGESS = True
            rospy.loginfo("Shooting starting")
            #Shoot 1 ball
            self.servo_shoot_pub.publish(msg)
            self.stop_pan_pub.publish(msg)
            return
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
    


cameraDataManager = CameraDataManager(1280, 720)
motor = MotorInstructionHandler()

def done_shot_callback(data):
    rospy.loginfo("Shooting finished")
    global SHOT_IN_PROGESS
    SHOT_IN_PROGESS = False

def init_subscribers():
    rospy.Subscriber("x_center", Float32, pan_callback)
    rospy.Subscriber("y_center", Float32, tilt_callback)
    rospy.Subscriber("state", Int32, state_callback)
    rospy.Subscriber("done_shot", Float64, done_shot_callback)

def state_callback(state):
    global SENTRY_MODE
    SENTRY_MODE = state.data

def pan_callback(pixels_x):
    x = int(pixels_x.data)
    instr = cameraDataManager.create_motor_instructions_pan(x)
    motor.send_instruction(instr)
    #rospy.loginfo("x_center: {}   direction:{}".format(x, instr))


def tilt_callback(pixels_y):
    #y = int(pixels_y.data)
    # Commenting this out since we no longer care about tilt position
    #instr = cameraDataManager.create_motor_instructions_tilt(y)
    #motor.send_instruction(instr)
    #rospy.loginfo("y_center: {}   direction:{}".format(y, instr))
    return
    


def main():
    rospy.init_node("motor_intructions")
    motor.init_publishers()
    init_subscribers()
    rospy.spin()


if __name__ == "__main__":
    main()
