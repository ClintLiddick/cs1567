#!/usr/bin/python
import rospy
from std_msgs.msg import *
from nav_msgs.msg import *
from geometry_msgs.msg import *
from cs1567p4.srv import *
from kobuki_msgs.msg import *
from tf.transformations import euler_from_quaternion
import math
import sys
import random
import time

global pub
global pub2

global started
started = False
global pos
global turning
turning = False
global currz
currz = 0
global xLeftError
xLeftError = .05
global xRightError
xRightError = 1.35
global yError
yError = 1.2
global score
score = False
pub = None
pub2 = None

global score2
score2 = False
global score3 
score3 = False

global numHits
numHits = 0

def get_start_orientation():
    global pos
    global pub
    #pub.publish(Empty())
    command = Twist()
    send_command = rospy.ServiceProxy('constant_command', ConstantCommand)
    target = 1 + random.random()
    posneg = random.random()
    if(posneg > .5):
        target *= -1
    zgoal = 3
    w = pos.pose.pose.orientation.w
    z = pos.pose.pose.orientation.z
    x_theta_new,y_theta_new,z_theta_new = euler_from_quaternion([0,0,z,w])

    x = pos.pose.pose.position.x

    command.angular.z = 0
    send_command(command)
    
    while(x < .7):
	if(command.linear.x != .3):
	    command.linear.x = .3
	    send_command(command)

	x = pos.pose.pose.position.x

    command.linear.x = 0
    send_command(command)
    while(z_theta_new < (target - .1) or z_theta_new > (target + .1)):
        if(command.angular.z != zgoal):
   	    command.angular.z = zgoal
	    send_command(command)
	w = pos.pose.pose.orientation.w
        z = pos.pose.pose.orientation.z
        x_theta_new,y_theta_new,z_theta_new = euler_from_quaternion([0,0,z,w])
    command.angular.z = 0
    send_command(command)
    command.linear.x = .3
    send_command(command)
    #currz = pos.pose.pose.position.x + pos.pose.pose.position.y

    return target

def get_new_orientation():
    global pos

    tar = random.random()
    posneg = random.random()
    w = pos.pose.pose.orientation.w
    z = pos.pose.pose.orientation.z
    x_theta_new,y_theta_new,z_theta_new = euler_from_quaternion([0,0,z,w])

    halfPi = 1.57
    if(posneg > .5):
        tar *=-1

    halfPi += tar

    if(z < 0):
        return halfPi
    else:
	return halfPi *-1

def turn_left():
    global turning
    global pos
    global currz
    command = Twist()
    send_command = rospy.ServiceProxy('constant_command', ConstantCommand)
    w = pos.pose.pose.orientation.w
    z = pos.pose.pose.orientation.z
    x_theta_new,y_theta_new,z_theta_new = euler_from_quaternion([0,0,z,w])
    target = z_theta_new + .7
    zgoal = 3
    while(z_theta_new < (target - .1) or z_theta_new > (target + .1)):
        if(command.angular.z != zgoal):
	    command.angular.z = zgoal
	    send_command(command)
	w = pos.pose.pose.orientation.w
        z = pos.pose.pose.orientation.z
        x_theta_new,y_theta_new,z_theta_new = euler_from_quaternion([0,0,z,w])
    command.angular.z = 0
    send_command(command)
    rospy.sleep(.1)
    command.linear.x = .3
    send_command(command)
    currz = pos.pose.pose.position.x + pos.pose.pose.position.y



def turn_around():
    global turning
    global pos
    global currz
    command = Twist()
    send_command = rospy.ServiceProxy('constant_command', ConstantCommand)
    w = pos.pose.pose.orientation.w
    z = pos.pose.pose.orientation.z
    x_theta_new,y_theta_new,z_theta_new = euler_from_quaternion([0,0,z,w])

    target = get_new_orientation()
    currOrientation = z_theta_new

    if(currOrientation + target < 0):
	zgoal = 3
    else:
	zgoal = -3

    while(z_theta_new < (target - .1) or z_theta_new > (target + .1)):
        if(command.angular.z != zgoal):
	    command.angular.z = zgoal
	    send_command(command)
	w = pos.pose.pose.orientation.w
        z = pos.pose.pose.orientation.z
        x_theta_new,y_theta_new,z_theta_new = euler_from_quaternion([0,0,z,w])
    command.angular.z = 0
    send_command(command)
    rospy.sleep(.1)
    command.linear.x = .3
    send_command(command)
    currz = pos.pose.pose.position.x + pos.pose.pose.position.y


def turn_right():
    global turning
    global pos
    global currz
    command = Twist()
    send_command = rospy.ServiceProxy('constant_command', ConstantCommand)
    w = pos.pose.pose.orientation.w
    z = pos.pose.pose.orientation.z
    x_theta_new,y_theta_new,z_theta_new = euler_from_quaternion([0,0,z,w])
    target = z_theta_new - .7
    zgoal = -3
    while(z_theta_new < (target - .1) or z_theta_new > (target + .1)):
        if(command.angular.z != zgoal):
	    command.angular.z = zgoal
	    send_command(command)
	w = pos.pose.pose.orientation.w
        z = pos.pose.pose.orientation.z
        x_theta_new,y_theta_new,z_theta_new = euler_from_quaternion([0,0,z,w])
    command.angular.z = 0
    send_command(command)
    rospy.sleep(.1)
    command.linear.x = .3
    send_command(command)
    currz = pos.pose.pose.position.x + pos.pose.pose.position.y

