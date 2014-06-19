#!/usr/bin/env python
import rospy
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import *
from cs1567p2.msg import *

# some colors from images taken of PostIt and construction PAper
# in BRG format
GREEN_PI = [90,225,220]
LPINK_PI = [75,150,235]
DPINK_PI = [175,120,230]
RED_PA = [110,90,230]
BLUE_PI = [200,205,175]

color_mask_list = [RED_PA] # try to use Blue postit as position and Red paper as direction
threshold = 70
kinect1pub = None
kinect2pub = None
kinect3pub = None
top_mask = Image()
mid_mask = Image()
bot_mask = Image()

top_cloud_points = (None,None,None,None)
mid_cloud_points = (None,None,None,None)
bot_cloud_points = (None,None,None,None)

def mask_image(message):
    byte_array = list(message.data) #convert unit8[] from string to chars
    for index in xrange(message.height*message.width): #iterate through
        for k in xrange(len(color_mask_list)): 
            #iterate through color list, if the bytes match, save the color
            #in the mask
            # ord(b) returns the value of ascii char (or 8-bit byte) b
            if abs(color_mask_list[k][0] - ord(byte_array[3*index])) < threshold\
                    and abs(color_mask_list[k][1] - ord(byte_array[3*index+1])) < threshold\
                    and abs(color_mask_list[k][2] - ord(byte_array[3*index+2])) < threshold:
                byte_array[3*index+0] = chr(color_mask_list[k][0])
                byte_array[3*index+1] = chr(color_mask_list[k][1])
                byte_array[3*index+2] = chr(color_mask_list[k][2])
            else:
                # chr(i) returns a byte ("ascii") whose value is i
                byte_array[3*index] = chr(0) # each pixel = 3 bytes, 1 for each color BGR
                byte_array[3*index+1] = chr(0)
                byte_array[3*index+2] = chr(0)
          
    return "".join(byte_array) #make char[] back into uint8[] string
 
def top_image_callback(message):
    global color_mask_list
    global top_mask
    global threshold
    global kinect1pub
    #make a new image if you want to view your mask
    top_mask = Image()
    top_mask.height = message.height # height/width in pixels?
    top_mask.width = message.width
    top_mask.encoding = message.encoding
    top_mask.is_bigendian = message.is_bigendian
    top_mask.step = message.step
    mask = ""
    if message.encoding == "bgr8": #this is image_color encoding
        mask = mask_image(message)
    top_mask.data = mask
    kinect1pub.publish(top_mask) #publish the mask for viewing
    print "done1"
        
def mid_image_callback(message):
    global color_mask_list
    global mid_mask
    global threshold
    global kinect3pub
    mid_mask = Image()
    mid_mask.height = message.height
    mid_mask.width = message.width
    mid_mask.encoding = message.encoding
    mid_mask.is_bigendian = message.is_bigendian
    mid_mask.step = message.step
    mask = ""
    if message.encoding == "bgr8":
        mask = mask_image(message)
    mid_mask.data = mask
    kinect3pub.publish(mid_mask)
    print "done3"

def bot_image_callback(message):
    global color_mask_list
    global bot_mask
    global threshold
    global kinect2pub
    bot_mask = Image()
    bot_mask.height = message.height
    bot_mask.width = message.width
    bot_mask.encoding = message.encoding
    bot_mask.is_bigendian = message.is_bigendian
    bot_mask.step = message.step
    mask = ""
    if message.encoding == "bgr8": #this is image_color encoding
        mask = mask_image(message)
    top_mask.data = mask
    kinect2pub.publish(bot_mask)
    print "done2"



def top_cloud_callback(message):
    try:
        #make a generator, skipping points that have no depth, on points in 
        # list of uvs (index into image [col,row]) or if empty list, get all pt
        global top_cloud_points
        top_cloud_points = message
        """data_out = pc2.read_points(message, field_names=None, skip_nans=True, uvs=[]) # list of 4-tuples
        i=0
        iteration1 = next(data_out) #format x,y,z,rgba
        while iteration1 != None:
            iteration1 = next(data_out)
            i=i+1
        """
    except StopIteration: 
        print "1 complete"

def mid_cloud_callback(message):
    try:
        global mid_cloud_points
        mid_cloud_points = message
        """data_out = pc2.read_points(message, field_names=None, skip_nans=True, uvs=[])
        i=0
        iteration1 = next(data_out) #format x,y,z,rgba
        while iteration1 != None:
            iteration1 = next(data_out)
            i=i+1
        """
    except StopIteration: 
        print "3 complete"


def bot_cloud_callback(message):
    try:
        global bot_cloud_points
        bot_cloud_points = message
        """data_out = pc2.read_points(message, field_names=None, skip_nans=True, uvs=[])
        i=0
        iteration1 = next(data_out) #format x,y,z,rgba
        while iteration1 != None:

            iteration1 = next(data_out)
            i=i+1
        """
    except StopIteration: 
        print "2 complete"

