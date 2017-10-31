from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm,cm
from reportlab.pdfgen import canvas
from reportlab.platypus import Image, Paragraph, Table
from reportlab.lib import colors
import csv
import matplotlib.pyplot as plt


class pdfFormat:
    def _init_(self,allMarkedAnswers, scores):
        self.allMarkedAnswers=allMarkedAnswers
        self.scores=scores
        
    def fun(self):           
        data_1 = list(csv.reader(open('test.csv')))
        English=[]
        x=self.scores[0]
        for i in range(0,len(data_1)):
            if((data_1[i][0])<=x):
                English.append(data_1[i][0])
                English.append(data_1[i][1])
        data_2 = list(csv.reader(open('math_test.csv')))
        Math=[]
        x=self.scores[1]
        for i in range(0,len(data_2)):
            if((data_2[i][0])<=x):
                Math.append(data_2[i][0])
                Math.append(data_2[i][1])
        data_3 = list(csv.reader(open('reading_test.csv')))
        Reading=[]
        x=self.scores[2]
        for i in range(0,len(data_3)):
            if((data_3[i][0])<=x):
                Reading.append(data_3[i][0])
                Reading.append(data_3[i][1])
        data_4 = list(csv.reader(open('science_test.csv')))
        Science=[]
        x=self.scores[3]
        for i in range(0,len(data_4)):
            if((data_4[i][0])<=x):
                Science.append(data_4[i][0])
                Science.append(data_4[i][1])
        total = int(English[-1])+int(Math[-1])+int(Reading[-1])+int(Science[-1])
        c = canvas.Canvas('example.pdf', pagesize=A4)  # alternatively use bottomup=False
        width, height = A4
        #del(list)
        
        data =  [["Diagnostic Test: Assessment"],
        ["Name :"," "],
        ["Date :"," "],
        ["Phone :"," "],
        ["Email :", " "],
        ]
        
        table = Table(data)
        table.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ("ALIGN", (0,0), (-1,-1), "LEFT"),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                        ('BOX',(0,0),(-1,-1),0.25,colors.black)])
        
        table.wrapOn(c, width, height)
        table.drawOn(c, 20*mm, 255*mm)
        data_score = [[" ","English","Math","Reading","Science","Total"],
                      ["Score",English[-1],Math[-1],Reading[-1], Science[-1],total]]
        table1 = Table(data_score)
        table1.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ("ALIGN", (0,0), (-1,-1), "LEFT"),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                        ('BOX',(0,0),(-1,-1),0.25,colors.black)])
        
        table1.wrapOn(c, width, height)
        table1.drawOn(c, 20*mm, 235*mm)
        
        styles = getSampleStyleSheet() 
        c.showPage()
        data1 =  [
        ["Diagnostic Test: English"],
        ["Summary"],
        ["Your Score :", English[-1]],
        ["Correct :"," "],
        ["Incorrect :"," "],
        ["Omitted :"," "]
        ]
        
        table2 = Table(data1)
        table2.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ("ALIGN", (0,0), (-1,-1), "LEFT"),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                        ('BOX',(0,0),(-1,-1),0.25,colors.black)])
        
        table2.wrapOn(c, width, height)
        table2.drawOn(c, 20*mm, 255*mm) 
        data3 =list(csv.reader(open("english1.csv")))
        table3 = Table(data3)
        table3.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ("ALIGN", (0,0), (-1,-1), "LEFT"),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                        ('BOX',(0,0),(-1,-1),0.25,colors.black)])
        
        table3.wrapOn(c, width, height)
        table3.drawOn(c, 20*mm, 20*mm) 
        c.showPage() 
        data4 =list(csv.reader(open("english2.csv")))
        table4 = Table(data4)
        table4.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ("ALIGN", (0,0), (-1,-1), "LEFT"),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                        ('BOX',(0,0),(-1,-1),0.25,colors.black)])
        
        table4.wrapOn(c, width, height)
        table4.drawOn(c, 20*mm, 30*mm)
        c.showPage()
        import pandas as pd
        import numpy as np
        data = pd.read_csv("edited_act.csv")
        data.head()
        list1 = data['CORRECT']
        list2 = data['LEVEl']
        list3=self.allMarkedAnswers[0:75]
        countr1=0
        countg1=0
        countr2=0
        countg2=0
        countr3=0
        countg3=0
        countr4=0
        countg4=0
        countr5=0
        countg5=0
        countw1=0
        countw2=0
        countw3=0
        countw4=0
        countw5=0
        for i in range(0,75):
            if ((list2[i] ==1) &(list1[i] != list3[i])):
                 countr1+=1
            elif((list2[i] ==1) &(list1[i] == list3[i])):
                countg1+=1
            elif((list2[i] ==1) &(list3[i] == 5)):
                countw1+=1
            if ((list2[i] ==2) &(list1[i] != list3[i])):
                 countr2+=1
            elif((list2[i] ==2) &(list1[i] == list3[i])):
                countg2+=1
            elif((list2[i] ==2) &(list3[i] == 5)):
                countw2+=1
            if ((list2[i] ==3) &(list1[i] != list3[i])):
                 countr3+=1
            elif((list2[i] ==3) &(list1[i] == list3[i])):
                countg3+=1
            elif((list2[i] ==3) &(list3[i] == 5)):
                countw3+=1
            if ((list2[i] ==4) &(list1[i] != list3[i])):
                 countr4+=1
            elif((list2[i] ==4) &(list1[i] == list3[i])):
                countg4+=1
            elif((list2[i] ==4) &(list3[i] == 5)):
                countw4+=1
            if ((list2[i] ==5) &(list1[i] != list3[i])):
                 countr5+=1
            elif((list2[i] ==5) &(list1[i] == list3[i])):
                countg5+=1
            elif((list2[i] ==5) &(list3[i] == 5)):
                countw5+=1
        print countr1+countg1+countr2+countg2+countr3+countg3+countr4+countg4+countr5+countg5
        difficulties_level1 = ('1', '2', '3', '4', '5')
        y_pos1= np.arange(len(difficulties_level1))
        performance1 = [countr1+countg1+countw1,countr2+countg2+countw2,countr3+countg3+countw3,countr4+countg4+countw4,countr5+countg5+countw5]
        performance2 = [countr1+countg1,countr2+countg2,countr3+countg3,countr4+countg4,countr5+countg5]
        performance3 = [countg1,countg2,countg3,countg4,countg5]
         
        plt.bar(y_pos1, performance1, align='center', alpha=1,color='Blue')
        plt.bar(y_pos1, performance2, align='center', alpha=1,color='Red')
        plt.bar(y_pos1, performance3, align='center', alpha=1,color='Green')
        plt.xticks(y_pos1, difficulties_level1)
        plt.ylabel('NUMBER OF QUESTION')
        plt.title('PERFORMANCE BY DIFFICULTY')                  # step 4
        plt.savefig("English.png")
        plt.show()
          
        c.drawImage('English.png', 60, 500, 10*cm, 10*cm)
        c.showPage()
        data5 =  [["Diagnostic Test: Math"],
        ["Summary"],
        ["Your Score :",Math[-1]],
        ["Correct :"," "],
        ["Incorrect :"," "],
        ["Omitted :"," "]]
        table5 = Table(data5)
        table5.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ("ALIGN", (0,0), (-1,-1), "LEFT"),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                        ('BOX',(0,0),(-1,-1),0.25,colors.black)])
        table5.wrapOn(c, width, height)
        table5.drawOn(c, 20*mm, 255*mm) 
        data6 =list(csv.reader(open("Math.csv")))
        table6 = Table(data6)
        table6.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ("ALIGN", (0,0), (-1,-1), "LEFT"),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                        ('BOX',(0,0),(-1,-1),0.25,colors.black)])
        
        table6.wrapOn(c, width, height)
        table6.drawOn(c, 20*mm, 30*mm) 
        c.showPage() 
        data4 =list(csv.reader(open("Math1.csv")))
        table4 = Table(data4)
        table4.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ("ALIGN", (0,0), (-1,-1), "LEFT"),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                        ('BOX',(0,0),(-1,-1),0.25,colors.black)])
        
        table4.wrapOn(c, width, height)
        table4.drawOn(c, 20*mm, 70*mm)
        c.showPage() 
        import pandas as pd
        import numpy as np
        data = pd.read_csv("maths_edited.csv")
        data.head()
        list1 = data['ANSWER']
        list2 = data['LEVEl']
        list3=self.allMarkedAnswers[75:135]
        countr1=0
        countg1=0
        countr2=0
        countg2=0
        countr3=0
        countg3=0
        countr4=0
        countg4=0
        countr5=0
        countg5=0
        countw1=0
        countw2=0
        countw3=0
        countw4=0
        countw5=0
        for i in range(0,60):
            if ((list2[i] ==1) &(list1[i] != list3[i])):
                 countr1+=1
            elif((list2[i] ==1) &(list1[i] == list3[i])):
                countg1+=1
            elif((list2[i] ==1) &(list3[i] == 5)):
                countw1+=1
            if ((list2[i] ==2) &(list1[i] != list3[i])):
                 countr2+=1
            elif((list2[i] ==2) &(list1[i] == list3[i])):
                countg2+=1
            elif((list2[i] ==2) &(list3[i] == 5)):
                countw2+=1
            if ((list2[i] ==3) &(list1[i] != list3[i])):
                 countr3+=1
            elif((list2[i] ==3) &(list1[i] == list3[i])):
                countg3+=1
            elif((list2[i] ==3) &(list3[i] == 5)):
                countw3+=1
            if ((list2[i] ==4) &(list1[i] != list3[i])):
                 countr4+=1
            elif((list2[i] ==4) &(list1[i] == list3[i])):
                countg4+=1
            elif((list2[i] ==4) &(list3[i] == 5)):
                countw4+=1
            if ((list2[i] ==5) &(list1[i] != list3[i])):
                 countr5+=1
            elif((list2[i] ==5) &(list1[i] == list3[i])):
                countg5+=1
            elif((list2[i] ==5) &(list3[i] == 5)):
                countw5+=1
        print countr1+countg1+countr2+countg2+countr3+countg3+countr4+countg4+countr5+countg5
         
        difficulties_level1 = ('1', '2', '3', '4', '5')
        y_pos1= np.arange(len(difficulties_level1))
        performance4 = [countr1+countg1+countw1,countr2+countg2+countw2,countr3+countg3+countw3,countr4+countg4+countw4,countr5+countg5+countw5]
        performance5 = [countr1+countg1,countr2+countg2,countr3+countg3,countr4+countg4,countr5+countg5]
        performance6 = [countg1,countg2,countg3,countg4,countg5]
         
        plt.bar(y_pos1, performance4, align='center', alpha=1,color='Blue')
        plt.bar(y_pos1, performance5, align='center', alpha=1,color='Red')
        plt.bar(y_pos1, performance6, align='center', alpha=1,color='Green')
        plt.xticks(y_pos1, difficulties_level1)
        plt.ylabel('NUMBER OF QUESTION')
        plt.title('PERFORMANCE BY DIFFICULTY')                  # step 4
        plt.savefig("Math.png")
        plt.show()
          
        c.drawImage('Math.png', 60, 400, 10*cm, 10*cm)
        c.showPage()
        data5 =  [["Diagnostic Test: Reading"],
        ["Summary"],
        ["Your Score :",Reading[-1]],
        ["Correct :"," "],
        ["Incorrect :"," "],
        ["Omitted :"," "]]
        
        table5 = Table(data5)
        table5.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ("ALIGN", (0,0), (-1,-1), "LEFT"),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                        ('BOX',(0,0),(-1,-1),0.25,colors.black)])
        
        table5.wrapOn(c, width, height)
        table5.drawOn(c, 20*mm, 255*mm) 
        data6 =list(csv.reader(open("Reading.csv")))
        table6 = Table(data6)
        table6.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ("ALIGN", (0,0), (-1,-1), "LEFT"),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                        ('BOX',(0,0),(-1,-1),0.25,colors.black)])
        
        table6.wrapOn(c, width, height)
        table6.drawOn(c, 20*mm, 40*mm) 
        c.showPage() 
        data4 =list(csv.reader(open("Reading1.csv")))
        table4 = Table(data4)
        table4.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ("ALIGN", (0,0), (-1,-1), "LEFT"),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                        ('BOX',(0,0),(-1,-1),0.25,colors.black)])
        
        table4.wrapOn(c, width, height)
        table4.drawOn(c, 20*mm, 200*mm) 
        import pandas as pd
        import numpy as np
        data = pd.read_csv("Reading_editted1.csv")
        data.head()
        
        list1 = data['ANSWER']
        list2 = data['LEVEl']
        list3=self.allMarkedAnswers[135:175]
        countr1=0
        countg1=0
        countr2=0
        countg2=0
        countr3=0
        countg3=0
        countr4=0
        countg4=0
        countr5=0
        countg5=0
        countw1=0
        countw2=0
        countw3=0
        countw4=0
        countw5=0
        for i in range(0,40):
            if ((list2[i] ==1) &(list1[i] != list3[i])):
                 countr1+=1
            elif((list2[i] ==1) &(list1[i] == list3[i])):
                countg1+=1
            elif((list2[i] ==1) &(list3[i] == 5)):
                countw1+=1
            if ((list2[i] ==2) &(list1[i] != list3[i])):
                 countr2+=1
            elif((list2[i] ==2) &(list1[i] == list3[i])):
                countg2+=1
            elif((list2[i] ==2) &(list3[i] == 5)):
                countw2+=1
            if ((list2[i] ==3) &(list1[i] != list3[i])):
                 countr3+=1
            elif((list2[i] ==3) &(list1[i] == list3[i])):
                countg3+=1
            elif((list2[i] ==3) &(list3[i] == 5)):
                countw3+=1
            if ((list2[i] ==4) &(list1[i] != list3[i])):
                 countr4+=1
            elif((list2[i] ==4) &(list1[i] == list3[i])):
                countg4+=1
            elif((list2[i] ==4) &(list3[i] == 5)):
                countw4+=1
            if ((list2[i] ==5) &(list1[i] != list3[i])):
                 countr5+=1
            elif((list2[i] ==5) &(list1[i] == list3[i])):
                countg5+=1
            elif((list2[i] ==5) &(list3[i] == 5)):
                countw5+=1
        print countr1+countg1+countr2+countg2+countr3+countg3+countr4+countg4+countr5+countg5
         
        difficulties_level1 = ('1', '2', '3', '4', '5')
        y_pos1= np.arange(len(difficulties_level1))
        performance9 = [countr1+countg1+countw1,countr2+countg2+countw2,countr3+countg3+countw3,countr4+countg4+countw4,countr5+countg5+countw5]
        performance7 = [countr1+countg1,countr2+countg2,countr3+countg3,countr4+countg4,countr5+countg5]
        performance8 = [countg1,countg2,countg3,countg4,countg5]
         
        plt.bar(y_pos1, performance9, align='center', alpha=1,color='Blue')
        plt.bar(y_pos1, performance7, align='center', alpha=1,color='Red')
        plt.bar(y_pos1, performance8, align='center', alpha=1,color='Green')
        plt.xticks(y_pos1, difficulties_level1)
        plt.ylabel('NUMBER OF QUESTION')
        plt.title('PERFORMANCE BY DIFFICULTY')                  # step 4
        plt.savefig("Reading_editted.png")
        plt.show()
          
        c.drawImage('Reading_editted.png', 60, 200, 10*cm, 10*cm)
        c.showPage()
        data5 =  [["Diagnostic Test: Science"],
        ["Summary"],
        ["Your Score :",Science[-1]],
        ["Correct :"," "],
        ["Incorrect :"," "],
        ["Omitted :"," "]]
        
        table5 = Table(data5)
        table5.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ("ALIGN", (0,0), (-1,-1), "LEFT"),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                        ('BOX',(0,0),(-1,-1),0.25,colors.black)])
        
        table5.wrapOn(c, width, height)
        table5.drawOn(c, 20*mm, 255*mm) 
        data6 =list(csv.reader(open("Science.csv")))
        table6 = Table(data6)
        table6.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ("ALIGN", (0,0), (-1,-1), "LEFT"),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                        ('BOX',(0,0),(-1,-1),0.25,colors.black)])
        
        table6.wrapOn(c, width, height)
        table6.drawOn(c, 20*mm, 90*mm) 
        c.showPage() 
        data4 =list(csv.reader(open("Science1.csv")))
        table4 = Table(data4)
        table4.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ("ALIGN", (0,0), (-1,-1), "LEFT"),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                        ('BOX',(0,0),(-1,-1),0.25,colors.black)])
        
        table4.wrapOn(c, width, height)
        table4.drawOn(c, 20*mm, 150*mm) 
        import pandas as pd
        import numpy as np
        data = pd.read_csv("Science_edited.csv")
        data.head()
        print data
        list1 = data['ANSWER']
        list2 = data['LEVEl']
        list3=self.allMarkedAnswers[175:215]
        countr1=0
        countg1=0
        countr2=0
        countg2=0
        countr3=0
        countg3=0
        countr4=0
        countg4=0
        countr5=0
        countg5=0
        countw1=0
        countw2=0
        countw3=0
        countw4=0
        countw5=0
        for i in range(0,40):
            if ((list2[i] ==1) &(list1[i] != list3[i])):
                 countr1+=1
            elif((list2[i] ==1) &(list1[i] == list3[i])):
                countg1+=1
            elif((list2[i] ==1) &(list3[i] == 5)):
                countw1+=1
            if ((list2[i] ==2) &(list1[i] != list3[i])):
                 countr2+=1
            elif((list2[i] ==2) &(list1[i] == list3[i])):
                countg2+=1
            elif((list2[i] ==2) &(list3[i] == 5)):
                countw2+=1
            if ((list2[i] ==3) &(list1[i] != list3[i])):
                 countr3+=1
            elif((list2[i] ==3) &(list1[i] == list3[i])):
                countg3+=1
            elif((list2[i] ==3) &(list3[i] == 5)):
                countw3+=1
            if ((list2[i] ==4) &(list1[i] != list3[i])):
                 countr4+=1
            elif((list2[i] ==4) &(list1[i] == list3[i])):
                countg4+=1
            elif((list2[i] ==4) &(list3[i] == 5)):
                countw4+=1
            if ((list2[i] ==5) &(list1[i] != list3[i])):
                 countr5+=1
            elif((list2[i] ==5) &(list1[i] == list3[i])):
                countg5+=1
            elif((list2[i] ==5) &(list3[i] == 5)):
                countw5+=1
        print countr1+countg1+countr2+countg2+countr3+countg3+countr4+countg4+countr5+countg5
         
        difficulties_level1 = ('1', '2', '3', '4', '5')
        y_pos1= np.arange(len(difficulties_level1))
        performance10 = [countr1+countg1+countw1,countr2+countg2+countw2,countr3+countg3+countw3,countr4+countg4+countw4,countr5+countg5+countw5]
        performance11 = [countr1+countg1,countr2+countg2,countr3+countg3,countr4+countg4,countr5+countg5]
        performance12 = [countg1,countg2,countg3,countg4,countg5]
         
        plt.bar(y_pos1, performance10, align='center', alpha=1,color='Blue')
        plt.bar(y_pos1, performance11, align='center', alpha=1,color='Red')
        plt.bar(y_pos1, performance12, align='center', alpha=1,color='Green')
        plt.xticks(y_pos1, difficulties_level1)
        plt.ylabel('NUMBER OF QUESTION')
        plt.title('PERFORMANCE BY DIFFICULTY')                  # step 4
        plt.savefig("Science.png")
        plt.show()
          
        c.drawImage('Science.png', 60, 100, 10*cm, 10*cm)
        c.save()
