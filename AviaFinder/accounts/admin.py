from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)

class User_admin(UserAdmin):
    list_display = ("id", "name", "email", "first_name", "second_name")
