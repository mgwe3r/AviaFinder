from django.db import models
from datetime import timedelta

class City(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}-{self.code}"
    
class Airline(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='airline_logos/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Flight(models.Model):
    airline = models.ForeignKey(Airline, on_delete= models.CASCADE ,blank=True, null=True)
    origin = models.ForeignKey(City, on_delete= models.CASCADE, related_name="start_city")
    destination = models.ForeignKey(City, on_delete= models.CASCADE, related_name="end_city")
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    transfers = models.IntegerField(default=0)

    @property
    def flight_time(self):
        result = self.arrival_time - self.departure_time
        if result.total_seconds() < 0:
            result += timedelta(days=1)
        total_minutes = result.total_seconds() // 60
        hours = int(total_minutes // 60)
        minutes = int(total_minutes % 60)
        return f"{hours} ч {minutes} мин"

    def __str__(self):
        return f"{self.origin}-{self.destination}-{self.airline}"
    
class Buyflight(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True, null=True)
    passport = models.IntegerField()

    def __str__(self):
        return f"{self.first_name}-{self.last_name}-{self.email}"
    