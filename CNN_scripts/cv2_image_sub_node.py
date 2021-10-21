#!/usr/bin/env python
#coding:utf-8
import os
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError
import numpy as np
root = "/path/to/your/python_data"
def callback(data):
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    # transfer gray and load template
    cv_image_gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    template_path = os.path.join(root, "ball.jpeg")
    template_image = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    res = cv2.matchTemplate(cv_image_gray, template_image, cv2.TM_SQDIFF)
    # find max index, and plot
    index_position = np.where(res == np.min(res))
    index_h, index_w = index_position[0][0], index_position[1][0]
    template_h, template_w = template_image.shape
    cv2.rectangle(cv_image, (index_w, index_h), (index_w + template_w, index_h + template_h), [0,0,255], 2)
    cv2.imshow("view", cv_image)
def showImage():
    rospy.init_node('showImage', anonymous = True)
    cv2.namedWindow("view", cv2.WINDOW_AUTOSIZE)
    cv2.startWindowThread()
    rospy.Subscriber('ShowImage', Image, callback)
    rospy.spin()
    cv2.destroyWindow("view")
if __name__ == '__main__':
    showImage()