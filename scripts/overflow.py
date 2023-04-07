#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16

def callback(alr):
    rospy.loginfo("SSbross %d", alr.data)

rospy.init_node('sluhai1peregruz')
rospy.Subscriber('peregruz_topic', Int16, callback, queue_size=10)
rospy.spin()
