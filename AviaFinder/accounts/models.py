from django.db import models
from django.contrib.auth.models import User
from .models import Flight


class UserFavorite(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, blank=True, null=True)
    flight = models.ForeignKey(Flight, on_delete= models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField()

    def __str__(self):
        return f"{self.user}-{self.flight}"
