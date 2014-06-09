#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from cs1567p0.srv import *

def move_square():
    rospy.init_node('MoveSquareNoOdometry', anonymous=True)
    rospy.wait_for_service('constant_command')
    command = Twist()
    
    try:
        send_command = rospy.ServiceProxy('constant_command', ConstantCommand)
        for x in range(0,4):
            # forward
            command.linear.x = 0.5
            response = send_command(command)
            rospy.sleep(2.4)
            # stop forward
            command.linear.x = 0.0
            response = send_command(command)
            rospy.sleep(0.2)
            # turn
            command.angular.z = 1.5
            response = send_command(command)
            rospy.sleep(1.5)
            # stop turn
            command.angular.z = 0
            response = send_command(command)
            rospy.sleep(1)

        print response

    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    move_square()
