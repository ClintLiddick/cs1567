#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from std_msgs.msg import UInt32
from kobuki_msgs.msg import *

PADDLE_1_SCORE = 0
PADDLE_2_SCORE = 0
WIN_SCORE = 3

led_pub = None
sound_pub = None

def score_notif(led):
    sound_pub.publish(Sound.OFF)
    for x in range(4):
        led_pub.publish(led)
        rospy.sleep(0.2)
        led_pub.publish(Led.BLACK)
        rospy.sleep(0.2)


def print_scores():
    rospy.loginfo('Paddle 1: {}'.format(PADDLE_1_SCORE))
    rospy.loginfo('Paddle 2: {}'.format(PADDLE_2_SCORE))


def points_callback(data):
    global PADDLE_1_SCORE
    global PADDLE_2_SCORE
    if data.data == 1:
        PADDLE_1_SCORE+=1
        rospy.loginfo('Point for Paddle 1!')
        score_notif(Led.GREEN)
    if data.data == 2:
        PADDLE_2_SCORE+=1
        rospy.loginfo('Point for Paddle 2!')
        score_notif(Led.RED)
    print_scores()



def end():
    if PADDLE_1_SCORE == WIN_SCORE:
        return True
    elif PADDLE_2_SCORE == WIN_SCORE:
        return True
    else:
        return False


def play():
    while not end() and not rospy.is_shutdown():
        rospy.sleep(0.3)
    print_scores()
    winner = ''
    if PADDLE_1_SCORE == WIN_SCORE:
        winner = 'Paddle 1'
    elif PADDLE_2_SCORE == WIN_SCORE:
        winner = 'Paddle 2'
    else:
        winner = 'NONE'
    rospy.loginfo('Winner: {}!'.format(winner))
    led_pub.publish(Led.BLACK)


def init():
    rospy.init_node('gamekeepernode',anonymous=True)
    rospy.Subscriber('/point_scored',UInt32,points_callback)
    global led_pub
    led_pub = rospy.Publisher('/mobile_base/commands/led1', Led, queue_size=10)
    global sound_pub
    sound_pub = rospy.Publisher('/mobile_base/commands/sound', Sound, queue_size=10)
    play()


if __name__ == '__main__':
    try:
        init()
    except rospy.ROSInterruptException: pass