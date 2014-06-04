#!/usr/bin/python
import rospy
from geometry_msgs.msg import Twist
from cs1567p1.srv import *
from std_srvs.srv import * 
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

# movement commands

def move_forward():
    global facing
    global current_pos
    
    try:
        command.linear.x = 0.1
        response = constant_command_service(command)
        rospy.sleep(6.2)
        command.linear.x = 0.0
        response = constant_command_service(command)
        rospy.sleep(0.5)
        
        if facing == LEFT:
            current_pos = (current_pos[0]-1,current_pos[1])
        elif facing == RIGHT:
            current_pos = (current_pos[0]+1,current_pos[1])
        elif facing == UP:
            current_pos = (current_pos[0],current_pos[1]-1)
        elif facing == DOWN:
            current_pos = (current_pos[0],current_pos[1]+1)
            
    except rospyServiceException, e:
        print "Service call failed: %s"%e
    
def turn_left():
    global facing
    command.angular.z = 0.5
    response = constant_command_service(command)
    rospy.sleep(5.4)
    command.angular.z = 0.0
    response = constant_command_service(command)
    rospy.sleep(0.5)

    facing = getNextLeftDirection()


def turn_right():
    global facing
    command.angular.z = -0.5
    response = constant_command_service(command)
    rospy.sleep(5.3)
    command.angular.z = 0.0
    response = constant_command_service(command)
    rospy.sleep(0.5)

    facing = getNextRightDirection()
        

def solve_maze():
    global current_pos
    global facing
    # easy way to start algo is to be facing down
    turn_right()
    turn_right()
    
    #begin left-hand rule algo
    while (current_pos != (4,4)):      
        # DEBUG
        rospy.loginfo("position: ({},{})".format(current_pos[0],current_pos[1]))
        rospy.loginfo("facing: {}".format(facing))
        print "left: {} forward: {} right: {}".format(leftwall(),forwardwall(),rightwall())
        ### need to check what kind of value the get_wall_service returns (leftwall() etc) ###
        
        # go left if possible
        if not leftwall():
            turn_left()
            move_forward()
        # else go forward if possible
        elif not forwardwall():
            move_forward()
        # else go right if possible
        elif not rightwall():
            turn_right()
            move_forward()
        else:
            turn_left()
    rospy.loginfo("final position: ({},{})".format(current_pos[0],current_pos[1]))


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
    pub = rospy.Publisher('/mobile_base/commands/reset_odometry', Empty, queue_size=10)
    rospy.Subscriber('/odom', Odometry, odometry_callback)
    while (pub.get_num_connections() <= 0):
        rospy.sleep(0.1)

    pub.publish(Empty())
    rospy.spin()
    ## end odom

    global make_maze_service, print_maze_service, get_wall_service
    global constant_command_service

    make_maze_service = rospy.ServiceProxy('make_maze', MakeNewMaze)
    print_maze_service = rospy.ServiceProxy('print_maze', Empty)
    get_wall_service = rospy.ServiceProxy('get_wall', GetMazeWall)
    constant_command_service = rospy.ServiceProxy('constant_command', ConstantCommand)
    
    # runs code
    make_maze_service(MAZE_SIZE,MAZE_SIZE)
    print_maze_service()
    solve_maze()

     
if __name__ == "__main__":   
    try: 
        initialize_commands()
    except rospy.ROSInterruptException: pass

