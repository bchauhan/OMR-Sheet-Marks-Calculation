from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm, cm
from reportlab.pdfgen import canvas
from reportlab.platypus import Image, Paragraph, Table
from reportlab.lib import colors
import csv
import datetime
from models import StudentRegister
import matplotlib.pyplot as plt
import numpy as np


class pdfFormat:
    def __init__(self, allMarkedAnswers, scores):
        ##print " value-------pdfFormat1---------:"
        self.allMarkedAnswers = allMarkedAnswers
        self.scores = scores

    def drawGraph(self, username):
        data_1 = list(csv.reader(open('test.csv')))
        ##print " value-------pdfFormat2---------:"
        # print data_1
        English = []
        x = self.scores[0]
        for i in range(0, len(data_1)):
            if (int(data_1[i][0])) <= x:
                ##print " value-------pdfFormat3---------:"
                English.append(int(data_1[i][0]))
                ##print " value1---------:" + str(data_1[i][1])
                English.append(data_1[i][1])
                ##print " value-------2---------:" + str(English[-1])
                ##print "---------score : " + str(x)
        data_2 = list(csv.reader(open('math_test.csv')))
        Math = []
        x = self.scores[1]
        for i in range(0, len(data_2)):
            if (int(data_2[i][0]) <= x):
                Math.append(data_2[i][0])
                Math.append(data_2[i][1])
        data_3 = list(csv.reader(open('reading_test.csv')))
        Reading = []
        x = self.scores[2]
        for i in range(0, len(data_3)):
            if (int(data_3[i][0]) <= x):
                Reading.append(data_3[i][0])
                Reading.append(data_3[i][1])
        data_4 = list(csv.reader(open('science_test.csv')))
        Science = []
        x = self.scores[3]
        for i in range(0, len(data_4)):
            if (int(data_4[i][0]) <= x):
                Science.append(data_4[i][0])
                Science.append(data_4[i][1])
        total = int(English[-1]) + int(Math[-1]) + int(Reading[-1]) + int(Science[-1])
        c = canvas.Canvas('example.pdf', pagesize=A4)  # alternatively use bottomup=False
        width, height = A4
        # del(list)


        c.drawImage('logo.png', 20, 750)
        c.setFont('Helvetica', 30)
        c.drawString(180, 700, "Test Results")
        today = datetime.date.today()
        Email=StudentRegister.objects.get(Username=username).Email
        Phone = StudentRegister.objects.get(Username=username).Phone

        data = [["Diagnostic Test Assessment"],
                ["Name :", username],
                ["Date :", today],
                ["Phone :", Email],
                ["Email :", Phone],
                ]

        table = Table(data)
        table.setStyle([("VALIGN", (0, 0), (1, 1), "MIDDLE"),
                        ("ALIGN", (0, 0), (1, 1), "LEFT"),
                        ('INNERGRID', (0, 0), (1, 1), 0.25, colors.white),
                        ('BOX', (0, 0), (1, 1), 0.25, colors.white)])

        table.wrapOn(c, width, height)
        table.drawOn(c, 20 * mm, 195 * mm)

        data_score = [[" ", "English", "Math", "Reading", "Science", "Total"],
                      ["Score", English[-1], Math[-1], Reading[-1], Science[-1], total]]
        table1 = Table(data_score)
        table1.setStyle([("VALIGN", (0, 0), (1, 1), "MIDDLE"),
                         ("ALIGN", (0, 0), (1, 1), "LEFT"),
                         ('INNERGRID', (0, 0), (1, 1), 0.25, colors.white),
                         ('BOX', (0, 0), (1, 1), 0.25, colors.white)])

        table1.wrapOn(c, width, height)
        table1.drawOn(c, 20 * mm, 155 * mm)

        styles = getSampleStyleSheet()
        c.showPage()
        data1 = [
            ["Diagnostic Test: English"],
            ["Summary"],
            ["Your Score :", English[-1]],
            [" ", " "],
            [" ", " "],
            [" ", " "]
        ]

        table2 = Table(data1)
        table2.setStyle([("VALIGN", (0, 0), (1, 1), "MIDDLE"),
                         ("ALIGN", (0, 0), (1, 1), "LEFT"),
                         ('INNERGRID', (0, 0), (1, 1), 0.25, colors.white),
                         ('BOX', (0, 0), (1, 1), 0.25, colors.white)])

        table2.wrapOn(c, width, height)
        table2.drawOn(c, 20 * mm, 255 * mm)
        data3 = list(csv.reader(open("english1.csv")))

        import pandas as pd
        df = pd.read_csv("english1.csv")
        Question = list(df.Question)
        Correct=list(df.Correct)
        Your_Answers=[]
        Topic = list(df.Topic)
        Difficulty = list(df.Difficulty)
        #Your_Answers.append("Your Answers")
        #Your_Answers.append(" _ ")
        #j=0
        for i in  self.allMarkedAnswers[0:34] :
            #if j < 34:
            Your_Answers.append(i)
           # j+=1
        row=[]
        with open( "english1_n.csv", "wb") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            header=["Question","Correct","Your Answer","Result","Topic","Difficulty",]
            #header = ["Question", "Correct", "Your Answer", "Result", "Topic", "Difficulty", ]
            writer.writerow(header)
            for i in range (0,34):
                print "a1: " + str(Correct[i]) + "   b1 : " + str(Your_Answers[i])
                if Your_Answers[i] == -1:
                    Result = "Omitted"
                elif Correct[i]==Your_Answers[i]:
                    print "a: "+str(Correct[i])+"   b : "+str(Your_Answers[i])
                    Result="Correct"
                else:
                    Result="Incorrect"
                row=[Question[i],Correct[i],Your_Answers[i],Result,Topic[i],Difficulty[i]]
                writer.writerow(row)

        data3 = list(csv.reader(open("english1_n.csv")))

        table3 = Table(data3)
        table3.setStyle([("VALIGN", (0, 0), (1, 1), "MIDDLE"),
                         ("ALIGN", (0, 0), (1, 1), "LEFT"),
                         ('INNERGRID', (0, 0), (1, 1), 0.25, colors.white),
                         ('BOX', (0, 0), (1, 1), 0.25, colors.white)])

        table3.wrapOn(c, width, height)
        table3.drawOn(c, 20 * mm, 20 * mm)
        c.showPage()
        data4 = list(csv.reader(open("english2.csv")))

        import pandas as pd
        df = pd.read_csv("english2.csv")
        Question = list(df.Question)
        Correct = list(df.Correct)
        Your_Answers = []
        Topic = list(df.Topic)
        Difficulty = list(df.Difficulty)
        # Your_Answers.append("Your Answers")
        #Your_Answers.append(" _ ")
        #j = 35
        for i in self.allMarkedAnswers[34:75]:
            #if j <76:
            Your_Answers.append(i)
            #j += 1
        row = []
        with open("english2_n.csv", "wb") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            header = ["Question", "Correct", "Your Answer", "Result", "Topic", "Difficulty", ]
            #header = ["Question", "Correct", "Your Answer", "Result", "Topic", "Difficulty", ]
            writer.writerow(header)
            for i in range(0, 41):
                if Your_Answers[i]==-1:
                    Result="Omitted"
                elif Correct[i] == Your_Answers[i]:
                    Result = "Correct"
                else:
                    Result = "Incorrect"
                row = [Question[i], Correct[i], Your_Answers[i], Result, Topic[i], Difficulty[i]]
                writer.writerow(row)

        data4 = list(csv.reader(open("english2_n.csv")))



        table4 = Table(data4)
        table4.setStyle([("VALIGN", (0, 0), (1, 1), "MIDDLE"),
                         ("ALIGN", (0, 0), (1, 1), "LEFT"),
                         ('INNERGRID', (0, 0), (1, 1), 0.25, colors.white),
                         ('BOX', (0, 0), (1, 1), 0.25, colors.white)])



        table4.wrapOn(c, width, height)
        table4.drawOn(c, 20 * mm, 30 * mm)

        c.showPage()
        import pandas as pd
        import numpy as np
        data = pd.read_csv("edited_act.csv")
        data.head()
        list1 = data['CORRECT']
        list2 = data['LEVEl']
        list3 = self.allMarkedAnswers[0:75]
        countr1 = 0
        countg1 = 0
        countr2 = 0
        countg2 = 0
        countr3 = 0
        countg3 = 0
        countr4 = 0
        countg4 = 0
        countr5 = 0
        countg5 = 0
        countw1 = 0
        countw2 = 0
        countw3 = 0
        countw4 = 0
        countw5 = 0
        for i in range(0, 75):
            print "list2:" + str(list2[i]) + "  list1:" + str(list1[i]) + "   list3:" + str(list3[i])
            if ((list2[i] == 1) & (list3[i] == -1)):
                print "Ommitted added"
                countw1 += 1

            elif ((list2[i] == 1) & (list1[i] != list3[i])):
                countr1 += 1
            elif ((list2[i] == 1) & (list1[i] == list3[i])):
                countg1 += 1

            if ((list2[i] == 2) & (list3[i] == -1)):
                countw2 += 1
                print "Ommitted added"
            elif ((list2[i] == 2) & (list1[i] != list3[i])):
                countr2 += 1

            elif ((list2[i] == 2) & (list1[i] == list3[i])):
                countg2 += 1

            if ((list2[i] == 3) & (list3[i] == -1)):
                print "Ommitted added"
                countw3 += 1
            elif ((list2[i] == 3) & (list1[i] != list3[i])):
                countr3 += 1
            elif ((list2[i] == 3) & (list1[i] == list3[i])):
                countg3 += 1

            if ((list2[i] == 4) & (list3[i] == -1)):
                print "Ommitted added"
                countw4 += 1
            elif ((list2[i] == 4) & (list1[i] != list3[i])):
                countr4 += 1
            elif ((list2[i] == 4) & (list1[i] == list3[i])):
                countg4 += 1

            if ((list2[i] == 5) & (list3[i] == -1)):
                print "Ommitted added"
                countw5 += 1
            elif ((list2[i] == 5) & (list1[i] != list3[i])):
                countr5 += 1
            elif ((list2[i] == 5) & (list1[i] == list3[i])):
                countg5 += 1




