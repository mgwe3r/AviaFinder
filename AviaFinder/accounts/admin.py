from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# @admin.register(User)

# class User_admin(UserAdmin):
#     list_display = ("id", "name", "email", "first_name", "second_name")

@admin.register(CustomUser)

class CustomUser_admin(UserAdmin):
    list_display = ("username", "email", "password")