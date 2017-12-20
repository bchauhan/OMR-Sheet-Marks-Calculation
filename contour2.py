# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 16:06:50 2017

@author: admin
"""

import cv2
import random
import numpy as np
import houghlinesp
import time
from math import sqrt

# Create windows to show the captured images
#cv2.namedWindow("window_a", cv2.CV_WINDOW_AUTOSIZE) 
#cv2.namedWindow("window_b", cv2.CV_WINDOW_AUTOSIZE)
HEIGHT=700
WIDTH=0
def readImage(capture):
    flag, img=capture.read()
    if flag:
        h,w,_=img.shape
        a=float(h)/w
        WIDTH=int(HEIGHT/a)
        img=cv2.resize(img,(WIDTH,HEIGHT))
    else:
        img=None
    return flag,img

def distance(a,b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def is_between(a,c,b):
    return distance(a,c) + distance(c,b) == distance(a,b)

def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)
# Structuring element
es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9,4))
## Webcam Settings
capture = cv2.VideoCapture("087_edited.avi")

#dimensions
frameWidth = 700
frameHeight = 1000
ret,frame=readImage(capture)
HEIGHT,WIDTH,_=frame.shape
#previous = cv2.blur(frame, (5,5))
previous=frame#cv2.resize(frame,(1400,800))
point1,point2=houghlinesp.main(previous)
point3=(point1[0]-500,point1[1])
point4=(point2[0]-500,HEIGHT)

now=time.time()
print "start line : ",point1,point2
p1=None
xpre=WIDTH
ypre=HEIGHT
dt=0

framenumber=0
beep=False
k=None
font=cv2.FONT_HERSHEY_SIMPLEX 
lastframe=None
i=0
#for cnt in contours:
while True:
    # Capture a frame

        
    flag,frame = readImage(capture)
    if flag==False:
        cv2.destroyAllWindows()
        break
    #frame=cv2.resize(frame,(1400,800))
    
    
    cv2.line(frame, point1,point2, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.line(frame, point3,point4, (0, 0, 255), 2, cv2.LINE_AA)
    key = cv2.waitKey(10) #20
    if key == 27 or flag!=True: #exit on ESC
        cv2.destroyAllWindows()
        break
    elif key==13:
        beep=True
        print "->",beep
        
    if beep:
        framenumber+=1
        print framenumber
    else:
        cv2.putText(frame,"Press Enter to start timer",(200,200),font,0.7,(0,0,255),2)
        

    current = cv2.blur(frame, (5,5))
    difference = cv2.absdiff(current, previous) #difference is taken of the current frame and the previous frame
    previous = current
    frame2 = cv2.cvtColor(difference, cv2.COLOR_RGB2GRAY)
    retval,thresh = cv2.threshold(frame2, 10, 0xff, cv2.THRESH_OTSU)
    kernel = np.ones((7,7),np.uint8)
    kernel1 = np.ones((15,15),np.uint8)
    erosion = cv2.erode(thresh,kernel,iterations = 3)
    dilation = cv2.dilate(erosion,kernel1,iterations = 10)
    blur=cv2.medianBlur(dilation,25)
    #blur = cv2.medianBlur(blur,45)
    #blur = cv2.medianBlur(blur,25)
    #blur = cv2.medianBlur(blur,25)
    erosion = cv2.erode(blur,kernel,iterations = 10) 
    #dilated1 = cv2.dilate(erosion, es)
    #dilated2 = cv2.dilate(dilated1, es)
    im2, contours, hierarchy = cv2.findContours(erosion,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
   

    if len(contours)!=0:
        cnt = max(contours, key = cv2.contourArea)
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        area = cv2.contourArea(cnt)
        if area>12000:
            #print "area : ",area
            cv2.circle(frame,(cx,cy),6,(0,255,255),-1)
            #if area>2000:
            rect = cv2.boundingRect(cnt)
            x,y,w,h = rect
            #cv2.drawContours(frame, contours, -1, (0,255,0), 2)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
            xcurrent=x
            ycurrent=y
            if intersect((xpre,ypre),(xcurrent,ycurrent),point3,point4) and p1==None:
                print"->", (xpre,ypre),(xcurrent,ycurrent)
                print "=>",point3,point4
                print "is f1 : ",flag==0,flag
                endtime=time.time()
                print "crossed at : ",endtime
                p1=(WIDTH-(WIDTH/4),HEIGHT-50)
                timediff=endtime-now
                fpsnew=framenumber/(timediff)
                print "time diffrence : ",timediff
                print "frames till now : ",framenumber
                dt=float(framenumber)/150.0
                print "frame new speed : ",fpsnew
                print "*********************************************"
            xpre=xcurrent
            ypre=ycurrent
    if p1!=None and beep:
        #print "starttime : ",now
        #print "endtime : ",endtime
        
        cv2.putText(frame,"Crossed in : "+str(dt)+" seconds",p1,font,0.5,(0,0,255),2)
        if i==0 or i==1:
            lastframe=frame
            i+=1

    cv2.imshow('window_a', erosion)
    cv2.imshow('window_b', frame)

    previous = current
    
cv2.imshow('output', lastframe)
cv2.waitKey(0)
cv2.destroyAllWindows()
