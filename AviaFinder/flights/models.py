from django.db import models


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
    origin = models.ForeignKey(City, on_delete= models.CASCADE ,blank=True, null=True)
    destination = models.ForeignKey(City, on_delete= models.CASCADE ,blank=True, null=True)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    transfers = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.origin}-{self.destination}-{self.airline}"
    