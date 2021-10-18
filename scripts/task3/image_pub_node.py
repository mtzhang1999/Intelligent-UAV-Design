#!/usr/bin/env python
#coding:utf-8
import rospy
import sys
import cv2
import os
import numpy as np
from sensor_msgs.msg import Image
import random
from cv_bridge import CvBridge, CvBridgeError

root = "/path/to/your/python_data"

def pubImage():
    rospy.init_node('pubImage', anonymous = True)
    pub = rospy.Publisher('ShowImage', Image, queue_size = 10)
    rate = rospy.Rate(1)
    bridge = CvBridge()
    path = os.path.join(root, "three_balls.jpeg")
    image = cv2.imread(path)
    h, w, _ = image.shape
    while not rospy.is_shutdown():
        start_h = int(random.random() * h / 4)
        height = int(h * 3 / 4)
        start_w = int(random.random() * w / 4)
        width = int(w * 3 / 4)
        transfer_image = image[start_h:(start_h+height),start_w:
        (start_w+width),:]

        pub.publish(bridge.cv2_to_imgmsg(transfer_image, "bgr8"))
        rate.sleep()

if __name__ == '__main__':
    try:
        pubImage()
    except rospy.ROSInterruptException:
        pass
