#!/usr/bin/python2.7
# Feed dumby data to the motor.

import rospy
from std_msgs.msg import Float32


def publish_dumby_data():
    rospy.init_node("mock_detectnet", anonymous=True)
    x_data_pub = rospy.Publisher("x_center", Float32, queue_size=10)
    y_data_pub = rospy.Publisher("y_center", Float32, queue_size=10)
    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        x = 10.0
        y = 10.0
        x_data_pub.publish(x)
        y_data_pub.publish(y)
        rospy.loginfo("sending {} , {}".format(x, y))
        rate.sleep()


if __name__ == "__main__":
    try:
        publish_dumby_data()
    except rospy.ROSInterruptException:
        pass
