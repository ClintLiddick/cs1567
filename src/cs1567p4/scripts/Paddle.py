#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt32
from cs1567p4.srv import *
from geometry_msgs.msg import Twist
from tf.transformations import euler_from_quaternion

LINEAR_SPEED = 0.3

object_position = 0
motion_command = Twist()
constant_command_serv = None

def object_position_callback(data):
    rospy.loginfo('position: {}'.format(data.data))
    w = data.pose.pose.orientation.w
    z = data.pose.pose.orientation.z
    x,y,z = euler_from_quaternion([0,0,z,w])
    rospy.loginfo('heading: {} {} {}'.format(x,y,z))
    global object_position
    object_position = data.data

def strafe_right():
    #forward
    try:
        motion_command.linear.x = LINEAR_SPEED
        const_command_serv(motion_command)
    except rospy.ServiceException, e:
        rospy.logerr("Service call failed: %s",e)

def strafe_left():
    #forward
    try:
        motion_command.linear.x = -LINEAR_SPEED
        const_command_serv(motion_command)
    except rospy.ServiceException, e:
        rospy.logerr("Service call failed: %s",e)

def stay():
    #forward
    try:
        motion_command.linear.x = 0
        const_command_serv(motion_command)
    except rospy.ServiceException, e:
        rospy.logerr("Service call failed: %s",e)

def run():
    while not rospy.is_shutdown():
        if object_position == 3:
            strafe_right()
        elif object_position == 2:
            stay()
        elif object_position == 1:
            strafe_left()
        else:
            stay()

def init():
    rospy.logdebug('init called')
    rospy.init_node('paddle_node',anonymous=True,log_level=rospy.INFO)
    rospy.logdebug('node init')
    rospy.wait_for_service('constant_command')
    rospy.logdebug('constant_command service')
    rospy.Subscriber('paddle1_obj',UInt32,object_position_callback)
    rospy.logdebug('subscribed')
    
    global const_command_serv
    const_command_serv = rospy.ServiceProxy('constant_command', ConstantCommand)
    run()

if __name__ == '__main__':
    try:
        rospy.loginfo('started paddle')
        init()
    except rospy.ROSInterruptException: pass
