#! /usr/bin/python
# coding=utf-8

import rospy
from  geometry_msgs.msg import Twist

rospy.init_node('burak_node')

publisher_turtle1 = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size = 1)

a=0
x_diff = 0
y_diff = 0
div = 0

movement = Twist()

movement.linear.x = 0.0
movement.linear.y = 0.0
movement.linear.z = 0.0
movement.angular.x = 0.0
movement.angular.y = 0.0
movement.angular.z = 0.0

if __name__ == '__main__':
    rate = rospy.Rate(10)
    #rospy.Subscriber("/odom", Odometry, myFunc)
    #rospy.Subscriber("/scan",LaserScan,junk)
    while not rospy.is_shutdown():

        f = open("/home/burak/catkin_ws/src/moving_turtlebot/src/command.txt", "r")
        command = f.read()
        print(command)
        if(command == "GIT"):
            movement.linear.x = 0.05
        if (command == "DUR"):
            movement.linear.x = 0.0

        publisher_turtle1.publish(movement)
        rate.sleep()

