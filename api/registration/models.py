from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_passenger = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)


class Passenger(models.Model):
    id = models.AutoField(primary_key=True)
    passengerName = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    profilePicUrl = models.ImageField()
    telNo = models.CharField(max_length=20)
    createdDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now=True)


class Driver(models.Model):
    id = models.AutoField(primary_key=True)
    driverName = models.CharField(max_length=100)
    DOB = models.DateField()
    address = models.CharField(max_length=100)
    NIC = models.CharField(max_length=100)
    licenseNO = models.CharField(max_length=100)
    profilePicUrl = models.ImageField()
    drivingLicenseUrl = models.ImageField()
    createdDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now=True)


class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    vehicleImage1 = models.ImageField()
    vehicleImage2 = models.ImageField()
    vehicleImage3 = models.ImageField()
    regNo = models.CharField(max_length=100)
    ownerName = models.CharField(max_length=100)
    ownerAddress = models.CharField(max_length=100)
    numberOfPassenger = models.IntegerField()
    acCondition = models.BinaryField()
    insExpDate = models.DateField()
    createdDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now=True)