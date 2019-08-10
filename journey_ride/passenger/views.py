from django.shortcuts import render
from .froms import StartTourForm
from owner.models import Owner, Driver, Vehicle


def startTourView(request):
    form = StartTourForm(request.POST or None)
    if form.is_valid():
        passenger = request.POST.get('passenger')
        vehicleType = request.POST.get('vehicleType')
        travelLocation = request.POST.get('travelLocation')
        NumberOfPassenger = request.POST.get('NumberOfPassenger')
        ArrivalDate = request.POST.get('ArrivalDate')
        DepartureDate = request.POST.get('DepartureDate')
        PickLocation = request.POST.get('PickLocation')
        AcCondition = request.POST.get('AcCondition')

        #form.save()
        #form = StartTourForm()

    context = {
        'form' : form
    }

    return render(request, "startTour.html", context)


def searchVehicle(vehicleType,
                  travelLocation,
                  NumberOfPassenger,
                  ArrivalDate,
                  DepartureDate,
                  PickLocation,
                  AcCondition):

    queryset = Owner.objects.all()
