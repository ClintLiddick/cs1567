import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from std_msgs.msg import UInt32
from kobuki_msgs import Led

PADDLE_1_SCORE = 0
PADDLE_2_SCORE = 0
WIN_SCORE = 5

led_pub = None

	
def points_callback(data):
	if data.data == 1:
		PADDLE_1_SCORE+=1
		led_pub.publish(Led.GREEN)
	if data.data == 2:
		PADDLE_2_SCORE+=1
		led_pub.publish(Led.RED)
	rospy.sleep(1)
	led_pub.publish(Led.BLACK)



def end():
	if PADDLE_1_SCORE == WIN_SCORE:
		return True
	elif PADDLE_2_SCORE == WIN_SCORE:
		return True
	else:
		return False


def start():
	while not end():
		rospy.sleep(0.3)


def init():
    rospy.init_node('gamekeepernode',anonymous=True)
    rospy.Subscriber('/odom',Odometry,odometry_callback)
    rospy.Subscriber('/point_scored',UInt32,points_callback)
    global led_pub
    led_pub = rospy.Publisher('/mobile_base/commands/led1', Led, queue_size=10)
	start()


if __name__ == '__main__':
    try:
        init()
    except rospy.ROSInterruptException: pass