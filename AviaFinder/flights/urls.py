from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path("", views.flight_view, name="flight_view"),
]
