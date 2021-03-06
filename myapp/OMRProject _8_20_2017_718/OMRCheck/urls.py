"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
import views

urlpatterns = [
            url(r'^login$',views.login, name='login'),
            url(r'^admin/',admin.site.urls),
            url(r'^$', 'django.contrib.auth.views.login'),
            #url(r'^$', index_page),

            url(r'logout_page/$', views.logout_page, name="logout_page"),
            #url(r'^logout/', 'logout', name = 'logout'),
            url(r'register', views.adminRegister),
            url(r'register/success', views.register_success),
            url(r'studentRegister/$', views.studentRegister, name="studentRegister"),
            url(r'omrSubmit/$', views.omrSubmissionView, name='omrSubmit'),

            #url(r'omrSubmit/$', views.omrSubmissionView, name='omrSubmit'),
            url(r'connection',views.formView, name = 'loginform'),
            #url(r'home', IndexView.as_view()), #r'^home/$',
            url(r'home/$', views.IndexView.as_view(), name='home'),
        ]

