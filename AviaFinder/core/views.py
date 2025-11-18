from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from flights.models import Flight


def flight_view(request):
    flight = Flight.objects.all()
    return render(request, "flight_list.html", {"flight": flight})