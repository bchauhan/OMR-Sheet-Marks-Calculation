from __future__ import unicode_literals

from django.db import models
from PIL import Image
from django.core.validators import RegexValidator


alpha = RegexValidator(r'^[a-zA-Z\s]*$', 'Name: Only alphabets are allowed.')
numeric = RegexValidator(r'^[0-9]*$', 'Phone: Invalid Phone Number')

# Create your models here.
class AdminRegister(models.Model):
    #alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    username = models.CharField(max_length=200, primary_key=True, validators=[alpha])
    email = models.CharField(max_length=200, validators=[alpha])
    password1 = models.CharField(max_length=200, )
    password2 = models.CharField(max_length=200, )


    def __unicode__(self):
        return self.username


import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class StudentRegister(models.Model):
    #Username=models.CharField(max_length=200, primary_key=True,)
    Username = models.AutoField(primary_key=True,unique=True)
    Name = models.CharField(max_length=200, default="xyz", validators=[alpha])
    #RollNo = models.CharField(max_length=10, default="xyz", )
    #Class = models.CharField(max_length=15, default="xyz",)
    Email = models.CharField(max_length=30,)
    Phone=models.CharField(max_length=10, default="1234567890",validators=[numeric], unique=True)
    #Username=str(Name)+"_"+str(Phone)+"_"+str(Email)
    #inventory = models.ManyToManyField(Item, through='Inventory')

    def __unicode__(self):
        #return self.Name
        return self.Name

    @property
    def Email1(self):
      return self.Email 

    """@property
    def RollNo1(self):
      return self.RollNo"""

"""class OMRSubmitModel(models.Model):
    id = models.AutoField(primary_key=True, default=1)
    #username_id = models.ForeignKey(StudentRegister,on_delete=models.CASCADE, default="name")
    #student = models.ForeignKey(StudentRegister, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related") #"%(app_label)s_%(class)s_related"
    Email = models.CharField(max_length=30,default="----")#StudentRegister.objects.values_list('Email', flat=True)

    phone=models.CharField(max_length=30,default="---")
    Name = models.CharField(max_length=200, default="xyz",)

    #name=models.CharField(max_length=30,default="xyz",)

    omrsheet=models.ImageField(blank=False,)"""
class OMRSubmitModel(models.Model):
    id = models.AutoField(primary_key=True, default=1)
    #username_id = models.ForeignKey(StudentRegister,on_delete=models.CASCADE, default="name")
    #student = models.ForeignKey(StudentRegister, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related") #"%(app_label)s_%(class)s_related"
    Email = models.CharField(max_length=30, )#StudentRegister.objects.values_list('Email', flat=True)

    Phone = models.CharField(max_length=10, default="1234567890", validators=[numeric])
    Name = models.CharField(max_length=200, default="xyz", validators=[alpha])

    #name=models.CharField(max_length=30,default="xyz",)

    omrsheet=models.ImageField(blank=False,)

