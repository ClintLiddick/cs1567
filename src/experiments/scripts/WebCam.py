#!/usr/bin/env python

import cv2 

MASK_THRESHOLD = 20

webcam = cv2.VideoCapture(0)
cv2.namedWindow("orig")
cv2.namedWindow("mask")

# img is list of lists, 1 per row/col (3D array, since each pixel is list of 3 uints)
def get_image():
    retval, img = webcam.read()
    return img

# img is [[[bgr],[bgr]...],[...]...]
# color is [b,g,r]    
def mask_image(img,color):
    mask = img.copy()
    width,height,_ = img.shape
    for j in range(height):
        for i in range(width):
            b = img.item(i,j,0)
            g = img.item(i,j,1)
            r = img.item(i,j,2)
            if abs(b - color[0]) > MASK_THRESHOLD\
                    and abs(g - color[1]) > MASK_THRESHOLD\
                    and abs(r - color[2]) > MASK_THRESHOLD:
                mask.itemset((i,j,0),0)
                mask.itemset((i,j,1),0)
                mask.itemset((i,j,2),0)
            else:
                mask.itemset((i,j,0),255)
                mask.itemset((i,j,1),255)
                mask.itemset((i,j,2),255)  
    return mask

def binary_img(img):
    _,binary = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    return binary
    
def gray_img(img):
    return cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# clear first few frames fro ramp-up    
for x in range(30):
    temp = get_image()
while True:
    img = get_image()
    mask = mask_image(img,[185,196,112])
    gray = gray_img(img)
    binary = binary_img(gray)
    contours,_ = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    moments = cv2.moments(contours[0])
    if (moments['m00'] > 0.0):
        center_x = int(moments['m10']/moments['m00'])
        center_y = int(moments['m01']/moments['m00'])
        print center_x,center_y
    print moments['m00']
    cv2.imshow("orig",binary)
    cv2.imshow("mask",mask)
    key = cv2.waitKey(20)
    if key in [27, ord('Q'), ord('q')]:
        break

