#!/usr/bin/python2.7
import RPi.GPIO as GPIO 
import rospy
from std_msgs.msg import Int32

input_pin = 18  # BCM pin 18, BOARD pin 12

def main(pub, rate):
    prev_value = None

    # Pin Setup:
    GPIO.setmode(GPIO.BCM)  # BCM pin-numbering scheme from Raspberry Pi
    GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # set pin as an input pin
    try:
        while True:
            value = GPIO.input(input_pin)
            if value != prev_value:
                if value == GPIO.HIGH:
                    value_str = "HIGH"
                else:
                    value_str = "LOW"
                print("Value read from pin {} : {}".format(input_pin,
                                                           value_str))
                prev_value = value
            pub.publish(value)
            rate.sleep()
    finally:
        GPIO.cleanup()

def publisher():
    pub = rospy.Publisher("state", Int32, queue_size=10)
    rospy.init_node("system_state", anonymous=True)
    rate = rospy.Rate(10)
    main(pub, rate)


if __name__ == "__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