def bumper_callback(data):
    global pos
    global turning
    global currz
    global score
    global xLeftError
    global xRightError
    global yError
    print "bumper callback"
    command = Twist()
    send_command = rospy.ServiceProxy('constant_command', ConstantCommand)

    #left = 0 
    #center = 1
    #right = 2
    direction = data.bumper
    event = data.state

    global started
    global numHits
    global pub

    global score
    global score2
    global score3

    if(score == True):
	print "Score"
	currz = 0
	xLeftError = .05
	xRightError = 1.35
	yError = 1.2		    
	currz = 0
	numHits = 0
	#print pos
	score = False
	score2 = True
    elif(score2 == True):
	score2 = False
	pub.publish(Empty())
	score3 = True
    elif(score3 == True):
	started = False
	score3 = False
    elif(started == False):
	started = True
	get_start_orientation()
        currz = pos.pose.pose.position.x+pos.pose.pose.position.y
    else:
        if(event == 1):


	    w = pos.pose.pose.orientation.w
            z = pos.pose.pose.orientation.z

            x_theta_new,y_theta_new,z_theta_new = euler_from_quaternion([0,0,z,w])
 	    newz = pos.pose.pose.position.x + pos.pose.pose.position.y

	    if(abs(currz - newz) > .02):
		numHits+=1
		xLeftError += .01
		xRightError += .01
		yError += .01
		command.linear.x = 0
		send_command(command)
		target = z_theta_new
	        x = pos.pose.pose.position.x
	        y = pos.pose.pose.position.y
		pub_data = 0
		if(abs(y) > yError and not score):
		    score = True
		    if(y < 0):
			print "Robot 1 missed, point Robot 2"
			pub_data = 2
		    else:
			print "Robot 2 missed, point Robot 1"
			pub_data = 1

		    pub2.publish(pub_data)
    	

		    

		elif(abs(y) > 1 and (x < xLeftError or x > xRightError)):
		    print "Hit robot"
		    if(y < 0):
		        print "Hit robot 1"
	            else:
		        print "Hit robot 2"

		    turn_around()		    

	        elif(x > xLeftError and x < xRightError and abs(y) < yError):
		    print "Hit robot"
		    if(y < 0):
		        print "Hit robot 1"
	            else:
		        print "Hit robot 2"

		    turn_around()
	    	elif(x < xLeftError):
		    print "Left Wall hit"
		    if(direction == 0):
		        print "Left Bumper hit"
		        turn_right()
		    elif(direction == 2):
		        print "Right Bumper hit"
		        turn_left()
		    elif(direction == 1):
			if(z_theta_new > 0):
			    turn_left()
			else:
			    turn_right()

	        elif(x > xRightError):
		    print "Right wall hit"
		    if(direction == 0):
		        print "Left Bumper hit"
		        turn_right()
		    elif(direction == 2):
		        print "Right Bumper hit"
		        turn_left()

		    elif(direction == 1):
			if(z_theta_new > 0):
			    turn_left()
			else:
			    turn_right()



	        else:
		    print "Something went wrong"
		    print "X: " 
		    print pos.pose.pose.position.x
		    print pos.pose.pose.position.y

	    	print pos.pose.pose.position.x
	    	print pos.pose.pose.position.y
		print numHits
		

	   # if(abs(currz - newz) > .05):
           #     print "Bumper Hit"
           #     command.linear.x = 0
     	   #     send_command(command)
	    
 	   #     target = z_theta_new
	   # 	if(direction == 0):
	#	    print "Left bumper hit"
#		    turn_right()
#		    #turn right 45 degrees

#	        if(direction == 2):
#		    print "Right bumper hit"
#		    turn_left()
#		    #turn left 45 degrees
#	        if(direction == 1):
#		    turn_around()
			
		    #turn around ~ 180

	   # print currz
       	   # print pos.pose.pose.orientation.z

	   



def odometry_callback(data):
    global pos
    pos = data
    #print pos
    print pos.pose.pose.position.y
	#pos.pose.pose.position.x = top wall = 1.42 meters
	
	#position [x] ~ 1.42m
	#position [y] ~ 1m to robot
	

	
    
def initialize_commands():
    print "init"
    rospy.init_node('ball_bot', anonymous=True)
    global pub
    pub = rospy.Publisher('/mobile_base/commands/reset_odometry', Empty, queue_size=10)
    global pub2
    print "publishing point_scored"
    pub2 = rospy.Publisher('point_scored', UInt32, queue_size=10)
    print "subscribing to bumper"
    rospy.Subscriber('mobile_base/events/bumper', BumperEvent, bumper_callback)
    print "subscribing to odometry"
    rospy.Subscriber('/odom', Odometry, odometry_callback)
    print "waiting for constant command service"
    rospy.wait_for_service('constant_command')
    print "constant command service success"
    rospy.wait_for_service('constant_command')

    while pub.get_num_connections() < 1:
     rospy.sleep(0.1)

    pub.publish(Empty())
    rospy.spin()


    
     
if __name__ == "__main__":   
    try: 
        initialize_commands()
    except rospy.ROSInterruptException: pass

