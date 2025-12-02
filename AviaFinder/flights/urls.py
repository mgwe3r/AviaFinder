from django.contrib import admin
from django.urls import path
from core import views
from core.views import profile_view

urlpatterns = [
    path("", views.flight_view, name="flight_view"),
    path("flight/<int:flight_id>", views.flight, name="flight"),
    path("profile/", profile_view, name="profle_view")
]
