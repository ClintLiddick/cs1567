#!/usr/bin/env python
"""
ROS Publisher node for Topic 'tracked_object_position'

This node determines whether the tuned object is in the left, center, or right
third of the image frame, or whether it is not in the frame at all.

UInt32
0 = not in frame
1 = left third
2 = center third
3 = right third
"""

import rospy
import cv2
import numpy
from std_msgs.msg import *

# OpenCV HSV value ranges
lowH = 0
highH = 179
lowS = 0
highS = 255
lowV = 0
highV = 255
# objects
webcam = None
pub = None
# webcam info
cam_width = 1
cam_height = 1

def updateHSV():
    """Reads the image color tuning trackbar and updates global data"""
    global lowH
    global highH
    global lowS
    global highS
    global lowV
    global highV
    
    lowH  = cv2.getTrackbarPos('lowH','control')
    highH = cv2.getTrackbarPos('highH','control')
    lowS  = cv2.getTrackbarPos('lowS','control')
    highS = cv2.getTrackbarPos('highS','control')
    lowV  = cv2.getTrackbarPos('lowV','control')
    highV = cv2.getTrackbarPos('highV','control')

# img is [[[bgr],[bgr]...],[...]...]

def nothing(dummy=None):
    """Dummy callback for trackbars"""
    pass


def run():
    """Main image masking and publishing code"""
    while not rospy.is_shutdown():
        # read frame from webcam
        _,img = webcam.read()
        # update color tuning from control panel
        updateHSV()
        # convert frame to HSV format
        hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        # create mask for color selected in color tuning panel
        mask = cv2.inRange(hsv_img, numpy.array([lowH,lowS,lowV],numpy.uint8),\
                numpy.array([highH,highS,highV],numpy.uint8))
        # convert mask to binary image format
        _,binary = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)
        # filter image to reduce noise
        binary = cv2.erode(binary,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)))
        binary = cv2.dilate(binary,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)))

        binary = cv2.dilate(binary,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)))
        binary = cv2.erode(binary,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)))

        center_x = -1
        center_y = -1
        # get moments of image
        moments = cv2.moments(binary)
        if (moments['m00'] > 0.0):
            # find the "center of gravity" of the moment 
            # (which is hopefully the tracked object)
            center_x = int(moments['m10']/moments['m00'])
            center_y = int(moments['m01']/moments['m00'])
        rospy.loginfo('Center: (%d,%d)',center_x,center_y)

        # publish
        pub_data = 0
        if (center_x == -1):
            # out of frame
            pub_data = 0    
        elif (center_x < (cam_width/3)):
            # left third
            pub_data = 1
        elif (center_x < (2*cam_width/3)):
            # middle third
            pub_data = 2
        elif (center_x < (cam_width)):
            # right third
            pub_data = 3

        pub.publish(pub_data)
        rospy.loginfo('published: %d',pub_data)
        
        # draw a green dot on the center and display images on local screen
        cv2.circle(mask,(center_x,center_y),2,[0,255,0],2)
        cv2.imshow('masked',mask)
        cv2.imshow('binary',binary)
	cv2.waitKey(1)

def setup_control_panel():
    """Setup color tuning panel"""
    cv2.namedWindow('control',flags=cv2.WINDOW_NORMAL)
    rospy.logdebug('control panel open')
    cv2.createTrackbar('lowH','control',0,179,nothing)
    cv2.createTrackbar('highH','control',179,179,nothing)
    cv2.createTrackbar('lowS','control',0,255,nothing)
    cv2.createTrackbar('highS','control',255,255,nothing)
    cv2.createTrackbar('lowV','control',0,255,nothing)
    cv2.createTrackbar('highV','control',255,255,nothing)

def set_img_dimensions():
    """Set dimensions of frame captured from webcam"""
    global cam_width
    global cam_height
    _,img = webcam.read()
    cam_height,cam_width,_ = img.shape


def init():
    """Init node, global data, windows, and publisher"""
    rospy.init_node('objecttrackernode',anonymous=True)
    global pub
    pub = rospy.Publisher('paddle1_obj',UInt32, queue_size=10)
    global webcam
    cv2.namedWindow('masked')
    rospy.logdebug('masked window open')
    cv2.namedWindow('binary')
    rospy.logdebug('binary window open')
    setup_control_panel()
    webcam = cv2.VideoCapture(0)
    set_img_dimensions()
    run()


if __name__ == '__main__':
    try:
        init()
    except rospy.ROSInterruptException: pass
