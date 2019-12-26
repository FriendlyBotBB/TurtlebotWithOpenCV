#! /usr/bin/python

import cv2
kamera = cv2.VideoCapture(0)
yuz_cascade = cv2.CascadeClassifier('haarcascade-frontalface-default.xml')

if __name__ == '__main__':
    while(1):
        ret, goruntu = kamera.read()

        griton = cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)
        yuzler = yuz_cascade.detectMultiScale(goruntu,1.3,4)

        for(x,y,w,h) in yuzler:
            cv2.rectangle(goruntu, (x,y),(x+w,y+h),(0,255,255),3)

        if(yuzler != ()):
            f = open("command.txt", "w")
            f.write("GIT")
            f.close()
        else:
            f = open("command.txt", "w")
            f.write("DUR")
            f.close()

        cv2.imshow('Sa', goruntu)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
cv2.destroyAllWindows()
kamera.release()

