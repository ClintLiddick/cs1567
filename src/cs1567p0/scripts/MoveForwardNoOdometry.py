#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from cs1567p0.srv import *

def move_forward():
    rospy.init_node('MoveForwardNoOdometry', anonymous=True)
    rospy.wait_for_service('constant_command')
    command = Twist()
    
    try:
        send_command = rospy.ServiceProxy('constant_command', ConstantCommand)
        command.linear.x = 0.5
        response = send_command(command)
        rospy.sleep(2.5)
        command.linear.x = 0.0
        response = send_command(command)
        print response

    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    move_forward()
