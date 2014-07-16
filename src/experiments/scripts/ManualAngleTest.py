#!/usr/bin/env python

import rospy
import math
from experiments.srv import *
from geometry_msgs.msg import Twist
from kobuki_msgs.msg import BumperEvent
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

x_displacement = 0.0
y_displacement = 0.0
x_theta_prev = 0.0
y_theta_prev = 0.0
z_theta_prev = 0.0

has_left_beginning = False

def odometry_callback(data):
    #global x_displacement
    #global y_displacement
    global x_theta_prev
    global y_theta_prev
    global z_theta_prev
    
    #x_displacement = data.pose.pose.position.x
    #y_displacement = data.pose.pose.position.y
    w = data.pose.pose.orientation.w
    z = data.pose.pose.orientation.z

    x_theta_new,y_theta_new,z_theta_new = euler_from_quaternion([0,0,z,w])
    if (x_theta_new != x_theta_prev or y_theta_new != y_theta_prev or z_theta_new != z_theta_prev):
        x_theta_prev = x_theta_new
        y_theta_prev = y_theta_new
        z_theta_prev = z_theta_new
        rospy.loginfo('x: {}\ny: {}\nz: {}'.format(x_theta_prev,y_theta_prev,z_theta_prev))

"""
def stop():
    try:
        motion_command.linear.x = 0
        motion_command.angular.z = 0
        const_command_serv(motion_command)
        rospy.sleep(0.2)
    except rospy.ServiceException, e:
        rospy.logerr("Service call failed: %s",e)
"""

def initialize_commands():
    rospy.init_node('manualangletestnode',anonymous=True,log_level=rospy.DEBUG)
    rospy.Subscriber('/odom',Odometry,odometry_callback)
    rospy.loginfo('started')
    rospy.spin()

if __name__ == '__main__':
    try:
        initialize_commands()
    except rospy.ROSInterruptException: pass
