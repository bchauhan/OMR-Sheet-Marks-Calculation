# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 13:04:06 2017

@author: miracle
"""

import cv2
import datetime
import omrCheck
import pdfGenerator

ccm = omrCheck.ClassCalculateMarks()
import os

print datetime.datetime.now()
print"****************Welcome to OMRsheet Program*******************"


class StudentMarks:
    # imageName="SCAN1.jpg"

    def __init__(self, imagename):
        print "image name : " + imagename

        self.imageName = imagename
        self.img = cv2.imread(self.imageName)
        ret, self.thresh = cv2.threshold(self.img, 127, 255, 0)
        # to create binary of the image make it self.grayscale
        self.gray = cv2.cvtColor(self.thresh, cv2.COLOR_BGR2GRAY)
        self.height, self.width, self.channels = self.img.shape  # Get the self.width and hight of the image for iterating over
        print "Image height : " + str(self.height) + "Image   width : " + str(self.width)


    def checkValidImage(self):
        print "image name : "+self.imageName
        if self.height>2300 and self.height<2400 and  self.width>1600 and self.width<1700:
            print "Image is valid"
        else:
            return -1

    ########################### function : findself.widths() ###########################################
    def findwidths(self, ht0, ht1):

        # print "I am in findself.widths function"
        h = ht0
        w = int(self.width / 9)
        vertical = []
        # contains all unique self.width where black pxl count is least(10)
        vValleys = []
        # traversing self.width wise
        while w < int((9 * self.width) / 10):
            h = ht0
            black = 0
            while h < ht1:
                if self.gray[h, w] == 0:
                    black += 1
                h += 1
            if black < 10:
                vValleys.append(w)
            vertical.append(black)
            w += 1
        vValleyValues = []
        x = vValleys[0]
        vValleyValues.append(x)
        # saving unique value of self.heights with leask black pxl count
        for vt in vValleys:
            if (vt - x > 190):
                vValleyValues.append(vt)
                x = vt
        return vValleyValues

        #######################################################################

    def getmarks(self, username):

        print"image name : " + self.imageName
        h = int(self.height / 6)
        w = 0
        horizontal = []
        HPeaks = []  # contains all heights where black pxl count is least(10)

        # traversing self.height wise
        while h < int((3 * self.height) / 4):
            w = 0
            black = 0
            while w < self.width:
                if self.gray[h, w] == 0:
                    black += 1
                w += 1
            if black > 600:
                HPeaks.append(h)
            horizontal.append(black)
            h += 1
        HPeakValues = []  # will contains all unique self.heights where black pxl count is least(10)
        x = HPeaks[0]
        # append first value
        HPeakValues.append(x)
        # saving unique value of self.heights with leask black pxl count
        for pv in HPeaks:
            if (pv - x > 100):
                HPeakValues.append(pv)
                x = pv
        # printing unique value of self.heights with leask black pxl count
        print "HPeakValues length : "+str(len(HPeakValues))
        widthSets = []

        for i in range(len(HPeakValues) - 1):
            widthSets.append(self.findwidths(HPeakValues[i], HPeakValues[i + 1]))

        print "widthSets length : " + str(len(widthSets))

        if len(HPeakValues)==5 and len(widthSets)==4:
            print "Image partitions are fine"
        else :
            return -1
        hp = 0
        circle = 0
        TotalQstn = 0
        marks = []
        ROINames = []
        # creating the ROIs
        totalMarked = []
        for wsets in widthSets:
            x = 0
            sum = 0
            y = 0
            totalQsn = 0
            for i in range(len(wsets) - 1):
                cv2.rectangle(self.img, (wsets[i], HPeakValues[hp] + 35), (wsets[i + 1] + 10,
                                                                           HPeakValues[hp + 1] - 5), (255, 0, 0), 1)
                ROI = self.gray[HPeakValues[hp] + 35:HPeakValues[hp + 1] + 15, wsets[i]:wsets[i + 1] + 10]
                roiname = str(i) + str(w) + str(hp) + ".jpg"
                ROINames.append(roiname)
                cv2.imwrite(roiname, ROI)
                #v=ccm.checkValidROI(ROI)
                x, y, z = ccm.calculateMarks(roiname)
                if x==-1:
                    print " image invalid some disturbance ion image"
                    return -1
                for zs in z:
                    totalMarked.append(zs)
                sum += x
                totalQsn += y
                os.remove(roiname)
                # circle+=ccm.calculateMarks(roiname)[1]
                # TotalQstn+=ccm.calculateMarks(roiname)[2]
            marks.append(sum)
            hp += 1

        # print "number of TotalQstn = :"+str(totalQsn)
        print "number of TotalQstn = :" + str(len(totalMarked))

        print "------Answers---------"
        print totalMarked
        pdf = pdfGenerator.pdfFormat(totalMarked, marks)
        pdf.drawGraph(username)
        '''    
        print "number of circles = :"+str(circle)


        print "------marks----: "
        print "English : "+str(marks[0])+"/75"
        print "Maths   : "+str(marks[1])+"/60"
        print "Reading : "+str(marks[2])+"/40"
        print "Science : "+str(marks[3])+"/40"
        '''
        return marks
