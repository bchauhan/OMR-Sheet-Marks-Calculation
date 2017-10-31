from django.contrib import admin
from django.db import models
from .models import AdminRegister,StudentRegister, OMRSubmitModel

# Register your models here.

admin.site.register(AdminRegister)
admin.site.register(StudentRegister)
admin.site.register(OMRSubmitModel)
