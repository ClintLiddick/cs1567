#!/usr/bin/env python

import cv2
import numpy

# color range used to mask image
lower_blue = numpy.array([90,0,0],numpy.uint8)
upper_blue = numpy.array([130,255,255],numpy.uint8)

lowH = 0
highH = 179

lowS = 0
highS = 255

lowV = 0
highV = 255

webcam = cv2.VideoCapture(0)
cv2.namedWindow("orig")
cv2.namedWindow("masked")
cv2.namedWindow("gray")
cv2.namedWindow("binary")

cv2.namedWindow('control')

def updateHSV():
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

def nothing():
    pass

cv2.createTrackbar('lowH','control',0,179,nothing)
cv2.createTrackbar('highH','control',0,179,nothing)
cv2.createTrackbar('lowS','control',0,255,nothing)
cv2.createTrackbar('highS','control',0,255,nothing)
cv2.createTrackbar('lowV','control',0,255,nothing)
cv2.createTrackbar('highV','control',0,255,nothing)

while True:
    _,img = webcam.read()
    updateHSV()
    hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_img, numpy.array([lowH,lowS,lowV],numpy.uint8),\
            numpy.array([highH,highS,highV],numpy.uint8))
    #masked_img = cv2.bitwise_and(img,img, mask=mask)
    #gray = cv2.cvtColor(masked_img,cv2.COLOR_BGR2GRAY)
    _,binary = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)
    binary = cv2.erode(binary,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)))
    binary = cv2.dilate(binary,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)))

    binary = cv2.dilate(binary,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)))
    binary = cv2.erode(binary,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)))
    #contours,_ = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    moments = cv2.moments(binary)
    if (moments['m00'] > 0.0):
        # find the "center of gravity"
        center_x = int(moments['m10']/moments['m00'])
        center_y = int(moments['m01']/moments['m00'])
        print center_x,center_y
    print moments['m00']

    #cv2.drawContours(img,contours,-1,(0,255,0),3)
    
    cv2.imshow("orig",img)
    cv2.imshow("masked",mask)
    #cv2.imshow("gray",gray)
    cv2.imshow("binary",binary)
    key = cv2.waitKey(20)
    if key in [27, ord('Q'), ord('q')]:
        break

