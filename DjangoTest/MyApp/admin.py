from django.contrib import admin
from MyApp.models import Student
# Register your models here.
# 超级管理员用户名：admin

admin.site.register(Student)
