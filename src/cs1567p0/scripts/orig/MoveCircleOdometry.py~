#!/usr/bin/env python
import rospy
from std_msgs.msg import *
from nav_msgs.msg import *
from geometry_msgs.msg import *
from cs1567p0.srv import *

def odometry_callback(data):
    command = Twist()
    send_command = rospy.ServiceProxy('constant_command', ConstantCommand)

    if(data.pose.pose.position.x < 1.0):
        command.linear.x = 0.5
        send_command(command)
    else:
        command.linear.x = 0.0
        send_command(command)


def initialize():
    pub = rospy.Publisher('/mobile_base/commands/reset_odometry', Empty, queue_size=10)
    rospy.Subscriber('/odom', Odometry, odometry_callback)
    rospy.init_node('MoveCircleOdometry', anonymous=True)
    rospy.wait_for_service('constant_command')
    pub.publish(Empty())
    rospy.spin()
    

if __name__ == "__main__":
    initialize()

