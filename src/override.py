#!/usr/bin/python2.7
"""
When this node is on the tower will not listen to the GPIO pin anymore 
It will put the sentry in sentry mode!
"""
import rospy
from std_msgs.msg import String

GLOB_PUB = rospy.Publisher("override", String, queue_size=10)

def clean_up():
     GLOB_PUB.publish("Running clean up lets go, sweep sweep the broom!")
     for i in range(1,10):
        GLOB_PUB.publish("off")

def publisher(pub):
    rospy.init_node("override", anonymous=True)
    rate = rospy.Rate(1)
    rospy.on_shutdown(clean_up)
    while not rospy.is_shutdown():
        override_message = "on"
        rospy.loginfo("override activated")
        pub.publish(override_message)
        rate.sleep()

        
if __name__ == "__main__":
    pub = GLOB_PUB
    try:
        publisher(pub)
    except rospy.ROSInterruptException:
       pass 
