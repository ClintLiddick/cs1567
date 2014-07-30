#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt32
from cs1567p4.srv import *
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

LINEAR_SPEED = 0.2
ANGULAR_SPEED = 0.2
THETA_DELTA = 0.01

object_position = 0
motion_command = Twist()
constant_command_serv = None

heading = 0

def odom_callback(data):
    w = data.pose.pose.orientation.w
    z = data.pose.pose.orientation.z
    global heading
    _,_,heading = euler_from_quaternion([0,0,z,w])
    rospy.loginfo('heading: {}'.format(heading))

def object_position_callback(data):
    rospy.loginfo('position: {}'.format(data.data))
    global object_position
    object_position = data.data

def correct_heading():
    if heading < -THETA_DELTA:
        # correct left
        motion_command.angular.z = ANGULAR_SPEED
        const_command_serv(motion_command)
    elif heading > THETA_DELTA:
        # correct right
        motion_command.angular.z = -ANGULAR_SPEED
        const_command_serv(motion_command)
    else:
        motion_command.angular.z = 0
        const_command_serv(motion_command)

def strafe_right():
    #forward
    try:
        motion_command.linear.x = LINEAR_SPEED
        const_command_serv(motion_command)
        correct_heading()
    except rospy.ServiceException, e:
        rospy.logerr("Service call failed: %s",e)

def strafe_left():
    #forward
    try:
        motion_command.linear.x = -LINEAR_SPEED
        const_command_serv(motion_command)
        correct_heading()
    except rospy.ServiceException, e:
        rospy.logerr("Service call failed: %s",e)

def stay():
    #forward
    try:
        motion_command.linear.x = 0
        motion_command.angular.z = 0
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
    rospy.logdebug('subscribed object position')
    rospy.Subscriber('/odom',Odometry,odom_callback)
    rospy.logdebug('subscribed odom')
    
    global const_command_serv
    const_command_serv = rospy.ServiceProxy('constant_command', ConstantCommand)
    run()

if __name__ == '__main__':
    try:
        rospy.loginfo('started paddle')
        init()
    except rospy.ROSInterruptException: pass
