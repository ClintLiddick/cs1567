#!/usr/bin/env python

import rospy
import math
from cs1567p3.srv import *
from geometry_msgs.msg import Twist
from kobuki_msgs.msg import BumperEvent
from nav_msgs.msg import Odometry

ODOM_RATE = 11
LINEAR_SPEED = 0.1
ANGULAR_SPEED = 0.5
ANGULAR_SLEEP_TIME = 1.3
ORIGIN_TOLERANCE = 0.5

motion_command = Twist()
const_command_serv = None
bumped = False
number_of_bump_misses = 0

x_displacement = 0.0
y_displacement = 0.0
theta_displacement_w = 0.0
theta_displacement_z = 0.0
orientation_w = 0.0
orientation_z = 0.0

has_left_beginning = False

def odometry_callback(data):
    global x_displacement
    global y_displacement
    global theta_displacement_w
    global theta_displacement_z
    global orientation_w
    global orientation_z
    
    x_displacement = data.pose.pose.position.x
    y_displacement = data.pose.pose.position.y
    theta_displacement_w = 2*math.acos(data.pose.pose.orientation.w)
    orientation_w = data.pose.pose.orientation.w
    theta_displacement_z = 2*math.asin(data.pose.pose.orientation.z)
    orientation_z = data.pose.pose.orientation.z

def bumper_event_callback(data):
    # data is a BumperEvent
    # uint8 data.bumper: 0=left, 1=center, 2=right
    # uint8 data.state: 0=released, 1=pressed
    # use ord(uint8) to get number
    global bumped

    state = data.state
    if state == 1:
        bumped = True
    else:
        bumped = False
    
    rospy.loginfo('state: %d',state)

def stop():
    try:
        motion_command.linear.x = 0
        motion_command.angular.z = 0
        const_command_serv(motion_command)
        rospy.sleep(0.2)
    except rospy.ServiceException, e:
        rospy.logerr("Service call failed: %s",e)

# moves forward until stop() is executed
def go_forward_continuous():
    try:
        motion_command.linear.x = 0.1
        const_command_serv(motion_command)
    except rospy.ServiceException, e:
        rospy.logerr("Service call failed: %s",e)

# backs up a constant amount    
def back_up_unit():
    r = rospy.Rate(ODOM_RATE)
    
    starting_x = x_displacement
    starting_y = y_displacement
    
    while math.hypot((x_displacement - starting_x),(y_displacement - starting_y)) < 0.03\
            and not rospy.is_shutdown():
        try:
            motion_command.linear.x = -LINEAR_SPEED
            const_command_serv(motion_command)
            r.sleep()
        except rospy.ServiceException, e:
            rospy.logerr("Service call failed: %s",e)
    
    stop()
    
# turns left x degrees
def turn_left_unit():
    """
    starting_theta = theta_displacement_w
    rospy.loginfo('turning left starting at theta %f',starting_theta)
    r = rospy.Rate(ODOM_RATE)
    # theta is increasing while turning left
    # TODO this might break when completing a whole rotation (theta wraps to 0)
    radians_to_turn = math.radians(deg)
    while (theta_displacement_w - starting_theta) < radians_to_turn\
            and not rospy.is_shutdown():
        rospy.loginfo('theta_displacement_w: %f',theta_displacement_w)
        rospy.loginfo('w value: %f',orientation_w)
        motion_command.angular.z = 0.5
        const_command_serv(motion_command)
        r.sleep()
    """
    try:
        motion_command.angular.z = ANGULAR_SPEED
        const_command_serv(motion_command)
        rospy.sleep(ANGULAR_SLEEP_TIME)
    except rospy.ServiceException, e:
        rospy.logerr("Service call failed: %s",e)
    finally:
        stop()

