#!/usr/bin/env python3
import rospy
import tf
import math
from tf.transformations import quaternion_from_euler
from turtlesim.msg import Pose
rospy.init_node('tf_turtle')
turtlename = rospy.get_param('~turtle')
def handle_turtle_pose(msg):
    br = tf.TransformBroadcaster()
    br.sendTransform((msg.x, msg.y, 0),
                     quaternion_from_euler(0, 0, msg.theta),
                     rospy.Time.now(),
                     turtlename,
                     "world")
    angle=rospy.Time.now().to_sec() * math.pi
    x=3*math.cos(angle)
    y=3*math.sin(angle)    
    br.sendTransform((x, y, 0), 
    quaternion_from_euler(0, 0, angle), 
    rospy.Time.now(), 
    "carrot", 
    turtlename)
rospy.Subscriber('input_pose',
                 Pose,
                 handle_turtle_pose)
rospy.spin()
