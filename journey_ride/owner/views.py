from django.shortcuts import render
from .forms import OwnerForm, VehicleForm, DriverForm
from .models import Owner, Driver, Vehicle
from django.views.generic import ListView, CreateView # new


def ownerView(request):
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = OwnerForm()

    context = {
        'form': form
    }

    return render(request, "ownerForm.html", context)


def driverView(request):
    form = DriverForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = DriverForm()

    context = {
        'form': form
    }

    return render(request, "driverForm.html", context)


def vehicleView(request):
    form = VehicleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = VehicleForm()

    context = {
        'form': form
    }

    return render(request, "vehicleForm.html", context)


def ownerView(request):
    queryset = Owner.objects.all() #list of objects
    context = {
        "object_List" : queryset
    }