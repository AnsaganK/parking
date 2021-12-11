from django.contrib import admin
from .models import ParkingSpace, ReservingUser, Reserve, Profile


@admin.register(ParkingSpace)
class ParkingSpaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ReservingUser)
class ReservingUserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']


@admin.register(Reserve)
class ReserveAdmin(admin.ModelAdmin):
    list_display = ['unique_id']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']
