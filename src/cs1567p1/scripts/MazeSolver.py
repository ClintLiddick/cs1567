#!/usr/bin/python
import rospy
import std_msgs.msg as stdmsg
from nav_msgs.msg import *
from geometry_msgs.msg import Twist
from cs1567p1.srv import *
import std_srvs.srv as std_srv 
import math

MAZE_SIZE = 5

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

x_displacement = 0.0
y_displacement = 0.0
theta_displacement = 0.0

make_maze_service = None
print_maze_service = None
get_wall_service = None
constant_command_service = None
pub = None

command = Twist()

# starting position
facing = UP
current_pos = (0,0) # tuple in (col,row)

def getNextLeftDirection():
    if facing == LEFT:
        return DOWN
    elif facing == RIGHT:
        return UP
    elif facing == UP:
        return LEFT
    else:
        return RIGHT

def getNextRightDirection():
    if facing == LEFT:
        return UP
    elif facing == RIGHT:
        return DOWN
    elif facing == UP:
        return RIGHT
    else:
        return LEFT  
        
def checkWall(col,row,direction):
    # out of bounds check
    if col >= MAZE_SIZE or col < 0 or row >= MAZE_SIZE or row < 0:
        return True    
    else:
        res = get_wall_service(col,row,direction)
        print "res",res.wall
        if res.wall == 0:
            return False
        else:
            return True

# clean boolean functions for forward/left/right wall check
def forwardwall():
    global facing
    global current_pos
    
    return checkWall(current_pos[0],current_pos[1],facing)

def leftwall():
    global current_pos
    direction = getNextLeftDirection()
    return checkWall(current_pos[0],current_pos[1],direction)

def rightwall():
    global current_pos
    direction = getNextRightDirection()
    return checkWall(current_pos[0],current_pos[1],direction)

# movement commandsservice "returned no response"

def move_forward():
    global current_pos
    global facing
    pub.publish(stdmsg.Empty())
    rospy.sleep(0.5)
    print "forward start x: {}".format(x_displacement)
    r = rospy.Rate(11)
    while (x_displacement < 0.47  and not rospy.is_shutdown()):
    #while (x_displacement < 0.2  and not rospy.is_shutdown()):
        command.linear.x = 0.1
        constant_command_service(command)
        r.sleep()
        
    command.linear.x = 0.0
    constant_command_service(command)
    print "forward end x: {}".format(x_displacement)
    pub.publish(stdmsg.Empty())
    rospy.sleep(0.5)
    
    if facing == LEFT:
        current_pos = (current_pos[0]-1,current_pos[1])
    elif facing == RIGHT:
        current_pos = (current_pos[0]+1,current_pos[1])
    elif facing == UP:
        current_pos = (current_pos[0],current_pos[1]-1)
    elif facing == DOWN:
        current_pos = (current_pos[0],current_pos[1]+1)

    
def turn_left():
    global facing
    
    pub.publish(stdmsg.Empty())
    rospy.sleep(0.5)
    
    rospy.loginfo("started left turn, theta: {}".format(theta_displacement))
    r = rospy.Rate(11)
    while (theta_displacement < 1.48 and not rospy.is_shutdown()):
        command.angular.z = 0.5
        constant_command_service(command)
        r.sleep()

    command.angular.z = 0.0
    constant_command_service(command)
    
    rospy.loginfo("ended left turn")
    rospy.loginfo("left turn theta: {}".format(theta_displacement))
    pub.publish(stdmsg.Empty())
    rospy.sleep(0.5) 
   
    facing = getNextLeftDirection()  


def turn_right():
    global facing
    """
    pub.publish(stdmsg.Empty())
    rospy.sleep(0.5)
    
    rospy.loginfo("started right turn, theta: {}".format(theta_displacement))
    r = rospy.Rate(11)
    while (theta_displacement < 1.5 and not rospy.is_shutdown()):
        command.angular.z = -0.5
        constant_command_service(command)
        r.sleep()

    command.angular.z = 0.0
    constant_command_service(command)
    
    rospy.loginfo("right turn theta: {}".format(theta_displacement))
    pub.publish(stdmsg.Empty())
    rospy.sleep(0.5)
    """
    turn_left()
    turn_left()
    turn_left()

    

def solve_maze():
    global current_pos
    global facing
    # easy way to start algo is to be facing down
    turn_left()
    turn_left()
    
    #begin left-hand rule algo
    while (current_pos != (4,4)):      
        # DEBUG
        rospy.loginfo("position: ({},{})".format(current_pos[0],current_pos[1]))
        rospy.loginfo("facing: {}".format(facing))
        print "left: {} forward: {} right: {}".format(leftwall(),forwardwall(),rightwall())
        ### need to check what kind of value the get_wall_service returns (leftwall() etc) ###
        
        # go left if possible
        if not leftwall():
            print "going left"
            turn_left()
            move_forward()
        # else go forward if possible
        elif not forwardwall():
            print "goind forward"
            move_forward()
        # else go right if possible
        elif not rightwall():
            "going right"
            turn_right()
            move_forward()
        else:
            turn_left()
    rospy.loginfo("final position: ({},{})".format(current_pos[0],current_pos[1]))

def calibrate_odometry():
    """
    for x in range(0,4):
        turn_left()
    for x in range(0,4):
        turn_right()
    """
    for x in range(0,2):
        move_forward()


def odometry_callback(data):
    global x_displacement
    global y_displacement
    global theta_displacement
    
    x_displacement = data.pose.pose.position.x
    y_displacement = data.pose.pose.position.y
    theta_displacement = 2*math.acos(data.pose.pose.orientation.w)

def initialize_commands():
    rospy.init_node('mazesolvernode', anonymous=True)
    rospy.wait_for_service('make_maze')
    rospy.wait_for_service('print_maze')
    rospy.wait_for_service('get_wall')
    rospy.wait_for_service('constant_command')
    # odometry

    global pub
    pub = rospy.Publisher('/mobile_base/commands/reset_odometry', stdmsg.Empty, queue_size=10)
    rospy.Subscriber('/odom', Odometry, odometry_callback)
    while (pub.get_num_connections() <= 0):
        rospy.sleep(0.1)

    pub.publish(stdmsg.Empty())
    ## end odom

    global make_maze_service, print_maze_service, get_wall_service
    global constant_command_service
    make_maze_service = rospy.ServiceProxy('make_maze', MakeNewMaze)
    print_maze_service = rospy.ServiceProxy('print_maze', std_srv.Empty)
    get_wall_service = rospy.ServiceProxy('get_wall', GetMazeWall)
    constant_command_service = rospy.ServiceProxy('constant_command', ConstantCommand)
    
    #calibrate_odometry()    
    # runs code
    make_maze_service(MAZE_SIZE,MAZE_SIZE)
    print_maze_service()
    solve_maze()

     
if __name__ == "__main__":   
    try: 
        initialize_commands()
    except rospy.ROSInterruptException: pass

