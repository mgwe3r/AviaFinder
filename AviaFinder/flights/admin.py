from django.contrib import admin
from .models import Flight, City, Airline

@admin.register(City)

class City_admin(admin.ModelAdmin):
    list_display = ("id", "name", "code")

@admin.register(Flight)

class Flight_admin(admin.ModelAdmin):
    list_display = ("id", "airline", "origin", "destination", "depature_time", "arrival_time", "price", "transfers")

@admin.register(Airline)

class Airplane_admin(admin.ModelAdmin):
    list_display = ("id", "name", "logo")