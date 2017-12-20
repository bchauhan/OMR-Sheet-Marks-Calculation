# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 10:23:38 2017

@author: admin
"""

import cv2
import numpy as np
import math

def distance(x1,y1,x2,y2):
    x=(x2-x1)**2
    y=(y2-y1)**2
    length=math.sqrt(x+y)
    print "x^2  ,  y^2   : ",x,y
    print "length achived : ",length
    return length
    
def intercept(x,y,m):
    print "calculating intercept of : ",x,y,m
    return y-m*x

def main(img):
    h,w,_=img.shape
    kernel = np.ones((5,5),np.uint8)
    
    #img = cv2.imread("WA0003_houghline.jpg")
    #img = cv2.resize(img,(1400,800))
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    gray=cv2.equalizeHist(gray)
    ret,thresh=cv2.threshold(gray,127, 255, cv2.THRESH_BINARY)
    #erosion = cv2.erode(thresh,kernel,iterations = 1)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    #thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    #thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    #thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    edges = cv2.Canny(thresh,50,150,apertureSize = 3)
    print img.shape[1]
    print img.shape
    minLineLength=100
    lines = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/180, threshold=100,lines= np.array([]), minLineLength=minLineLength,maxLineGap=40)

            
    line=[]
    if len(lines)!=0:
        a,b,c = lines.shape
        for i in range(a):
            x1=lines[i][0][0]
            y1=lines[i][0][1]
            x2=lines[i][0][2]
            y2=lines[i][0][3]
            
            if x2-x1!=0:
                m=float(y2-y1)/float(x2-x1)
                print "slope : ",m
                if m>1 or m<-1:
                    line.append(((x1,y1,x2,y2),distance(x1,y1,x2,y2),m))
                    print "(x1,y1),(x2,y2) , slope : ",x1,y1,x2,y2,m
                    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 1, cv2.LINE_AA)
                    
            else:
                print "(x1,y1),(x2,y2) : ",x1,y1,x2,y2
        #print "lines : ",line
        bigline=max(line,key=lambda item:item[1])    
        print "bigline : ",bigline
        c=intercept(bigline[0][0],bigline[0][1],bigline[2])
        y=0
        print "slope and intercept of biggest line : ",bigline[2],c
        x=int(-c/bigline[2])
        print "x of biggest line : ",x
        
        if bigline[0][1]>bigline[0][3]:
            point1=(x,y)
            point2=(bigline[0][0], h)
        else:
            point1=(x,y)
            point2=(bigline[0][2], h)
            
            
        cv2.line(img, point1,point2, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imwrite('houghlines5.jpg',img)
        
        cv2.imshow("lines",img)
        #cv2.imshow("edges",edges)
        if cv2.waitKey(0)==27:
            cv2.destroyAllWindows()
        return point1,point2
    print "No lines detected"
    return 0,0