# turns right x degrees
def turn_right_unit():
    """
    starting_theta = theta_displacement_w
    rospy.loginfo('turning right starting at theta %f',starting_theta)
    r = rospy.Rate(ODOM_RATE)
    radians_to_turn = math.radians(deg)
    while (theta_displacement_w - starting_theta) < radians_to_turn\
            and not rospy.is_shutdown():
        rospy.loginfo('theta_displacement_w: %f',theta_displacement_w)
        rospy.loginfo('w value: %f',orientation_w)
        motion_command.angular.z = -0.5
        const_command_serv(motion_command)
        r.sleep()
    """
    try:
        motion_command.angular.z = -ANGULAR_SPEED
        const_command_serv(motion_command)
        rospy.sleep(ANGULAR_SLEEP_TIME * ((number_of_bump_misses % 4)+1))
    except rospy.ServiceException, e:
        rospy.logerr("Service call failed: %s",e)
    finally:
        stop()

def turn_right_continuous():
    try:
        motion_command.angular.z = -ANGULAR_SPEED
        const_command_serv(motion_command)
    except rospy.ServiceException, e:
        rospy.logerr("Service call failed: %s",e)
        
def should_continue():
    global has_left_beginning
    distance_to_orig = math.hypot(x_displacement,y_displacement)
    rospy.loginfo('has_left_beginning: {}'.format(has_left_beginning))
    rospy.loginfo('distance from orig: {}'.format(distance_to_orig))
    # moved outside the tolerence zone once, so can stop if it enters again
    if (has_left_beginning):
        cont = not (distance_to_orig < ORIGIN_TOLERANCE)
        rospy.loginfo('should_cont: {}'.format(cont))
        return cont
    # hadn't left the tolerance zone at last check
    else: # hadn't left the tolerance zone at last check
        if (distance_to_orig > ORIGIN_TOLERANCE+0.01):
            has_left_beginning = True # check if outside tolerance zone
        return True # always continue in this situation
    
def follow_wall():
    """
    --algorithm--
    while: not done
        do: go_forward_continuous()
        while: not bumped and time_moving_forward < threshold
        // ^^^ needs tight rospy.Rate loop to check
        stop()
        if bumped:
            back_up_unit()
            stop()
            turn_left_unit()
            stop()
            continue
        else: time > threshold
            turn_right_unit() // try to hit wall now
            stop()
            continue
    """
    r = rospy.Rate(ODOM_RATE)
    time = 0.0
    global number_of_bump_misses
    while (should_continue() and not rospy.is_shutdown()):
        go_forward_continuous()
        time += 0.1
        
        if bumped:
            stop()
            back_up_unit()
            turn_left_unit()
            time = 0.0
            number_of_bump_misses = 0
            continue
        # normal
        """
        if time > 4.0:
            stop()
            turn_right_unit()
            time = 0.0
            number_of_bump_misses += 1
            continue
        # curving
        """
        if time > 4.0:
            turn_right_continuous()
            time = 0.0
            continue
        r.sleep()
    

def test_movements():
    """
    rospy.loginfo('4x back_up_unit then turn_left_unit')
    for i in range(0,4):
        back_up_unit()
        turn_left_unit(20)
    """ 
    rospy.loginfo('4x back_up_unit then turn_right_unit')
    for i in range(0,4):
        back_up_unit()
        turn_right_unit()
        
    r = rospy.Rate(0.5)
    rospy.loginfo('2x go_forward_continuous 1 second then stop')
    
    for i in range(0,2):
        for j in range(0,2):
            go_forward_continuous()
            r.sleep()
        stop()
        r.sleep()
    """
    rospy.loginfo('turn_right_unit in complete circle')
    for i in range(0,10):
        turn_right_unit(89)
        
    rospy.loginfo('turn_left_unit in complete circle')
    for i in range(0,10):
        turn_left_unit(89)
    """

def initialize_commands():
    rospy.init_node('wallsolvernode',anonymous=True)
    rospy.wait_for_service('constant_command')
    
    rospy.Subscriber('/mobile_base/events/bumper',BumperEvent,bumper_event_callback)
    rospy.Subscriber('/odom',Odometry,odometry_callback)

    global const_command_serv
    const_command_serv = rospy.ServiceProxy('constant_command', ConstantCommand)
    
    follow_wall()
    #test_movements()
    stop()

if __name__ == '__main__':
    try:
        initialize_commands()
    except rospy.ROSInterruptException: pass
