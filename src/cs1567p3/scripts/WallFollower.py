import rospy
from cs1567p3.srv import *
from geometry_msgs.msg import Twist
from kobuki_msgs.msg import BumperEvent
from nav_msgs.msg import Odometry

const_command_serv = None
bumped = false

def odometry_callback(data):
    # TODO

def bumper_event_callback(data):
    # data is a BumperEvent
    # uint8 data.bumper: 0=left, 1=center, 2=right
    # uint8 data.state: 0=released, 1=pressed
    # use ord(uint8) to get number
    # TODO

def stop():
    # TODO

def go_forward():
    # TODO

def turn_left():
    # TODO

def turn_right():
    # TODO    
    
def follow_wall():
    # TODO
    """
    --algorithm--
    while: not done
        do: go_forward()
        while: not bumped and time_moving_forward < threshold
        // ^^^ needs tight rospy.Rate loop to check
        stop()
        if bumped:
            back_up()
            stop()
            turn_right()
            stop()
            continue
        else: time > threshold
            turn_left() // try to hit wall now
            stop()
            continue
    """

def initialize_commands():
    rospy.init_node('wallsolvernode',anonymous=True)
    rospy.wait_for_service('constant_command')
    
    rospy.Subscriber('/mobile_base/events/bumper',BumperEvent,bumper_event_callback)
    rospy.Subscriber('/odom',Odometry,odometry_callback)

    global const_command_serv
    const_command_serv = rospy.ServiceProxy('constant_command', ConstantCommand)
    
    follow_wall()

if __name__ == '__main__':
    try:
        initialize_commands()
    except rospy.ROSInterruptException: pass
