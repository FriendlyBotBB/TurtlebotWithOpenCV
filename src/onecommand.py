#! /usr/bin/python
# coding=utf-8

import rospy
import cv2
from  geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

kamera = cv2.VideoCapture(0)
yuz_cascade = cv2.CascadeClassifier('haarcascade-frontalface-default.xml')

rospy.init_node('burak_bilge_node')

publisher_turtle1 = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size = 1)

movement = Twist()

movement.linear.x = 0.0
movement.linear.y = 0.0
movement.linear.z = 0.0
movement.angular.x = 0.0
movement.angular.y = 0.0
movement.angular.z = 0.0

def myFunc(data):
    a = 10

if __name__ == '__main__':
    rate = rospy.Rate(10)
    rospy.Subscriber("/odom", Odometry, myFunc)
    #rospy.Subscriber("/scan",LaserScan,junk)
    while not rospy.is_shutdown():
        ret, goruntu = kamera.read()

        # griton = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)
        yuzler = yuz_cascade.detectMultiScale(goruntu, 1.3, 4)
        # print yuzler
        for (x, y, w, h) in yuzler:
            cv2.rectangle(goruntu, (x, y), (x + w, y + h), (0, 255, 255), 3)

        if (yuzler != ()):
            movement.linear.x = 0.05
        else:
            movement.linear.x = 0.0

        cv2.imshow('Sa', goruntu)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        publisher_turtle1.publish(movement)
