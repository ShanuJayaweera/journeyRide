from django.db import models


class Owner(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    NIC = models.CharField(max_length=50)
    companyName = models.CharField(max_length=60)
    address = models.CharField(max_length=100)
    contactNo = models.CharField(max_length=20)
    serviceType = models.CharField(max_length=50)
    profileImage = models.ImageField(upload_to='ownerImage/profileImages/', default='pic_folder/None/no-img.jpg')
    createdDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now=True)


class Driver(models.Model):
    id = models.AutoField(primary_key=True)
    companyOwner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contactNo = models.CharField(max_length=20)
    NIC = models.CharField(max_length=100)
    licenseNO = models.CharField(max_length=100)
    profileImage = models.ImageField(upload_to='driverImage/profileImages/', default='pic_folder/None/no-img.jpg')
    drivingLicenseImage = models.ImageField(upload_to='driverImage/licenseImages/', default='pic_folder/None/no-img.jpg')
    createdDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now=True)


class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    vehicleImage1 = models.ImageField(upload_to='vehicleImage/vehicleImages/', default='pic_folder/None/no-img.jpg')
    vehicleImage2 = models.ImageField(upload_to='vehicleImage/vehicleImages/', default='pic_folder/None/no-img.jpg')
    vehicleImage3 = models.ImageField(upload_to='vehicleImage/vehicleImages/', default='pic_folder/None/no-img.jpg')
    regNo = models.CharField(max_length=100)
    numberOfPassenger = models.IntegerField()
    acCondition = models.BinaryField()
    insExpDate = models.DateField()
    createdDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now=True)