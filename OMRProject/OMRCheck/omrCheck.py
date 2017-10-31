from imutils import contours
import numpy as np
import cv2


# Loading OMR sheet
# def calCulateMarks(ROI)

class ClassCalculateMarks:
    def checkValidROI(self,ROI, circles):
        print " ROI Recived :"+ROI
        print type(ROI)
        ROI=str(ROI)
        print " Circles Recived : " + str(len(circles))
        print ROI in "016540.jpg"

        ###############  English #######################
        if (ROI in "016540.jpg") and (len(circles)!=52):
            return -1
        elif (ROI in "116540.jpg") and (len(circles)!=52):
            return -1
        elif (ROI in "216540.jpg") and (len(circles)!=52):
            return -1
        elif (ROI in "316540.jpg") and (len(circles)!=52):
            return -1
        elif (ROI in "416540.jpg") and (len(circles)!=52):
            return -1
        elif (ROI in "516540.jpg") and (len(circles)!=40):
            return -1
        ###############  math #######################
        elif (ROI in "016541.jpg") and (len(circles)!=50):
            return -1
        elif (ROI in "116541.jpg") and (len(circles)!=50):
            return -1
        elif (ROI in "216541.jpg") and (len(circles)!=50):
            return -1
        elif (ROI in "316541.jpg") and (len(circles)!=50):
            return -1
        elif (ROI in "416541.jpg") and (len(circles)!=50):
            return -1
        elif (ROI in "516541.jpg") and (len(circles)!=50):
            return -1
        ###############  reading #######################
        elif (ROI in "016542.jpg") and (len(circles)!=28):
            return -1
        elif (ROI in "116542.jpg") and (len(circles)!=28):
            return -1
        elif (ROI in "216542.jpg") and (len(circles)!=28):
            return -1
        elif (ROI in "316542.jpg") and (len(circles)!=28):
            return -1
        elif (ROI in "416542.jpg") and (len(circles)!=28):
            print " --- ROI Recived******************* :" + ROI

            print " ---Circles Recived : " + str(len(circles))

            return -1
        elif (ROI in "516542.jpg") and (len(circles)!=20):
            return -1
        ###############  science #######################
        elif (ROI in "016543.jpg") and (len(circles)!=28):
            return -1
        elif (ROI in "116543.jpg") and (len(circles)!=28):
            return -1
        elif (ROI in "216543.jpg") and (len(circles)!=28):
            return -1
        elif (ROI in "316543.jpg") and (len(circles)!=28):
            return -1
        elif (ROI in "416543.jpg") and (len(circles)!=28):
            return -1
        elif (ROI in "516543.jpg") and (len(circles)!=20):
            return -1
        return 1

    def test1AnswerKey(self,ROI):
        print "Test1 ROI Recived :" + ROI
        print type(ROI)
        ROI = str(ROI)
        #print " Circles Recived : " + str(len(circles))
        print ROI in "016540.jpg"

        ###############  English #######################
        if (ROI in "016540.jpg"):
            ANSWER_KEY016540 = {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 3, 6: 2, 7: 2, 8: 2, 9: 1, 10: 2, 11: 3, 12: 2}
            return ANSWER_KEY016540
        elif (ROI in "116540.jpg"):
            ANSWER_KEY116540 = {0: 2, 1: 3, 2: 2, 3: 0, 4: 1, 5: 3, 6: 2, 7: 3, 8: 1, 9: 2, 10: 3, 11: 3, 12: 2}
            return ANSWER_KEY116540
        elif (ROI in "216540.jpg"):
            ANSWER_KEY216540 = {0: 1, 1: 2, 2: 3, 3: 3, 4: 1, 5: 3, 6: 1, 7: 2, 8: 2, 9: 3, 10: 0, 11: 3, 12: 1}
            return ANSWER_KEY216540
        elif (ROI in "316540.jpg"):
            ANSWER_KEY316540 = {0: 3, 1: 0, 2: 2, 3: 2, 4: 1, 5: 3, 6: 1, 7: 1, 8: 2, 9: 3, 10: 1, 11: 2, 12: 1}
            return ANSWER_KEY316540
        elif (ROI in "416540.jpg"):
            ANSWER_KEY416540 = {0: 1, 1: 3, 2: 2, 3: 2, 4: 2, 5: 2, 6: 3, 7: 3, 8: 1, 9: 2, 10: 3, 11: 3, 12: 2}
            return ANSWER_KEY416540
        elif (ROI in "516540.jpg"):
            ANSWER_KEY516540 = {0: 3, 1: 2, 2: 2, 3: 1, 4: 2, 5: 3, 6: 3, 7: 3, 8: 2, 9: 3}
            return ANSWER_KEY516540

            ###############  math #######################
        elif (ROI in "016541.jpg") :
            ANSWER_KEY016541 = {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 3, 6: 2, 7: 2, 8: 2, 9: 1}
            return ANSWER_KEY016541
        elif (ROI in "116541.jpg") :
            ANSWER_KEY116541 = {0: 2, 1: 3, 2: 2, 3: 2, 4: 3, 5: 2, 6: 0, 7: 1, 8: 3, 9: 2}
            return ANSWER_KEY116541
        elif (ROI in "216541.jpg") :
            ANSWER_KEY216541 = {0: 3, 1: 1, 2: 2, 3: 3, 4: 3, 5: 2, 6: 1, 7: 2, 8: 3, 9: 3}
            return ANSWER_KEY216541
        elif (ROI in "316541.jpg") :
            ANSWER_KEY316541 = {0: 1, 1: 3, 2: 1, 3: 2, 4: 2, 5: 3, 6: 0, 7: 3, 8: 1, 9: 3}
            return ANSWER_KEY316541
        elif (ROI in "416541.jpg") :
            ANSWER_KEY416541 = {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 3, 6: 2, 7: 2, 8: 2, 9: 1}
            return ANSWER_KEY416541
        elif (ROI in "516541.jpg") :
            ANSWER_KEY516541 = {0: 2, 1: 3, 2: 2, 3: 2, 4: 3, 5: 2, 6: 0, 7: 1, 8: 0, 9: 1}
            return ANSWER_KEY516541
        ###############  reading #######################
        elif (ROI in "016542.jpg") :
            ANSWER_KEY016542 = {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 3, 6: 2}
            return ANSWER_KEY016542
        elif (ROI in "116542.jpg") :
            ANSWER_KEY116542 = {0: 2, 1: 2, 2: 1, 3: 2, 4: 3, 5: 2, 6: 2}
            return ANSWER_KEY116542
        elif (ROI in "216542.jpg") :
            ANSWER_KEY216542 = {0: 3, 1: 2, 2: 0, 3: 1, 4: 2, 5: 2, 6: 1}
            return ANSWER_KEY216542
        elif (ROI in "316542.jpg") :
            ANSWER_KEY316542 = {0: 1, 1: 1, 2: 3, 3: 3, 4: 2, 5: 1, 6: 2}
            return ANSWER_KEY316542
        elif (ROI in "416542.jpg") :
            ANSWER_KEY416542 = {0: 3, 1: 3, 2: 1, 3: 3, 4: 1, 5: 2, 6: 2}
            return ANSWER_KEY416542
        elif (ROI in "516542.jpg") :
            ANSWER_KEY516542 = {0: 3, 1: 0, 2: 3, 3: 1, 4: 3}
            return ANSWER_KEY516542

        ###############  science #######################
        elif (ROI in "016543.jpg") :
            ANSWER_KEY016543 = {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 3, 6: 2}
            return ANSWER_KEY016543
        elif (ROI in "116543.jpg") :
            ANSWER_KEY116543 = {0: 2, 1: 2, 2: 1, 3: 2, 4: 3, 5: 2, 6: 2}
            return ANSWER_KEY116543
        elif (ROI in "216543.jpg") :
            ANSWER_KEY216543 = {0: 3, 1: 2, 2: 0, 3: 1, 4: 3, 5: 3, 6: 1}
            return ANSWER_KEY216543
        elif (ROI in "316543.jpg") :
            ANSWER_KEY316543 = {0: 2, 1: 3, 2: 3, 3: 3, 4: 2, 5: 1, 6: 2}
            return ANSWER_KEY316543
        elif (ROI in "416543.jpg") :
            ANSWER_KEY416543 = {0: 3, 1: 3, 2: 1, 3: 3, 4: 1, 5: 2, 6: 2}
            return ANSWER_KEY416543
        elif (ROI in "516543.jpg") :
            ANSWER_KEY516543 = {0: 3, 1: 0, 2: 3, 3: 1, 4: 3}
            return ANSWER_KEY516543


    def test2AnswerKey(self,ROI):
        print " Test 2 ROI Recived :" + ROI
        print type(ROI)
        ROI = str(ROI)
        #print " Circles Recived : " + str(len(circles))
        print ROI in "016540.jpg"

        ###############  English #######################
        if (ROI in "016540.jpg"):
            ANSWER_KEY016540 = {0: 0, 1: 1, 2: 2, 3: 2, 4: 1, 5: 3, 6: 2, 7: 3, 8: 1, 9: 0, 10: 3, 11: 0, 12: 0}
            return ANSWER_KEY016540
        elif (ROI in "116540.jpg"):
            ANSWER_KEY116540 = {0: 1, 1: 3, 2: 0, 3: 1, 4: 0, 5: 1, 6: 1, 7: 1, 8: 2, 9: 3, 10: 2, 11: 3, 12: 0}
            return ANSWER_KEY116540
        elif (ROI in "216540.jpg"):
            ANSWER_KEY216540 = {0: 3, 1: 1, 2: 3, 3: 0, 4: 0, 5: 2, 6: 0, 7: 3, 8: 1, 9: 0, 10: 2, 11: 2, 12: 3}
            return ANSWER_KEY216540
        elif (ROI in "316540.jpg"):
            ANSWER_KEY316540 = {0: 0, 1: 2, 2: 1, 3: 3, 4: 1, 5: 2, 6: 0, 7: 2, 8: 3, 9: 0, 10: 1, 11: 2, 12: 3}
            return ANSWER_KEY316540
        elif (ROI in "416540.jpg"):
            ANSWER_KEY416540 = {0: 3, 1: 2, 2: 3, 3: 2, 4: 0, 5: 2, 6: 3, 7: 0, 8: 0, 9: 2, 10: 1, 11: 3, 12: 0}
            return ANSWER_KEY416540
        elif (ROI in "516540.jpg"):
            ANSWER_KEY516540 = {0: 0, 1: 2, 2: 3, 3: 1, 4: 0, 5: 1, 6: 1, 7: 3, 8: 3, 9: 3}
            return ANSWER_KEY516540

            ###############  math #######################
        elif (ROI in "016541.jpg") :
            ANSWER_KEY016541 = {0: 2, 1: 3, 2: 1, 3: 2, 4: 0, 5: 0, 6: 2, 7: 4, 8: 1, 9: 4}
            return ANSWER_KEY016541
        elif (ROI in "116541.jpg") :
            ANSWER_KEY116541 = {0: 2, 1: 4, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 4, 9: 1}
            return ANSWER_KEY116541
        elif (ROI in "216541.jpg") :
            ANSWER_KEY216541 = {0: 1, 1: 2, 2: 0, 3: 4, 4: 2, 5: 0, 6: 3, 7: 3, 8: 1, 9: 4}
            return ANSWER_KEY216541
        elif (ROI in "316541.jpg") :
            ANSWER_KEY316541 = {0: 4, 1: 1, 2: 3, 3: 0, 4: 1, 5: 0, 6: 4, 7: 1, 8: 3, 9: 1}
            return ANSWER_KEY316541
        elif (ROI in "416541.jpg") :
            ANSWER_KEY416541 = {0: 1, 1: 0, 2: 3, 3: 1, 4: 4, 5: 3, 6: 1, 7: 1, 8: 0, 9: 4}
            return ANSWER_KEY416541
        elif (ROI in "516541.jpg") :
            ANSWER_KEY516541 = {0: 3, 1: 2, 2: 3, 3: 4, 4: 3, 5: 3, 6: 0, 7: 3, 8: 0, 9: 0}
            return ANSWER_KEY516541
        ###############  reading #######################
        elif (ROI in "016542.jpg") :
            ANSWER_KEY016542 = {0: 3, 1: 0, 2: 1, 3: 2, 4: 3, 5: 2, 6: 1}
            return ANSWER_KEY016542
        elif (ROI in "116542.jpg") :
            ANSWER_KEY116542 = {0: 2, 1: 0, 2: 1, 3: 1, 4: 0, 5: 0, 6: 2}
            return ANSWER_KEY116542
        elif (ROI in "216542.jpg") :
            ANSWER_KEY216542 = {0: 2, 1: 0, 2: 1, 3: 2, 4: 3, 5: 0, 6: 0}
            return ANSWER_KEY216542
        elif (ROI in "316542.jpg") :
            ANSWER_KEY316542 = {0: 2, 1: 2, 2: 3, 3: 3, 4: 0, 5: 3, 6: 0}
            return ANSWER_KEY316542
        elif (ROI in "416542.jpg") :
            ANSWER_KEY416542 = {0: 1, 1: 1, 2: 1, 3: 0, 4: 2, 5: 3, 6: 3}
            return ANSWER_KEY416542
        elif (ROI in "516542.jpg") :
            ANSWER_KEY516542 = {0: 2, 1: 1, 2: 0, 3: 1, 4: 3}
            return ANSWER_KEY516542

        ###############  science #######################
        elif (ROI in "016543.jpg") :
            ANSWER_KEY016543 = {0: 1, 1: 0, 2: 0, 3: 2, 4: 3, 5: 1, 6: 3}
            return ANSWER_KEY016543
        elif (ROI in "116543.jpg") :
            ANSWER_KEY116543 = {0: 0, 1: 2, 2: 1, 3: 2, 4: 2, 5: 3, 6: 1}
            return ANSWER_KEY116543
        elif (ROI in "216543.jpg") :
            ANSWER_KEY216543 = {0: 1, 1: 0, 2: 0, 3: 3, 4: 0, 5: 3, 6: 2}
            return ANSWER_KEY216543
        elif (ROI in "316543.jpg") :
            ANSWER_KEY316543 = {0: 2, 1: 2, 2: 1, 3: 3, 4: 1, 5: 1, 6: 3}
            return ANSWER_KEY316543
        elif (ROI in "416543.jpg") :
            ANSWER_KEY416543 = {0: 3, 1: 0, 2: 2, 3: 0, 4: 0, 5: 3, 6: 1}
            return ANSWER_KEY416543
        elif (ROI in "516543.jpg") :
            ANSWER_KEY516543 = {0: 3, 1: 1, 2: 2, 3: 2, 4: 3}
            return ANSWER_KEY516543

    def calculateMarks(self, ROI,Test):
        # print "ROI recieved in OMRcheck.py  : "+ROI
        #ANSWER_KEY = {0: 3, 1: 2, 2: 3, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 1, 9: 2, 10: 2, 11: 2, 12: 3}
        if Test in "Test1":
            ANSWER_KEY=self.test1AnswerKey(ROI)
        elif Test in "Test2":
            ANSWER_KEY = self.test2AnswerKey(ROI)

        print "--------------AK-----------"
        print ANSWER_KEY
        if ROI.find("16541") > 0:
            length = 5
        else:
            length = 4
        #print "---------------------Length : " + str(length)
        image = cv2.imread(ROI)
        kernel = np.ones((3, 3), np.uint8)
        image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
        TotalQstn = 7.0
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, thresh1 = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)
        #thresh1 = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)
        cv2.imwrite("1_"+ROI, thresh1)

        thresh = cv2.threshold(thresh1, 180, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        cv2.imwrite(ROI, thresh)
        cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        sum = 0
        circles = []  # array for storing all bubbles
        '''
        if len(cnts) > 0:
            print "------Total contours---------" + str(len(cnts))
        else:
            print "---------blank------"
        '''
        for cn in cnts:
            area = cv2.contourArea(cn)
            if area > 100:
                (x, y, w, h) = cv2.boundingRect(cn)
                # print "bounding rect"
                # print cv2.boundingRect(cn)
                if w >= 16 and h >= 16 and w < 35 and w > h:  # suitable condition for detecting circle
                    circles.append(cn)  # storing bubble contour
        TotalQstn = len(circles) / length
        sum += TotalQstn
        print "Total qns : " + str(sum)

        circles = contours.sort_contours(circles, method="top-to-bottom")[0]

        v=self.checkValidROI(ROI,circles)
        print " ROI status returned for buuble : "+str(v)
        if v==-1:
            return -2, -1, -1
        marked = []
        correct=0
        for (q, i) in enumerate(np.arange(0, len(circles), length)):
            cnts = contours.sort_contours(circles[i:i + length])[0]
            # initialize bubble
            bubbled = (0,0)
            flag =0
            print"---next---- : "
            for (j, c) in enumerate(cnts):
                # define proper mask to define to find non-zero(white) pixels
                mask = np.zeros(thresh.shape, dtype="uint8")
                cv2.drawContours(mask, [c], -1, 25, -1)
                mask = cv2.bitwise_and(thresh, thresh, mask=mask)

                # total=no of white pixels in contour/current bubble
                total = cv2.countNonZero(mask)
                print "Balck : "+str(total)

                # compare new total with its previous value
                if bubbled is None or total > bubbled[0]:
                    if bubbled[0]>220 and total>220:
                        flag =2
                        break
                    bubbled = (total, j)
            #print " no of white pixels in bubble : "+str(bubbled[0])
            # color = (0, 0, 255)
            if flag == 2:
                marked.append(-2)
                print "Marks added double->>>>>>>>>>>>>>>>> : "+str(total)
            elif bubbled[0]<220:
                marked.append(-1)
                print "Marks added omitted->>>>>>>>>>>>>>>>> : " + str(bubbled[0])
            else:
                marked.append(bubbled[1])
            k = ANSWER_KEY[q]
            # print "---marked---"
            # print marked
            # if filled bubble is the right answer inrease value of correct
            # draw green circle around bubble

            if k == bubbled[1]:
                correct += 1

        score=0
        if TotalQstn>0:
            score = (correct / TotalQstn) * 100
        # print("[INFO] score: {:.2f}%".format(score))
        cv2.putText(image, "{:.2f}%".format(score), (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        # cv2.imshow(ROI, image)
        # cv2.imwrite("P_"+ROI,image)
        return correct, len(circles), marked

