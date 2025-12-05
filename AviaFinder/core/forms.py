from django import forms
from django.contrib.auth.forms import UserCreationForm
from flights.models import City, Buyflight

class Flights_search_form(forms.Form):
    origin = forms.ModelChoiceField(
        queryset = City.objects.all(),
        label=None,
        required=True,
    )
    destination = forms.ModelChoiceField(
        queryset = City.objects.all(),
        required=True
    )
    date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
        required=False,
    )

class BuyFlightForm(forms.ModelForm):
    class Meta:
        model = Buyflight
        fields = ("first_name", "last_name", "email", "passport")