#!/usr/bin/env python
import rospy
import math
from std_msgs.msg import *
from nav_msgs.msg import *
from geometry_msgs.msg import *
from cs1567p0.srv import *

def odometry_callback(data):
    command = Twist()
    send_command = rospy.ServiceProxy('constant_command', ConstantCommand)

    rospy.loginfo("\nx: {}\ny: {}\nz: {}".format(data.pose.pose.position.x,data.pose.pose.position.y,data.pose.pose.orientation.z))

    # 1 forward/turn 
    if 2*math.acos(data.pose.pose.orientation.w) < 1.57:
        if data.pose.pose.position.x < 0.8:
            command.angular.z = 0.0
            command.linear.x = 0.5
            send_command(command)
        elif data.pose.pose.position.x < 1.0:
            command.linear.x = 0.1
            send_command(command)
        else:
            command.linear.x = 0.0
            command.angular.z = 0.5
            send_command(command)
    # 2 forward/turn
    elif 2*math.acos(data.pose.pose.orientation.w) < 3.14:
        if data.pose.pose.position.y < 0.8:
            command.angular.z = 0.0
            command.linear.x = 0.5
            send_command(command)
        elif data.pose.pose.position.y < 1.0:
            command.linear.x = 0.1
            send_command(command)
        else:
            command.linear.x = 0.0
            command.angular.z = 0.5


def initialize():
    pub = rospy.Publisher('/mobile_base/commands/reset_odometry', Empty, queue_size=10)
    rospy.Subscriber('/odom', Odometry, odometry_callback)
    rospy.init_node('MoveSquareOdometry', anonymous=True)
    rospy.wait_for_service('constant_command')
    while (pub.get_num_connections() <= 0):
        rospy.sleep(0.1)

    pub.publish(Empty())
    rospy.spin()
    

if __name__ == "__main__":
    initialize()

