from django.contrib import admin
from .models import Flight, City, Airline, Buyflight

@admin.register(City)

class City_admin(admin.ModelAdmin):
    list_display = ("id", "name", "code")

@admin.register(Flight)

class Flight_admin(admin.ModelAdmin):
    list_display = ("id", "airline", "origin", "destination", "departure_time", "arrival_time", "price", "transfers")

@admin.register(Airline)

class Airplane_admin(admin.ModelAdmin):
    list_display = ("id", "name", "logo")

@admin.register(Buyflight)

class BuyFlight_admin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "passport")