#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16

def callback(msg):
    rospy.loginfo("Slyhau %s", msg.data)

rospy.init_node('sluhai1')
rospy.Subscriber('slyhai1_topic', Int16, callback, queue_size=10)
rospy.spin()