###############################################
# TODO

# as 2D array: index = row*height + col*width

def colorsMatch(first,second):
    return first[0] == second[0] and first[1] == second[1] and first[2] == second[2]

def find_center(mask,index):
    mask = list(mask)
    # return point that is average of greatest/least y and x values
    pt_color = mask.data[index:index+3]
    color = pt_color
    up = 0
    i = 0
    while i >= index and colorsMatch(color,pt_color):
        i += mask.width * 3
        color = mask.data[index-i:index-i+3]
        up += 1

    color = pt_color
    down = 0
    i = 0
    while i < (mask.height*3 - index) and colorsMatch(color,pt_color):
        i += mask.width * 3
        color = mask.data[index+i:index+i+3]
        down += 1

    # check left right (col)
    color = pt_color
    left = 0
    i = 0
    while i <= (index % mask.width) and colorsMatch(color,pt_color):
        i += 3
        color = mask.data[index-i:index-i+3]
        left += 1

    color = pt_color
    right = 0
    i = 0
    while i <= (mask.width - (index % mask.width)) and colorsMatch(color,pt_color):
        i += 3
        color = mask.data[index+i:index+i+3]
        up += 1

    x = (right + left)/2
    y = (up + down)/2
    return (x,y)

def find_center_near(points, color, loc, dist):
    # returns point that is center of points, but within dist::int distance of loc point::(x,y)
    print "find center near"

def merge_xy_kinects(top_points, mid_points, bot_points):
    # return single merged list of points with (x,y) relative to global center
    # use this to take the two "masked" images into one big image before finding centers
    print "merge xy"

# note: filter a list with newlist = [item for item in oldlist if item.someattribute >= someval]

def blobWidthHeight(mask,index):
    mask = list(mask)
    # sum of distance from point that is still same color >= some threshold
    minSize = 100 #px
    # check up and down (row)
    pt_color = mask.data[index:index+3]
    color = pt_color
    up = 0
    i = 0
    while i >= index and colorsMatch(color,pt_color):
        i += mask.width * 3
        color = mask.data[index-i:index-i+3]
        up += 1

    color = pt_color
    down = 0
    i = 0
    while i < (mask.height*3 - index) and colorsMatch(color,pt_color):
        i += mask.width * 3
        color = mask.data[index+i:index+i+3]
        down += 1

    # check left right (col)
    color = pt_color
    left = 0
    i = 0
    while i <= (index % mask.width) and colorsMatch(color,pt_color):
        i += 3
        color = mask.data[index-i:index-i+3]
        left += 1

    color = pt_color
    right = 0
    i = 0
    while i <= (mask.width - (index % mask.width)) and colorsMatch(color,pt_color):
        i += 3
        color = mask.data[index+i:index+i+3]
        up += 1

    return (left+right,up+down)



def findUniqueCenters():
    minSize = 100
    mid_centers = []
    bot_centers = []
    for k in xrange(mid_mask.width*mid_mask.height):
        if mid_mask[k*3] != 0:
            x,y = blobWidthHeight(mid_mask,k*3)
            if x > minSize and y > minSize:
                center = find_center(mid_mask,k*3)
                if center not in mid_centers:
                    mid_centers.append(center)

    for k in xrange(bot_mask.width*bot_mask.height):
        if bot_mask[k*3] != 0:
            x,y = blobWidthHeight(bot_mask,k*3)
            if x > minSize and y > minSize:
                center = find_center(bot_mask,k*3)
                if center not in bot_centers:
                    bot_centers.append(center)
    print mid_centers
    print bot_centers
 

###############################################

def initialize():
    global kinect1pub
    global kinect2pub
    global kinect3pub
    global locpub
    rospy.init_node("localize")
    locpub = rospy.Publisher("/twiki/location",LocationList) #publish your locations
    kinect1pub = rospy.Publisher("/twiki/top_mask",Image) #test your mask
    kinect2pub = rospy.Publisher("/twiki/bot_mask",Image)
    kinect3pub = rospy.Publisher("/twiki/mid_mask",Image)
    rospy.Subscriber("/kinect1/rgb/image_color", Image, top_image_callback)
    rospy.Subscriber("/kinect1/depth_registered/points", PointCloud2, top_cloud_callback)
    rospy.Subscriber("/kinect3/rgb/image_color", Image, mid_image_callback)
    rospy.Subscriber("/kinect3/depth_registered/points", PointCloud2, mid_cloud_callback)
    rospy.Subscriber("/kinect2/rgb/image_color", Image, bot_image_callback)
    rospy.Subscriber("/kinect2/depth_registered/points", PointCloud2, bot_cloud_callback)
    findUniqueCenters()
    rospy.spin()

if __name__ == "__main__":
    initialize()

