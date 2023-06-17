from django.db import models
from user.models import User

# Create your models here.
class Cafe(models.Model):
    name = models.CharField(max_length=10)
    location = models.TextField()
    info = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=11, unique=True, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
# name, price, FK(cafe)
class Menu(models.Model):
    name = models.CharField(max_length=10)
    price = models.CharField(max_length=6)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)

    def __str__(self):
        return self.name