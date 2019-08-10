from django import forms

from .models import Owner, Driver, Vehicle


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
