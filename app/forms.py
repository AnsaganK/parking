from django import forms

from app.models import ParkingSpace, Reserve, ReservingUser


class ParkingSpaceForm(forms.ModelForm):
    class Meta:
        model = ParkingSpace
        fields = ['name']


class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = ['time_start', 'time_end']

class ReservingUserForm(forms.ModelForm):
    class Meta:
        model = ReservingUser
        fields = ['first_name', 'last_name', 'email', 'phone']