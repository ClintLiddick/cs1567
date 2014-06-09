#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from cs1567p0.srv import *

current_command = Twist()

def recv_commands(new_command):
    global current_command
    current_command = new_command.cmd
    return 1

def send_commands():
    global current_command
    rospy.init_node('constantcommandnode', anonymous=True)
    pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)
    s = rospy.Service('constant_command', ConstantCommand, recv_commands)

    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        str = "%s"%current_command
        rospy.loginfo(str)
        pub.publish(current_command)
        r.sleep()

if __name__ == '__main__':
    try:
        send_commands()
    except rospy.ROSInterruptException: pass
