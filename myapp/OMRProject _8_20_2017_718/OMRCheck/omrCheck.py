from imutils import contours
import numpy as np
import cv2


# Loading OMR sheet
# def calCulateMarks(ROI)

class ClassCalculateMarks:
    def checkValidROI(self,ROI, circles):
        if ROI is "016540.jpg" and circles!=52:
            return -1
        elif ROI is "116540.jpg"and circles!=52:
            return -1
        elif ROI is "216540.jpg"and circles!=52:
            return -1
        elif ROI is "316540.jpg"and circles!=52:
            return -1
        elif ROI is "416540.jpg"and circles!=52:
            return -1

        elif ROI is "516540.jpg"and circles!=40:
            return -1
        ###############  math #######################
        elif ROI is "016541.jpg"and circles!=50:
            return -1
        elif ROI is "116541.jpg"and circles!=50:
            return -1
        elif ROI is "216541.jpg"and circles!=50:
            return -1
        elif ROI is "316541.jpg"and circles!=50:
            return -1
        elif ROI is "416541.jpg"and circles!=50:
            return -1
        elif ROI is "516541.jpg"and circles!=50:
            return -1
        ###############  reading #######################
        elif ROI is "016542.jpg"and circles!=28:
            return -1
        elif ROI is "116542.jpg"and circles!=28:
            return -1
        elif ROI is "216542.jpg"and circles!=28:
            return -1
        elif ROI is "316542.jpg"and circles!=28:
            return -1
        elif ROI is "416542.jpg"and circles!=28:
            return -1
        elif ROI is "516542.jpg"and circles!=20:
            return -1
        ###############  science #######################
        elif ROI is "016543.jpg"and circles!=28:
            return -1
        elif ROI is "116543.jpg"and circles!=28:
            return -1
        elif ROI is "216543.jpg"and circles!=28:
            return -1
        elif ROI is "316543.jpg"and circles!=28:
            return -1
        elif ROI is "416543.jpg"and circles!=28:
            return -1
        elif ROI is "516543.jpg"and circles!=20:
            return -1

    def calculateMarks(self, ROI):
        # print "ROI recieved in OMRcheck.py  : "+ROI
        ANSWER_KEY = {0: 3, 1: 2, 2: 3, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 1, 9: 2, 10: 2, 11: 2, 12: 3}

        #######################################################################
        ###############  english #######################
        if ROI is "016540.jpg":
            ANSWER_KEY = {0: 3, 1: 2, 2: 3, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 1, 9: 2, 10: 2, 11: 2, 12: 3}
        elif ROI is "116540.jpg":
            ANSWER_KEY = {0: 3, 1: 2, 2: 3, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 1, 9: 2, 10: 2, 11: 2, 12: 3}
        elif ROI is "216540.jpg":
            ANSWER_KEY = {0: 3, 1: 2, 2: 3, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 1, 9: 2, 10: 2, 11: 2, 12: 3}
        elif ROI is "316540.jpg":
            ANSWER_KEY = {0: 3, 1: 2, 2: 3, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 1, 9: 2, 10: 2, 11: 2, 12: 3}
        elif ROI is "416540.jpg":
            ANSWER_KEY = {0: 3, 1: 2, 2: 3, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 1, 9: 2, 10: 2, 11: 2, 12: 3}
        elif ROI is "516540.jpg":
            ANSWER_KEY = {0: 3, 1: 2, 2: 3, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 1, 9: 2}
        ###############  math #######################
        elif ROI is "016541.jpg":
            ANSWER_KEY = {0: 3, 1: 2, 2: 3, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 1, 9: 2}
        elif ROI is "116541.jpg":
            ANSWER_KEY = {0: 3, 1: 2, 2: 3, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 1, 9: 2}
        elif ROI is "216541.jpg":
            ANSWER_KEY = {0: 3, 1: 2, 2: 3, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 1, 9: 2}
        elif ROI is "316541.jpg":
            ANSWER_KEY = {0: 3, 1: 2, 2: 3, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 1, 9: 2}
        elif ROI is "416541.jpg":
            ANSWER_KEY = {0: 3, 1: 2, 2: 3, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 1, 9: 2}
        elif ROI is "516541.jpg":
            ANSWER_KEY = {0: 3, 1: 2, 2: 3, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 1, 9: 2}
        ###############  reading #######################
        elif ROI is "016542.jpg":
            ANSWER_KEY = {0: 3, 1: 2, 2: 3, 3: 2, 4: 2, 5: 2, 6: 2}
        elif ROI is "116542.jpg":
            ANSWER_KEY = {0: 3, 1: 2, 2: 3, 3: 2, 4: 2, 5: 2, 6: 2}
        elif ROI is "216542.jpg":
            ANSWER_KEY = {0: 3, 1: 2, 2: 3, 3: 2, 4: 2, 5: 2, 6: 2}
        elif ROI is "316542.jpg":
            ANSWER_KEY = {0: 3, 1: 2, 2: 3, 3: 2, 4: 2, 5: 2, 6: 2}
        elif ROI is "416542.jpg":
            ANSWER_KEY = {0: 3, 1: 2, 2: 3, 3: 2, 4: 2, 5: 2, 6: 2}
        elif ROI is "516542.jpg":
            ANSWER_KEY = {0: 3, 1: 2, 2: 3, 3: 2, 4: 2}
        ###############  science #######################
        elif ROI is "016543.jpg":
            ANSWER_KEY = {0: 3, 1: 3, 2: 3, 3: 2, 4: 2, 5: 2, 6: 2}
        elif ROI is "116543.jpg":
            ANSWER_KEY = {0: 3, 1: 3, 2: 3, 3: 2, 4: 2, 5: 2, 6: 2}
        elif ROI is "216543.jpg":
            ANSWER_KEY = {0: 3, 1: 2, 2: 3, 3: 2, 4: 4, 5: 2, 6: 1}
        elif ROI is "316543.jpg":
            ANSWER_KEY = {0: 3, 1: 2, 2: 3, 3: 2, 4: 2, 5: 2, 6: 2}
        elif ROI is "416543.jpg":
            ANSWER_KEY = {0: 3, 1: 2, 2: 3, 3: 2, 4: 2, 5: 2, 6: 2}
        elif ROI is "516543.jpg":
            ANSWER_KEY = {0: 3, 1: 2, 2: 3, 3: 2, 4: 2}
        #######################################################################
        if ROI.find("16541") > 0:
            length = 5
        else:
            length = 4
        print "---------------------Length : " + str(length)
        image = cv2.imread(ROI)
        kernel = np.ones((3, 3), np.uint8)
        image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
        TotalQstn = 7.0
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, thresh1 = cv2.threshold(gray, 210, 255, cv2.THRESH_BINARY)

        thresh = cv2.threshold(thresh1, 200, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        # cv2.imwrite(ROI+"_.jpg",thresh)
        print "--------------roi written---"
        # thresh = cv2.dilate(thresh,kernel,iterations = 1)

        # finding for all contours in image

        cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        sum = 0
        circles = []  # array for storing all bubbles

        if len(cnts) > 0:
            print "------Total contours---------" + str(len(cnts))
        else:
            print "---------blank------"
        for cn in cnts:
            area = cv2.contourArea(cn)
            if area > 100:
                (x, y, w, h) = cv2.boundingRect(cn)
                # print "bounding rect"
                # print cv2.boundingRect(cn)
                if w >= 22 and h >= 16 and w < 35 and w > h:  # suitable condition for detecting circle
                    circles.append(cn)  # storing bubble contour
        TotalQstn = len(circles) / length
        sum += TotalQstn
        print "Total qns : " + str(sum)
        #cv2.drawContours(image, circles, -1, (255, 0, 0), 3)

        # print "number of circles = :"+str(len(circles))
        # if ROI.find("41654")>0:
        # cv2.imshow(ROI,image)

        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        # initilize correct variavle to store correct answers
        correct = 0

        # define your answer key
        circles = contours.sort_contours(circles, method="top-to-bottom")[0]
        v=self.checkValidROI(ROI,circles)
        if v==-1:
            return -1, -1, -1
        marked = []
        for (q, i) in enumerate(np.arange(0, len(circles), length)):
            cnts = contours.sort_contours(circles[i:i + length])[0]
            # initialize bubble
            bubbled = None
            for (j, c) in enumerate(cnts):
                # define proper mask to define to find non-zero(white) pixels
                mask = np.zeros(thresh.shape, dtype="uint8")
                cv2.drawContours(mask, [c], -1, 25, -1)
                mask = cv2.bitwise_and(thresh, thresh, mask=mask)

                # total=no of white pixels in contour/current bubble
                total = cv2.countNonZero(mask)

                # compare new total with its previous value
                if bubbled is None or total > bubbled[0]:

                    bubbled = (total, j)
            print " no of white pixels in bubble : "+str(bubbled[0])
            # color = (0, 0, 255)
            if bubbled[0]<300:
                marked.append(-1)
            else:
                marked.append(bubbled[1])
            k = ANSWER_KEY[q]
            # print "---marked---"
            # print marked
            # if filled bubble is the right answer inrease value of correct
            # draw green circle around bubble

            if k == bubbled[1]:
                # color = (0, 255, 0)
                correct += 1

                # print "correct -  k : "+str(k)+" and bubbled : "+str(bubbled[1])
                # cv2.drawContours(image, [cnts[k]], -1, color, 3)  #green
                # if filled bubble is wrong draw red color on that
                # and draw green on right bubble
        # calculate achived percentage
        score = (correct / TotalQstn) * 100
        # print("[INFO] score: {:.2f}%".format(score))
        cv2.putText(image, "{:.2f}%".format(score), (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        # cv2.imshow(ROI, image)
        # cv2.imwrite("P_"+ROI,image)
        return correct, len(circles), marked

