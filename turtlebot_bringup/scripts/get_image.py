#!/usr/bin/env python

import cv2
import rospy

from matplotlib import pyplot as plt
from sensor_msg.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def callback(msg):

    try:
        cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError as e:
        print(e)

    cv2.imshow('xiao', cv_image)
    cv2.waitKey(10)

if __name__=='__main__':
    rospy.init_node('get_image', anonymous=True)
    image_sub = rospy.Subscriber("/turtlebot02/camera/rgb/image_raw", Image, callback)
    rospy.spin()
