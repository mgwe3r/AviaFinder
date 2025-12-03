from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from flights.models import Flight
from .forms import Flights_search_form, BuyFlightForm

def profile_view(request): 
    return render(request, "profile.html")

def flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)

    if request.method == "POST":
        form = BuyFlightForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.flight = flight
            order.save()
            redirect("flight_view")
    else:
        form = BuyFlightForm()
    return render(request, "flight_card.html", {"form":form, "flight":flight})



def flight_search(request):
    form = Flights_search_form(request.GET or None)
    flights = None
    if form.is_valid():
        origin = form.cleaned_data["origin"]
        destination = form.cleaned_data["destination"]
        date = form.cleaned_data["date"]
        flights = Flight.objects.filter(origin=origin, destination=destination)
        if date:
            flights = flights.filter(departure_time__date=date)
    return render(request, "flight_list.html", {"form": form, "flights": flights})


def flight_view(request):
    form = Flights_search_form(request.GET or None)
    flights = None
    if request.GET and form.is_valid():
        flights = Flight.objects.all()
        origin = form.cleaned_data["origin"]
        destination = form.cleaned_data["destination"]
        date = form.cleaned_data["date"]
        flights = Flight.objects.filter(origin=origin, destination=destination)
        if date:
            flights = flights.filter(departure_time__date=date)
    return render(request, "flight_list.html", {"flights": flights, "form": form})

# def buy_flight(request, flight_id):
    # flight = get_object_or_404(Flight, id=flight_id)

    # if request.method == "POST":
    #     form = BuyFlightForm(request.POST)
    #     if form.is_valid():
    #         order = form.save()
    #         order.flight = flight
    #         order.save()
    #         redirect("flight_view")
    # else:
    #     form = BuyFlightForm()
    # return render(request, "flight_card.html", {"form":form, "flight":flight})