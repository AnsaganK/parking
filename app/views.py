from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from pytils.translit import slugify

from app.forms import ParkingSpaceForm
from app.models import ParkingSpace
from app.utils import show_form_errors


def base_page(request):
    return render(request, 'app/other/home.html')


@login_required()
def parking_list(request):
    if request.method == 'POST':
        form = ParkingSpaceForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            parking_space = form.save()
            parking_space.slug = slugify(f'{cd["name"]}-{str(parking_space.id)}')
            parking_space.save()
            messages.success(request, 'created')
        else:
            show_form_errors(request, form.errors)
        return redirect(reverse('app:parking_list'))
    parking_spaces = ParkingSpace.objects.all()
    return render(request, 'app/parking_space/list.html', {'parking_spaces': parking_spaces})


@login_required()
def parking_detail(request, slug):
    parking_space = get_object_or_404(ParkingSpace, slug=slug)
    return render(request, 'app/parking_space/detail.html', {'parking_space': parking_space})
