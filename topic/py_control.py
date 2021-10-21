#!/usr/bin/env python
# coding=utf-8

import rospy
from geometry_msgs.msg import Twist

def controller():
    rospy.init_node('pycontroller', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10) #set topic name
    rate = rospy.Rate(0.3) # 0.3hz
    
    count = 0
    while not rospy.is_shutdown():
        if count % 4 == 0:
            control_cmd = Twist()
            control_cmd.linear.x = 2 #move forward
        if count % 4 == 1:
            control_cmd = Twist() #turn left
        if count % 4 == 2:
            control_cmd = Twist() #forward
        if count % 4 == 3:
            control_cmd = Twist() #turn right

        count += 1
        rospy.loginfo(control_cmd)
        pub.publish(control_cmd)
        rate.sleep()

if __name__ == '__main__':
    try:
        controller()
    except rospy.ROSInterruptException:
        pass