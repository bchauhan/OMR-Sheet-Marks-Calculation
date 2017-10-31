# views.py
from OMRCheck.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from models import AdminRegister,StudentRegister
from django.contrib import messages
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.views.decorators.cache import cache_control
import studentMarks
from django.core.files.storage import FileSystemStorage
import cv2



def index_page(request):
    context = 'context variable'
    return render(request, 'registration/index.html', context)
    #if request.method == 'GET':
    #print 'Hello ...'
     #   return '''Hello String from
     #   index_page...
     #   ....
     #    '''
    #else:
     #   pass

@csrf_protect
def adminRegister(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
            )
            user.save()
            return HttpResponseRedirect('/register/success/')
    else:
        form = AdminRegistrationForm()
    variables = RequestContext(request, {
        'form': form
    })
    return render_to_response(
        'registration/register.html',
        variables,
    )
@login_required(login_url='/login/')
def studentRegister(request):
    if request.method == 'POST':
        formset = StudentRegisatrationForm(request.POST, request.FILES)
        if formset.is_valid():
            obj=StudentRegister()
            #fields = ('Username', 'Name', 'RollNo', 'Class', 'Email', 'Phone')
            '''
            obj.Username = str(formset.cleaned_data['Name'])+str(formset.cleaned_data['Phone'])
            obj.Name = formset.cleaned_data['Name']
            obj.RollNo = formset.cleaned_data['RollNo']
            obj.Class = formset.cleaned_data['Class']
            obj.Email = formset.cleaned_data['Email']
            obj.Phone = formset.cleaned_data['Phone']
            obj.save()
            '''
            #omrsheet = formset.cleaned_data['omrsheet']
            post=formset.save(commit=False)
            post.user=request.user
            post.save()

            return render(request, 'registration/StuRegSuccess.html', {})
        else:
            messages.error(request, "Form is not valid")
    else:
        formset = StudentRegisatrationForm()
    variables = RequestContext(request, {
        'formset': formset
    })
    return render_to_response('registration/studentRegister.html', variables,)

################################################################
"""def omrSubmissionView(request):
    omrForm = OmrSubmissionForm()
    studentForm=StudentRegister.objects.all()
    if request.method=='POST' :
        oform = OmrSubmissionForm(request.POST, request.FILES)
        stuForm=StudentRegisatrationForm(request.POST)
        print "------All stuForm 1--------"
        print stuForm.errors
        if stuForm.is_valid():
            stuForm.Name=stuForm.cleaned_data['Name']
            print "hero---------------------------**************"
            print stuForm.Name

        email=request.POST.get('Email',False)
        name=request.POST.get('Name', False)
        rollno=request.POST.get('RollNo', False)
        print "email -------- name -------- roll no"
        print email
        print rollno
        print name
        print "------All good 1--------"
        print oform.errors
        print "------All good 1.2--------"
	
        if oform.is_valid():
            print "------All good 2--------"

            oform.omrsheet=oform.cleaned_data['omrsheet']
            oform.email = oform.cleaned_data['email']
            oform.name = oform.cleaned_data['name']
            oform.phone = oform.cleaned_data['phone']
            print "image name---------------------------**************"
            print oform.omrsheet
            print oform.email
            print oform.name
            print oform.phone

            print "email name---------------------------**************"
            omrsheet=oform.omrsheet
            #username = omrForm.cleaned_data['username']
            #item=StudentRegister.objects.get(Username=username).Email

            post = oform.save(commit=True)
            post.user = request.user
            post.save()

            name = str(oform.name)
            email = str(oform.email)
            phone = str(oform.phone)
            #query='SELECT username FROM StudentRegister WHERE name="xyz"'
            print email


            #username = StudentRegister.objects.raw('SELECT Username FROM StudentRegister WHERE Name="xyz"')
            username = str(StudentRegister.objects.filter(Name=name, Email=email, Phone=phone))
            print "original username : "+str(username)
            print len(username)
            if len(username)>2:
                l=len(username)
                username=username[18:l-2]

                print "username -----------"+str(username)

                student = studentMarks.StudentMarks(str(omrsheet))
                y = student.checkValidImage()
                if y==-1:
                    return render(request, 'registration/', {})

                else:
                    x = student.getmarks(name,email,phone)
                if x==-1:
                    return render(request, 'registration/OMRFail.html', {})
            else:
                print "username is blank"
                return render(request, 'registration/UsernameNotFound.html', {})
            with open('example.pdf', 'r') as pdf:
                response = HttpResponse(pdf.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'inline;filename=some_file.pdf'
                return response
            print "printing marks list -------------------------"
            print x
            print "printed------------------------"
            return render(request, 'registration/OMRSuccess.html', {})

    else:
        omrForm = OmrSubmissionForm()
	studentForm=StudentRegister.objects.all()

    variables = RequestContext(request, {
        'omrForm': omrForm,
	'studentForm':studentForm
    })
    return render_to_response('registration/omrSubmit.html', variables,)"""
