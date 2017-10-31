import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from models import *
from django.core.validators import validate_email

class AdminRegistrationForm(forms.ModelForm):
    password1=forms.CharField(widget=forms.PasswordInput, )
    password2 = forms.CharField(widget=forms.PasswordInput,)

    class Meta:
        model = AdminRegister
        fields = ['username','email','password1', 'password2',]


    def clean_email(self):
        email=self.cleaned_data.get('email')
        try:

            match = User.objects.get(email=email)
        except User.DoesNotExist:
            if (not "mail" in email) | (not "@" in email) | (not ".com" in email):
                raise forms.ValidationError("INVALID EMAIL ID")
            return email
        raise forms.ValidationError("Emai is in use")

    def clean(self):
        pwd11=self.cleaned_data.get('password1')
        pwd12 = self.cleaned_data.get('password2')
        if (not pwd11) | (not pwd12):
            raise forms.ValidationError("Password length too small. Required length>=6")
        form_data = self.cleaned_data
        pwd1=form_data['password1']
        pwd2 = form_data['password2']
        if (not pwd1)|(not pwd2):
            raise forms.ValidationError("Password length too small. Required length>=6")
        pwd1=str(pwd1)
        pwd2 = str(pwd2)

        if len(pwd1) < 1 | len(pwd2) < 1:
            raise forms.ValidationError("Password length too small. Required length>=6")
        elif form_data['password1'] != form_data['password2'] :
            raise forms.ValidationError("Password do not match"+str(len(pwd1)))
            del form_data['password']
        return form_data

"""import studentMarks
email=[]
emails=[]
phone=[]
phones=[]
#email=StudentRegister.objects.values_list('Email',flat=True)
email=StudentRegister.objects.values_list('Email')
for em in email:
    l=len(em)
    em=str(em)
    em1=em[3:l-4]
    emails.append(em1)
    print "******em********"+str(em1)

phone=StudentRegister.objects.values_list('Phone')

#phone = instance[0]
for em in phone:
    l=len(em)
    em=str(em)
    em1=em[3:l-4]
    phones.append(em1)
    print "******em********"+str(em1)
names=[]
name=StudentRegister.objects.values_list('Name')
for em in name:
    l=len(em)
    em=str(em)
    em1=em[3:l-4]
    names.append(em1)
    print "******em********"+str(em1)

print "**************************************"
print email
class OmrSubmissionForm(forms.Form):
    #email=forms.ChoiceField(choices=emails,)
    #email=forms.ModelChoiceField(queryset=email)
    #iquery_choices = [('', 'None')] + [(id, id) for id in emails]
    e = forms.ModelChoiceField(queryset=StudentRegister.objects.values_list('Email'))
    print "      eeeeee   ",e
    # iquery_choices = [('', 'None')] + [(id, id) for id in phones]
    phone = forms.ModelChoiceField(queryset=StudentRegister.objects.values_list('Phone'))

    # iquery_choices = [('', 'None')] + [(id, id) for id in names]
    name = forms.ModelChoiceField(queryset=StudentRegister.objects.values_list('Name'))


class Meta:
        model=OMRSubmitModel
        fields=('name','email','phone','omrsheet')"""


class StudentRegisatrationForm(forms.ModelForm):
    Email=forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'validate'}))
    class Meta:
        model = StudentRegister
        fields = ['Name', 'Email', 'Phone']


    def clean_email(self):
        print "Hi I am heree-------------------------"
        email = self.cleaned_data.get('Email')
        if not email:
            raise forms.ValidationError("Invalid email")
            return email
        if (not "mail" in email) | (not "@" in email) | (not ".com" in email):
            raise forms.ValidationError("INVALID EMAIL ID")
            return email

    # Email not valid!


class LoginForm(forms.ModelForm):
    class Meta:
        model=AdminRegister
        fields=('username', 'password1',)

    def clean(self):
        #pwd = self.cleaned_data.get('password')
        username=self.cleaned_data.get('username')
        try:
            match = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("User does not exist")
        return username


    def clean(self):
        password = self.cleaned_data.get('password')
        try:
            match = User.objects.get(password1=password)
        except User.DoesNotExist:
            raise forms.ValidationError("User does not exist")
        return password
class OmrSubmissionForm(forms.ModelForm):
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'validate'}))
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True,max_length=10, validators=[numeric])
    omrsheet = forms.ImageField()

    class Meta:
        model = OMRSubmitModel
        fields = ('name', 'email', 'phone', 'omrsheet')