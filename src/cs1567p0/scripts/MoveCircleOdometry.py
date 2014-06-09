#!/usr/bin/env python
import rospy
from std_msgs.msg import *
from nav_msgs.msg import *
from geometry_msgs.msg import *
from cs1567p0.srv import *

def odometry_callback(data):
    command = Twist()
    send_command = rospy.ServiceProxy('constant_command', ConstantCommand)

# travel until completing a full circle
    rospy.loginfo("\nx: {}\ny: {}".format(data.pose.pose.position.x,data.pose.pose.position.y))
    
    if data.pose.pose.position.x > -0.18:
        command.linear.x = 0.5
        command.angular.z = 1.0
        send_command(command)
    else:
        command.linear.x = 0.0
        command.angular.z = 0.0
        send_command(command)


def initialize():
    pub = rospy.Publisher('/mobile_base/commands/reset_odometry', Empty, queue_size=10)
    rospy.Subscriber('/odom', Odometry, odometry_callback)
    rospy.init_node('MoveCircleOdometry', anonymous=True)
    rospy.wait_for_service('constant_command')
    while (pub.get_num_connections() <= 0):
        rospy.sleep(0.1)

    pub.publish(Empty())
    rospy.spin()
    

if __name__ == "__main__":
    initialize()

