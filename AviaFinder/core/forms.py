from django import forms
from django.contrib.auth.forms import UserCreationForm
from flights.models import City

class Flights_search_form(forms.ModelForm):
    origin = forms.ModelChoiceField(
        queryset = City.objects.all(),
        label="Город вылета ",
        required=True,
    )
    destination = forms.ModelChoiceField(
        queryset = City.objects.all(),
        label="Город прилета ",
        required=True
    )
    date = forms.DateField(
        label="Дата вылета ",
        widget=forms.DateInput(attrs={"type": "date"}),
        required=False
    )