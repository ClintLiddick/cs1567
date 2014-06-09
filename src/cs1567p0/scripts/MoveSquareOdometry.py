#!/usr/bin/env python
import rospy
from std_msgs.msg import *
from nav_msgs.msg import *
from geometry_msgs.msg import *
from cs1567p0.srv import *

def odometry_callback(data):
    command = Twist()
    send_command = rospy.ServiceProxy('constant_command', ConstantCommand)

    try:
	send_command = rospy.ServiceProxy('constant_command', ConstantCommand)

        if data.pose.pose.position.x < 0.8:
            command.linear.x = 0.5
            send_command(command)
        elif data.pose.pose.position.x < 1.0:
            command.linear.x = 0.1
            send_command(command)
        else:
            command.linear.x = 0.0
            send_command(command)
            if data.pose.pose.orientation.z < 0.67:
	            command.angular.z = 0.5
	            send_command(command)
            else:
                command.angular.z = 0.0
                send_command(command)
                pub = rospy.Publisher('/mobile_base/commands/reset_odometry', Empty, queue_size=10)
                pub.publish(Empty())


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

