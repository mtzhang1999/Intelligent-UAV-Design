#!/usr/bin/env python
#coding:utf-8
import os
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError
import numpy as np
import commands
root = "/path/to/your/python_data"
def callback(data):
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    # save image, detect, read result
    abs_path = os.path.join(root, "yolov3_detect")
    cv2.imwrite("%s/data/samples/three_balls.jpg" % abs_path, cv_image)
    os.system('cd %s && python detect.py' % abs_path)
    res_image = cv2.imread("%s/ball_detect.jpg" % abs_path)
    cv2.imshow("view", res_image)
def showImage():
    rospy.init_node('showImage', anonymous = True)
    cv2.namedWindow("view", cv2.WINDOW_AUTOSIZE)
    cv2.startWindowThread()
    rospy.Subscriber('ShowImage', Image, callback)
    rospy.spin()
    cv2.destroyWindow("view")
if __name__ == '__main__':
    showImage()