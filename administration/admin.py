from django.contrib import admin
from .models import *
from teachers.models import *
# Register your models here.
admin.site.register(Platform)
admin.site.register(Organization_Admin)
admin.site.register(TeacherProfile)