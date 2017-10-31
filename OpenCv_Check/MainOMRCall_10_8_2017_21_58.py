# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 20:45:39 2017

@author: barkh
"""
import studentMarks

#imagename="SCAN1.jpg"
imagename="Untitled3.jpg"

student=studentMarks.StudentMarks(imagename)

#x=student.getmarks()
    
    
  #student = studentMarks.StudentMarks(str(omrsheet))
y = student.checkValidImage()
if y == -1:
    print "Image size is not valid"
    #return render(request, 'registration/OMRFail.html', {})

else:
    x = student.getmarks("Barkha", "b@gmail.com", "2389237439")
if x == -1:
    print "Partitions Not Found"
    #return render(request, 'registration/OMRFail.html', {})
elif x== -2:
    print "One of the ROI has not expected number of bubbles"
    #return render(request, 'registration/OMRFail.html', {})
print "printing marks list "
print"-------------------------"
print x

