from django import forms

from app.models import ParkingSpace


class ParkingSpaceForm(forms.ModelForm):
    class Meta:
        model = ParkingSpace
        fields = ['name']