# print countr1 + countg1 + countr2 + countg2 + countr3 + countg3 + countr4 + countg4 + countr5 + countg5
        difficulties_level1 = ('1', '2', '3', '4', '5')
        y_pos1 = np.arange(len(difficulties_level1))

        performance1 = [countr1+countg1+countw1,countr2+countg2+countw2,countr3+countg3+countw3,countr4+countg4+countw4,countr5+countg5+countw5]
        performance2 = [countr1 + countg1, countr2 + countg2, countr3 + countg3, countr4 + countg4, countr5 + countg5]
        performance3 = [countg1, countg2, countg3, countg4, countg5]
        print "Performance for English "
        print "performance1"
        print performance1
        print "performance2"
        print performance2
        print "performance3"
        print performance3
        import matplotlib.pyplot as plt
        plt.bar(y_pos1, performance1, align='center', alpha=1, color='Blue')
        plt.bar(y_pos1, performance2, align='center', alpha=1, color='Red')

        plt.bar(y_pos1, performance3, align='center', alpha=1, color='Green')
        plt.xticks(y_pos1, difficulties_level1)
        plt.ylabel('NUMBER OF QUESTION')
        plt.title('PERFORMANCE BY DIFFICULTY')  # step 4
        plt.savefig("English.png")
        # plt.show()
        plt.clf()

        c.drawImage('English.png', 60, 500, 10 * cm, 10 * cm)
        c.showPage()
        data5 = [["Diagnostic Test: Math"],
                 ["Summary"],
                 ["Your Score :", Math[-1]],
                 [" ", " "],
                 [" ", " "],
                 [" ", " "]]
        table5 = Table(data5)
        table5.setStyle([("VALIGN", (0, 0), (1, 1), "MIDDLE"),
                         ("ALIGN", (0, 0), (1, 1), "LEFT"),
                         ('INNERGRID', (0, 0), (1, 1), 0.25, colors.white),
                         ('BOX', (0, 0), (1, 1), 0.25, colors.white)])
        table5.wrapOn(c, width, height)
        table5.drawOn(c, 20 * mm, 255 * mm)


        data6 = list(csv.reader(open("Math.csv")))

        import pandas as pd
        df = pd.read_csv("Math.csv")
        Question = list(df.Question)
        Correct = list(df.Correct)
        Your_Answers = []
        Topic = list(df.Topic)
        Difficulty = list(df.Difficulty)
        # Your_Answers.append("Your Answers")
        #Your_Answers.append(" _ ")
        #j = 76
        for i in self.allMarkedAnswers[75:107]:
            #if j < 108:
            Your_Answers.append(i)
            #j += 1
        row = []
        with open("Math_n.csv", "wb") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            header = ["Question", "Correct", "Your Answer", "Result", "Topic", "Difficulty", ]
            writer.writerow(header)
            for i in range(0, 32):
                if Your_Answers[i]==-1:
                    Result="Omitted"
                elif Correct[i] == Your_Answers[i]:
                    Result = "Correct"
                else:
                    Result = "Incorrect"
                row = [Question[i], Correct[i], Your_Answers[i], Result, Topic[i], Difficulty[i]]
                writer.writerow(row)

        data6 = list(csv.reader(open("Math_n.csv")))

        table6 = Table(data6)
        table6.setStyle([("VALIGN", (0, 0), (1, 1), "MIDDLE"),
                         ("ALIGN", (0, 0), (1, 1), "LEFT"),
                         ('INNERGRID', (0, 0), (1, 1), 0.25, colors.white),
                         ('BOX', (0, 0), (1, 1), 0.25, colors.white)])

        table6.wrapOn(c, width, height)
        table6.drawOn(c, 20 * mm, 30 * mm)
        c.showPage()
        data4 = list(csv.reader(open("Math1.csv")))

        import pandas as pd
        df = pd.read_csv("Math1.csv")
        Question = list(df.Question)
        Correct = list(df.Correct)
        Your_Answers = []
        Topic = list(df.Topic)
        Difficulty = list(df.Difficulty)
        # Your_Answers.append("Your Answers")
        #Your_Answers.append(" _ ")
        #j = 108
        for i in self.allMarkedAnswers[107:135]:
            #if j < 136:
            Your_Answers.append(i)
            #j += 1
        row = []
        with open("Math1_n.csv", "wb") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            header = ["Question", "Correct", "Your Answer", "Result", "Topic", "Difficulty", ]
            writer.writerow(header)
            for i in range(0, 28):
                if Your_Answers[i]==-1:
                    Result="Omitted"
                elif Correct[i] == Your_Answers[i]:
                    Result = "Correct"
                else:
                    Result = "Incorrect"
                row = [Question[i], Correct[i], Your_Answers[i], Result, Topic[i], Difficulty[i]]
                writer.writerow(row)

        data4 = list(csv.reader(open("Math1_n.csv")))

        table4 = Table(data4)
        table4.setStyle([("VALIGN", (0, 0), (1, 1), "MIDDLE"),
                         ("ALIGN", (0, 0), (1, 1), "LEFT"),
                         ('INNERGRID', (0, 0), (1, 1), 0.25, colors.white),
                         ('BOX', (0, 0), (1, 1), 0.25, colors.white)])

        table4.wrapOn(c, width, height)
        table4.drawOn(c, 20 * mm, 70 * mm)
        c.showPage()
        import pandas as pd
        import numpy as np
        data = pd.read_csv("maths_edited.csv")
        data.head()
        list1 = data['CORRECT']
        list2 = data['LEVEl']
        list3 = self.allMarkedAnswers[75:136]
        countr1 = 0
        countg1 = 0
        countr2 = 0
        countg2 = 0
        countr3 = 0
        countg3 = 0
        countr4 = 0
        countg4 = 0
        countr5 = 0
        countg5 = 0
        countw1 = 0
        countw2 = 0
        countw3 = 0
        countw4 = 0
        countw5 = 0
        for i in range(0, 60):
            # print "list2:" + str(list2[i]) + "  list1:" + str(list1[i]) + "   list3:" + str(list3[i])
            print "list2:" + str(list2[i]) + "  list1:" + str(list1[i]) + "   list3:" + str(list3[i])
            if ((list2[i] == 1) & (list3[i] == -1)):
                print "Ommitted added"
                countw1 += 1

            elif ((list2[i] == 1) & (list1[i] != list3[i])):
                countr1 += 1
            elif ((list2[i] == 1) & (list1[i] == list3[i])):
                countg1 += 1

            if ((list2[i] == 2) & (list3[i] == -1)):
                countw2 += 1
                print "Ommitted added"
            elif ((list2[i] == 2) & (list1[i] != list3[i])):
                countr2 += 1

            elif ((list2[i] == 2) & (list1[i] == list3[i])):
                countg2 += 1

            if ((list2[i] == 3) & (list3[i] == -1)):
                print "Ommitted added"
                countw3 += 1
            elif ((list2[i] == 3) & (list1[i] != list3[i])):
                countr3 += 1
            elif ((list2[i] == 3) & (list1[i] == list3[i])):
                countg3 += 1

            if ((list2[i] == 4) & (list3[i] == -1)):
                print "Ommitted added"
                countw4 += 1
            elif ((list2[i] == 4) & (list1[i] != list3[i])):
                countr4 += 1
            elif ((list2[i] == 4) & (list1[i] == list3[i])):
                countg4 += 1

            if ((list2[i] == 5) & (list3[i] == -1)):
                print "Ommitted added"
                countw5 += 1
            elif ((list2[i] == 5) & (list1[i] != list3[i])):
                countr5 += 1
            elif ((list2[i] == 5) & (list1[i] == list3[i])):
                countg5 += 1

        difficulties_level1 = ('1', '2', '3', '4', '5')
        y_pos1 = np.arange(len(difficulties_level1))
        performance4 = [countr1+countg1+countw1,countr2+countg2+countw2,countr3+countg3+countw3,countr4+countg4+countw4,countr5+countg5+countw5]
        performance5 = [countr1 + countg1, countr2 + countg2, countr3 + countg3, countr4 + countg4, countr5 + countg5]
        performance6 = [countg1, countg2, countg3, countg4, countg5]

        # print "performance4"
        # print performance4
        # print "performance5"
        # print performance5
        # print "performance6"
        # print performance6
        import matplotlib.pyplot as plt
        plt.bar(y_pos1, performance4, align='center', alpha=1, color='Blue')
        plt.bar(y_pos1, performance5, align='center', alpha=1, color='Red')
        plt.bar(y_pos1, performance6, align='center', alpha=1, color='Green')
        plt.xticks(y_pos1, difficulties_level1)
        plt.ylabel('NUMBER OF QUESTION')
        plt.title('PERFORMANCE BY DIFFICULTY')  # step 4
        plt.savefig("Math.png")
        plt.clf()
        # plt.show()

        c.drawImage('Math.png', 60, 400, 10 * cm, 10 * cm)
        c.showPage()
        data5 = [["Diagnostic Test: Reading"],
                 ["Summary"],
                 ["Your Score :", Reading[-1]],
                 [" ", " "],
                 [" ", " "],
                 [" ", " "]]

        table5 = Table(data5)
        table5.setStyle([("VALIGN", (0, 0), (1, 1), "MIDDLE"),
                         ("ALIGN", (0, 0), (1, 1), "LEFT"),
                         ('INNERGRID', (0, 0), (1, 1), 0.25, colors.white),
                         ('BOX', (0, 0), (1, 1), 0.25, colors.white)])

        table5.wrapOn(c, width, height)
        table5.drawOn(c, 20 * mm, 255 * mm)
        data6 = list(csv.reader(open("Reading.csv")))
        import pandas as pd
        df = pd.read_csv("Reading.csv")
        Question = list(df.Question)
        Correct = list(df.Correct)
        Your_Answers = []
        Topic = list(df.Topic)
        Difficulty = list(df.Difficulty)
        # Your_Answers.append("Your Answers")
        #Your_Answers.append(" _ ")
        j = 136
        for i in self.allMarkedAnswers[135:167]:
            #if j < 168:
            Your_Answers.append(i)
            #j += 1
        row = []
        with open("Reading_n.csv", "wb") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            header = ["Question", "Correct", "Your Answer", "Result", "Topic", "Difficulty", ]
            writer.writerow(header)
            for i in range(0, 32):
                if Your_Answers[i]==-1:
                    Result="Omitted"
                elif Correct[i] == Your_Answers[i]:
                    Result = "Correct"
                else:
                    Result = "Incorrect"
                row = [Question[i], Correct[i], Your_Answers[i], Result, Topic[i], Difficulty[i]]
                writer.writerow(row)

        data6 = list(csv.reader(open("Reading_n.csv")))
        table6 = Table(data6)
        table6.setStyle([("VALIGN", (0, 0), (1, 1), "MIDDLE"),
                         ("ALIGN", (0, 0), (1, 1), "LEFT"),
                         ('INNERGRID', (0, 0), (1, 1), 0.25, colors.white),
                         ('BOX', (0, 0), (1, 1), 0.25, colors.white)])

        table6.wrapOn(c, width, height)
        table6.drawOn(c, 20 * mm, 40 * mm)
        c.showPage()
        data4 = list(csv.reader(open("Reading1.csv")))

        import pandas as pd
        df = pd.read_csv("Reading1.csv")
        Question = list(df.Question)
        Correct = list(df.Correct)
        Your_Answers = []
        Topic = list(df.Topic)
        Difficulty = list(df.Difficulty)
        # Your_Answers.append("Your Answers")
        #Your_Answers.append(" _ ")
        #j = 168
        for i in self.allMarkedAnswers[167:175]:
            #if j < 176:
            Your_Answers.append(i)
            #j += 1
        row = []
        with open("Reading1_n.csv", "wb") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            header = ["Question", "Correct", "Your Answer", "Result", "Topic", "Difficulty", ]
            writer.writerow(header)
            for i in range(0, 8):
                if Your_Answers[i]==-1:
                    Result="Omitted"
                elif Correct[i] == Your_Answers[i]:
                    Result = "Correct"
                else:
                    Result = "Incorrect"
                row = [Question[i], Correct[i], Your_Answers[i], Result, Topic[i], Difficulty[i]]
                writer.writerow(row)

        data4 = list(csv.reader(open("Reading1_n.csv")))

        table4 = Table(data4)
        table4.setStyle([("VALIGN", (0, 0), (1, 1), "MIDDLE"),
                         ("ALIGN", (0, 0), (1, 1), "LEFT"),
                         ('INNERGRID', (0, 0), (1, 1), 0.25, colors.white),
                         ('BOX', (0, 0), (1, 1), 0.25, colors.white)])

        table4.wrapOn(c, width, height)
        table4.drawOn(c, 20 * mm, 200 * mm)
        import pandas as pd
        import numpy as np
        data = pd.read_csv("Reading_editted1.csv")
        data.head()

        list1 = data['CORRECT']
        list2 = data['LEVEl']
        list3 = self.allMarkedAnswers[135:176]
        countr1 = 0
        countg1 = 0
        countr2 = 0
        countg2 = 0
        countr3 = 0
        countg3 = 0
        countr4 = 0
        countg4 = 0
        countr5 = 0
        countg5 = 0
        countw1 = 0
        countw2 = 0
        countw3 = 0
        countw4 = 0
        countw5 = 0
        for i in range(0, 40):
            # print "list2:" + str(list2[i]) + "  list1:" + str(list1[i]) + "   list3:" + str(list3[i])

            print "list2:" + str(list2[i]) + "  list1:" + str(list1[i]) + "   list3:" + str(list3[i])
            if ((list2[i] == 1) & (list3[i] == -1)):
                print "Ommitted added"
                countw1 += 1

            elif ((list2[i] == 1) & (list1[i] != list3[i])):
                countr1 += 1
            elif ((list2[i] == 1) & (list1[i] == list3[i])):
                print "Correct added"
                countg1 += 1

            if ((list2[i] == 2) & (list3[i] == -1)):
                countw2 += 1
                print "Ommitted added"
            elif ((list2[i] == 2) & (list1[i] != list3[i])):
                countr2 += 1

            elif ((list2[i] == 2) & (list1[i] == list3[i])):
                print "Correct added"
                countg2 += 1

            if ((list2[i] == 3) & (list3[i] == -1)):
                print "Ommitted added"
                countw3 += 1
            elif ((list2[i] == 3) & (list1[i] != list3[i])):
                countr3 += 1
            elif ((list2[i] == 3) & (list1[i] == list3[i])):
                print "Correct added"
                countg3 += 1

            if ((list2[i] == 4) & (list3[i] == -1)):
                print "Ommitted added"
                countw4 += 1
            elif ((list2[i] == 4) & (list1[i] != list3[i])):
                countr4 += 1
            elif ((list2[i] == 4) & (list1[i] == list3[i])):
                print "Correct added"
                countg4 += 1

            if ((list2[i] == 5) & (list3[i] == -1)):
                print "Ommitted added"
                countw5 += 1
            elif ((list2[i] == 5) & (list1[i] != list3[i])):
                countr5 += 1
            elif ((list2[i] == 5) & (list1[i] == list3[i])):
                countg5 += 1

        difficulties_level1 = ('1', '2', '3', '4', '5')
        y_pos1 = np.arange(len(difficulties_level1))
        performance9 = [countr1+countg1+countw1,countr2+countg2+countw2,countr3+countg3+countw3,countr4+countg4+countw4,countr5+countg5+countw5]
        performance8 = [countr1 + countg1, countr2 + countg2, countr3 + countg3, countr4 + countg4, countr5 + countg5]
        performance7 = [countg1, countg2, countg3, countg4, countg5]

        plt.bar(y_pos1, performance9, align='center', alpha=1, color='Blue')
        plt.bar(y_pos1, performance8, align='center', alpha=1, color='Red')
        plt.bar(y_pos1, performance7, align='center', alpha=1, color='Green')


        plt.xticks(y_pos1, difficulties_level1)
        plt.ylabel('NUMBER OF QUESTION')
        plt.title('PERFORMANCE BY DIFFICULTY')  # step 4
        plt.savefig("Reading_editted.png")
        plt.clf()
        # plt.show()

        c.drawImage('Reading_editted.png', 60, 200, 10 * cm, 10 * cm)
        c.showPage()
        data5 = [["Diagnostic Test: Science"],
                 ["Summary"],
                 ["Your Score :", Science[-1]],
                 [" ", " "],
                 [" ", " "],
                 [" ", " "]]

        table5 = Table(data5)
        table5.setStyle([("VALIGN", (0, 0), (1, 1), "MIDDLE"),
                         ("ALIGN", (0, 0), (1, 1), "LEFT"),
                         ('INNERGRID', (0, 0), (1, 1), 0.25, colors.white),
                         ('BOX', (0, 0), (1, 1), 0.25, colors.white)])

        table5.wrapOn(c, width, height)
        table5.drawOn(c, 20 * mm, 255 * mm)
        data6 = list(csv.reader(open("Science.csv")))

        import pandas as pd
        df = pd.read_csv("Science.csv")
        Question = list(df.Question)
        Correct = list(df.Correct)
        Your_Answers = []
        Topic = list(df.Topic)
        Difficulty = list(df.Difficulty)
        # Your_Answers.append("Your Answers")
        #Your_Answers.append(" _ ")
        #j = 176
        for i in self.allMarkedAnswers[175:195]:
            #if j < 196:
            Your_Answers.append(i)
            #j += 1
        row = []
        with open("Science_n.csv", "wb") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            header = ["Question", "Correct", "Your Answer", "Result", "Topic", "Difficulty", ]
            writer.writerow(header)
            for i in range(0, 20):
                if Your_Answers[i]==-1:
                    Result="Omitted"
                elif Correct[i] == Your_Answers[i]:
                    Result = "Correct"
                else:
                    Result = "Incorrect"
                row = [Question[i], Correct[i], Your_Answers[i], Result, Topic[i], Difficulty[i]]
                writer.writerow(row)

        data6 = list(csv.reader(open("Science_n.csv")))

        table6 = Table(data6)
        table6.setStyle([("VALIGN", (0, 0), (1, 1), "MIDDLE"),
                         ("ALIGN", (0, 0), (1, 1), "LEFT"),
                         ('INNERGRID', (0, 0), (1, 1), 0.25, colors.white),
                         ('BOX', (0, 0), (1, 1), 0.25, colors.white)])

        table6.wrapOn(c, width, height)
        table6.drawOn(c, 20 * mm, 90 * mm)
        c.showPage()
        data4 = list(csv.reader(open("Science1.csv")))

        import pandas as pd
        df = pd.read_csv("Science1.csv")
        Question = list(df.Question)
        Correct = list(df.Correct)
        Your_Answers = []
        Topic = list(df.Topic)
        Difficulty = list(df.Difficulty)
        # Your_Answers.append("Your Answers")
        #Your_Answers.append(" _ ")
        #j = 196
        for i in self.allMarkedAnswers[195:215]:
            #if j < 206:
            Your_Answers.append(i)
            #j += 1
        row = []

        print "Your Answer"
        print Your_Answers
        with open("Science1_n.csv", "wb") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            header = ["Question", "Correct", "Your Answer", "Result", "Topic", "Difficulty", ]
            writer.writerow(header)
            for i in range(0, 20):
                print "a1: " + str(Correct[i]) + "   b1 : " + str(Your_Answers[i])
                if Your_Answers[i]==-1:
                    Result="Omitted"
                elif Correct[i] == Your_Answers[i]:
                    Result = "Correct"
                else:
                    Result = "Incorrect"
                row = [Question[i], Correct[i], Your_Answers[i], Result, Topic[i], Difficulty[i]]
                writer.writerow(row)
        data4 = list(csv.reader(open("Science1_n.csv")))
        table4 = Table(data4)
        table4.setStyle([("VALIGN", (0, 0), (1, 1), "MIDDLE"),
                         ("ALIGN", (0, 0), (1, 1), "LEFT"),
                         ('INNERGRID', (0, 0), (1, 1), 0.25, colors.white),
                         ('BOX', (0, 0), (1, 1), 0.25, colors.white)])

        table4.wrapOn(c, width, height)
        table4.drawOn(c, 20 * mm, 150 * mm)
        import pandas as pd
        import numpy as np
        data = pd.read_csv("Science_edited.csv")
        data.head()
        # print data
        list1 = data['CORRECT']
        list2 = data['LEVEl']
        list3 = self.allMarkedAnswers[175:215]
        countr1 = 0
        countg1 = 0
        countr2 = 0
        countg2 = 0
        countr3 = 0
        countg3 = 0
        countr4 = 0
        countg4 = 0
        countr5 = 0
        countg5 = 0
        countw1 = 0
        countw2 = 0
        countw3 = 0
        countw4 = 0
        countw5 = 0
        for i in range(0, 40):
            # print "list2:" + str(list2[i]) + "  list1:" + str(list1[i]) + "   list3:" + str(list3[i])
            print "list2:" + str(list2[i]) + "  list1:" + str(list1[i]) + "   list3:" + str(list3[i])
            if ((list2[i] == 1) & (list3[i] == -1)):
                print "Ommitted added"
                countw1 += 1

            elif ((list2[i] == 1) & (list1[i] != list3[i])):
                countr1 += 1
            elif ((list2[i] == 1) & (list1[i] == list3[i])):
                countg1 += 1

            if ((list2[i] == 2) & (list3[i] == -1)):
                countw2 += 1
                print "Ommitted added"
            elif ((list2[i] == 2) & (list1[i] != list3[i])):
                countr2 += 1

            elif ((list2[i] == 2) & (list1[i] == list3[i])):
                countg2 += 1

            if ((list2[i] == 3) & (list3[i] == -1)):
                print "Ommitted added"
                countw3 += 1
            elif ((list2[i] == 3) & (list1[i] != list3[i])):
                countr3 += 1
            elif ((list2[i] == 3) & (list1[i] == list3[i])):
                countg3 += 1

            if ((list2[i] == 4) & (list3[i] == -1)):
                print "Ommitted added"
                countw4 += 1
            elif ((list2[i] == 4) & (list1[i] != list3[i])):
                countr4 += 1
            elif ((list2[i] == 4) & (list1[i] == list3[i])):
                countg4 += 1

            if ((list2[i] == 5) & (list3[i] == -1)):
                print "Ommitted added"
                countw5 += 1
            elif ((list2[i] == 5) & (list1[i] != list3[i])):
                countr5 += 1
            elif ((list2[i] == 5) & (list1[i] == list3[i])):
                countg5 += 1

        difficulties_level1 = ('1', '2', '3', '4', '5')
        y_pos1 = np.arange(len(difficulties_level1))
        performance10 = [countr1+countg1+countw1,countr2+countg2+countw2,countr3+countg3+countw3,countr4+countg4+countw4,countr5+countg5+countw5]
        performance11 = [countr1 + countg1, countr2 + countg2, countr3 + countg3, countr4 + countg4, countr5 + countg5]
        performance12 = [countg1, countg2, countg3, countg4, countg5]

        plt.bar(y_pos1, performance10, align='center', alpha=1, color='Blue')
        plt.bar(y_pos1, performance11, align='center', alpha=1, color='Red')
        plt.bar(y_pos1, performance12, align='center', alpha=1, color='Green')
        plt.xticks(y_pos1, difficulties_level1)
        plt.ylabel('NUMBER OF QUESTION')
        plt.title('PERFORMANCE BY DIFFICULTY')  # step 4
        plt.savefig("Science.png")
        plt.clf()
        # plt.show()

        c.drawImage('Science.png', 60, 100, 10 * cm, 10 * cm)
        c.save()
