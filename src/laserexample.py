#! /usr/bin/python

import rospy
import random
import math
from  geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan

rospy.init_node('burak_node')

publisher_turtle1 = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size = 1)

a=0
movement = Twist()

movement.linear.x = 0.3
movement.linear.y = 0.0
movement.linear.z = 0.0
movement.angular.x = 0.0
movement.angular.y = 0.0
movement.angular.z = 0.0



def junk(data):
	global a
	for mesafe in data.ranges:
		if(mesafe < 0.8 ):
			movement.linear.x = 0.0
			print 'durdum'

if __name__ == '__main__':
	rate = rospy.Rate(10)
	rospy.Subscriber("/scan",LaserScan,junk)
   	while not rospy.is_shutdown():
		publisher_turtle1.publish(movement) 
		rate.sleep()
	rospy.spin()


