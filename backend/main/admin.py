from django.contrib import admin
from main.models import User, Student, Teacher, ClassRoom, Subject  
# from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User)

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(ClassRoom)
admin.site.register(Subject)