from django.db import models
from django.contrib.auth.models import User


class StartTour(models.Model):
    id = models.AutoField(primary_key=True)
    passenger = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicleType = models.CharField(max_length=200)
    travelLocation = models.CharField(max_length=200)
    numberOfPassenger = models.IntegerField()
    arrivalDate = models.DateField()
    departureDate = models.DateField()
    pickLocation = models.CharField(max_length=200)
    acCondition = models.BooleanField(default=False)
    wayPoints = models.CharField(max_length=5000)
    tourDescription = models.TextField(max_length=5000)
    createdDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now=True)







