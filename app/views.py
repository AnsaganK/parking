from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from app.models import ParkingSpace


def base_page(request):
    return render(request, 'app/other/home.html')


@login_required()
def parking_list(request):
    parking_spaces = ParkingSpace.objects.all()
    return render(request, 'app/parking_space/list.html', {'parking_spaces': parking_spaces})


@login_required()
def parking_detail(request, slug):
    parking_space = get_object_or_404(ParkingSpace, slug=slug)
    return render(request, 'app/parking_space/detail.html', {'parking_space': parking_space})
