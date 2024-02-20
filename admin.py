from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import DeptUser
# Register your models here.
admin.site.register(DeptUser,UserAdmin)