################################################################


class IndexView(generic.ListView):
    template_name = 'registration/home.html'
    context_object_name = 'student_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return StudentRegister.objects.all()



def register_success(request):
    return render_to_response(
        'registration/success.html',
    )



@login_required
def login(request):
    username = 'not logged in'

    if request.method == 'POST':
        MyLoginForm = LoginForm(request.POST)

        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
            request.session['username'] = username
        else:
            MyLoginForm = LoginForm()
    return render(request, 'registration/login.html', {"username": username})


def logout_page(request):
    logout(request)
    print "I am in logout_page"
    try:
        del request.session['username']
    except:
        pass
    #return HttpResponseRedirect('registration/login')
    return render(request, 'registration/logout_page.html')
    #return HttpResponse("<strong>You are logged out.</strong>")

@login_required(login_url='/login/')
def myview(request):
    return HttpResponse(render(request,'/'))


def omrSubmissionView(request):
    omrForm = OmrSubmissionForm()
    studentForm = StudentRegister.objects.all()
    if request.method == 'POST':
        oform = OmrSubmissionForm(request.POST, request.FILES)
        stuForm = StudentRegisatrationForm(request.POST)
        print "------All stuForm 1--------"
        print stuForm.errors
        if stuForm.is_valid():
            stuForm.Name = stuForm.cleaned_data['Name']
            print "hero---------------------------**************"
            print stuForm.Name

        email = request.POST.get('Email', False)
        name = request.POST.get('Name', False)
        rollno = request.POST.get('RollNo', False)
        print "email -------- name -------- roll no"
        print email
        print rollno
        print name
        print "------All good 1--------"
        print oform.errors
        print "------All good 1.2--------"

        if oform.is_valid():
            print "------All good 2--------"

            oform.omrsheet = oform.cleaned_data['omrsheet']
            oform.email = oform.cleaned_data['email']
            oform.name = oform.cleaned_data['name']
            oform.phone = oform.cleaned_data['phone']
            print "image name---------------------------**************"
            print oform.omrsheet
            print oform.email
            print oform.name
            print oform.phone

            print "email name---------------------------**************"
            omrsheet = oform.omrsheet
            # username = omrForm.cleaned_data['username']
            # item=StudentRegister.objects.get(Username=username).Email

            post = oform.save()
            post.user = request.user
            post.save()

            name = str(oform.name)
            email = str(oform.email)
            phone = str(oform.phone)
            # query='SELECT username FROM StudentRegister WHERE name="xyz"'
            print email

            # username = StudentRegister.objects.raw('SELECT Username FROM StudentRegister WHERE Name="xyz"')
            username = str(StudentRegister.objects.filter(Name=name, Email=email, Phone=phone))
            print "original username : " + str(username)
            print len(username)
            if len(username) > 2:
                l = len(username)
                username = username[18:l - 2]

                print "username -----------" + str(username)

                student = studentMarks.StudentMarks(str(omrsheet))
                y = student.checkValidImage()
                if y == -1:
                    print "Image size is not valid"
                    return render(request, 'registration/OMRFail.html', {})

                else:
                    x = student.getmarks(name, email, phone)
                if x == -1:
                    print "Partitions Not Found"
                    return render(request, 'registration/OMRFail.html', {})
                elif x== -2:
                    print "One of the ROI has not expected number of bubbles"
                    return render(request, 'registration/OMRFail.html', {})
            else:
                print "username is blank"
                return render(request, 'registration/UsernameNotFound.html', {})
            with open('example.pdf', 'r') as pdf:
                response = HttpResponse(pdf.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'inline;filename=some_file.pdf'
                return response
            print "printing marks list -------------------------"
            print x
            print "printed------------------------"
            return render(request, 'registration/OMRSuccess.html', {})

    else:
        omrForm = OmrSubmissionForm()
        studentForm = StudentRegister.objects.all()

    variables = RequestContext(request, {
        'omrForm': omrForm,
        'studentForm': studentForm
    })
    return render_to_response('registration/omrSubmit.html', variables)


@login_required
def home(request):
    return render_to_response(
        'registration/home.html',
        {'user': request.user}
    )


def formView(request):
   if request.session.has_key('username'):
      username = request.session['username']
      return render(request, 'loggedin.html', {"username" : username})
   else:
      return render(request, '/', {})