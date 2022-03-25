#!/usr/bin/python2.7
import RPi.GPIO as GPIO 
import time
import rospy
from std_msgs.msg import Float32

input_pin = 18  # BCM pin 18, BOARD pin 12

def main(pub, rate):
    prev_value = None

    # Pin Setup:
    GPIO.setmode(GPIO.BCM)  # BCM pin-numbering scheme from Raspberry Pi
    GPIO.setup(input_pin, GPIO.IN)  # set pin as an input pin
    print("Starting demo now! Press CTRL+C to exit")
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
            example_msg = 0.01
            rospy.loginfo(example_msg)
            pub.publish(example_msg)
            rate.sleep()
    finally:
        GPIO.cleanup()

def publisher():
  
    pub = rospy.Publisher("example_topic", Float32, queue_size=10)
    rospy.init_node("example_name", anonymous=True)
    rate = rospy.Rate(1)
    main(pub, rate)



if __name__ == "__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
