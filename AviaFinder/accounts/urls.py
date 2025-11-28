from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('account/login/', views.user_login, name="user_login"),
    path('account/logout/', views.user_logout, name="user_logout"),
    path('account/register', views.user_register, name="user_register")
]