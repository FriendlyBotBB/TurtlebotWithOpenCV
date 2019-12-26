#! /usr/bin/python

import cv2
import rospy
import random
import math
from  geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
kamera = cv2.VideoCapture(0)
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


def go(myPosition):
    global x_diff
    global y_diff
    global div

    destination_x = 0
    destination_y = 0

    my_x = myPosition.pose.pose.position.x
    my_y = myPosition.pose.pose.position.y

    my_angle = myPosition.pose.pose.orientation.z

    x_diff = (destination_x - my_x)
    y_diff = (destination_y - my_y)

    hipo = math.sqrt((x_diff * x_diff) + (y_diff * y_diff))


    if x_diff > 0 :
        movement.linear.x = 1.0
        div = y_diff/hipo
    elif(x_diff<0):
        movement.linear.x = -1.0
        div = -y_diff/hipo
    elif (x_diff == 0):
        div = 0

    if my_angle < div - 0.1:
            movement.angular.z = 0.4
    elif my_angle > div + 0.1:
        movement.angular.z = -0.4
    elif my_angle < div + 0.1 and my_angle > div - 0.1:
        movement.angular.z = 0.0

    if((x_diff < 0.3 and x_diff > 0) or (x_diff > -0.3 and x_diff < 0)):
        if((y_diff < 0.3 and y_diff>0) or (y_diff > -0.3 and y_diff < 0)):
            movement.linear.x = 0
            movement.angular.z = 0.0
            print '{}'.format(myPosition.pose.pose.position)


def myFunc(data):
    go(data)
    a=7

def junk(data):
    global a
    if(a==0):
        print '{}'.format(data)
        a = 1

if __name__ == '__main__':
    rate = rospy.Rate(10)
    rospy.Subscriber("/odom", Odometry, myFunc)
    #rospy.Subscriber("/scan",LaserScan,junk)
    while not rospy.is_shutdown():
        ret, goruntu=kamera.read()
        cv2.imshow('Sa',goruntu)
        if cv2.waitKey(25) & 0xFF==ord('q'):
            break
        publisher_turtle1.publish(movement)
        rate.sleep()
    rospy.spin()


