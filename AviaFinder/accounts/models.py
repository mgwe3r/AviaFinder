from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from flights.models import Flight

class CustomUser(AbstractUser):
    pass

class UserFavorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, blank=True, null=True)
    flight = models.ForeignKey(Flight, on_delete= models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField()

    def __str__(self):
        return f"{self.user}-{self.flight}"
