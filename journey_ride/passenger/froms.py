from django import forms

from .models import StartTour


class StartTourForm(forms.ModelForm):
    class Meta:
        model = StartTour
        fields = '__all__'
