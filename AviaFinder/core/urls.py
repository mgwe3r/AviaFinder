from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static
from .views import flight_search

urlpatterns = [
    path("search/", flight_search, name="flight_search")
]
