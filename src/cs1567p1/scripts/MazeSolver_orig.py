#!/usr/bin/python
import rospy
from cs1567p1.srv import *
from std_srvs.srv import * 

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

make_maze_service = None
print_maze_service = None
get_wall_service = None
constant_command_service = None

def move_forward():
    return 1

def turn_90_degrees():
    return 1

def solve_maze():
    return 1

def initialize_commands():
    rospy.init_node('mazesolvernode', anonymous=True)
    rospy.wait_for_service('make_maze')
    rospy.wait_for_service('print_maze')
    rospy.wait_for_service('get_wall')
#    rospy.wait_for_service('constant_command')

    global make_maze_service, print_maze_service, get_wall_service
    global constant_command_service

    make_maze_service = rospy.ServiceProxy('make_maze', MakeNewMaze)
    print_maze_service = rospy.ServiceProxy('print_maze', Empty)
    get_wall_service = rospy.ServiceProxy('get_wall', GetMazeWall)
#    constant_command_service = rospy.ServiceProxy('constant_command', ConstantCommand)

    make_maze_service(5,5)
    print_maze_service()
    solve_maze()

     
if __name__ == "__main__":   
    try: 
        initialize_commands()
    except rospy.ROSInterruptException: pass

