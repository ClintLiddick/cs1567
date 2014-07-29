import rospy
from cs1567p4.srv import *
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from std_msgs.msg import UInt32

PADDLE_1_SCORE = 0
PADDLE_2_SCORE = 0
WIN_SCORE = 5

x_displacement = 0.0
y_displacement = 0.0
LINEAR_SPEED = 0.3

motion_command = Twist()
const_command_serv = None


def odometry_callback():	# useless function for now, will get goal or not from other node
    global x_displacement
    global y_displacement
    
    x_displacement = data.pose.pose.position.x
    y_displacement = data.pose.pose.position.y
	
def points_callback(data):
	if data.data == 1:		#PATS CODE, NEED TO KNOW
		PADDLE_1_SCORE+=1
	if data.data == 2:		#PATS CODE, NEED TO KNOW
		PADDLE_2_SCORE+=1

def end():
	if PADDLE_1_SCORE == WIN_SCORE:
		return True
	elif PADDLE_2_SCORE == WIN_SCORE:
		return True
	else:
		return False

def startmove():
	try:
		motion_command.linear.x = LINEAR_SPEED
		const_command_serv(motion_command)
	except rospy.ServiceException, e:
		rospy.logerr("Service call failed: %s",e)

def stopmove():
	try:
		motion_command.linear.x = 0
		motion_command.angular.z = 0
		const_command_serv(motion_command)
	except rospy.ServiceException, e:
		rospy.logerr("Service call failed: %s",e)

def start():
	startmove()
	while not end():
		rospy.sleep(0.3)
	stopmove()	

def init():
    rospy.init_node('gamekeepernode',anonymous=True)
    rospy.wait_for_service('constant_command')
    rospy.Subscriber('/odom',Odometry,odometry_callback)
    rospy.Subscriber('/PATSCALLBACK',UInt32,points_callback) 	#NEED PAT FUNCTION/INFO
    global const_command_serv
    const_command_serv = rospy.ServiceProxy('constant_command', ConstantCommand)
	start()

if __name__ == '__main__':
    try:
        init()
    except rospy.ROSInterruptException: pass