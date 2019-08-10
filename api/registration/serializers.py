from rest_framework import serializers
from api.registration.models import Passenger, Vehicle, Driver


# Passenger Serializer


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ('passengerName', 'email', 'country', 'profilePicUrl', 'telNo', 'createdDate', 'updateDate')


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('driverName', 'DOB', 'address', 'NIC', 'licenseNO', 'profilePicUrl', 'drivingLicenseUrl')


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('brand', 'model', 'vehicleImage1', 'vehicleImage2', 'vehicleImage3', 'regNo', 'ownerName',
                  'ownerAddress',
                  'numberOfPassenger',
                  'acCondition',
                  'insExpDate')



