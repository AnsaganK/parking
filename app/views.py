from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from pytils.translit import slugify
from app.forms import ParkingSpaceForm
from app.models import ParkingSpace
from app.utils import show_form_errors, get_paginator
from datetime import datetime, timedelta


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
    parking_spaces = get_paginator(request, parking_spaces, 12)
    return render(request, 'app/parking_space/list.html', {'parking_spaces': parking_spaces})


@login_required()
def parking_detail(request, slug):
    dates = {}
    parking_space = get_object_or_404(ParkingSpace, slug=slug)
    date_format = '%Y-%m-%dT%H:%M'
    try:
        time_start = request.GET.get('time_start')
        time_end = request.GET.get('time_end')
        time_start = datetime.strptime(str(time_start), date_format)
        time_end = datetime.strptime(str(time_end), date_format)
    except Exception as e:
        print(e)
        time_start = datetime.now()
        time_end = datetime.now() + timedelta(days=7)

    date = time_start
    reserves = parking_space.reserves.filter(time_start__gt=time_start, time_end__lte=time_end)
    while date != time_end + timedelta(days=1):
        dates[date] = reserves.filter(time_start__gt=date).filter(time_start__lte=date)
        date += timedelta(days=1)
    return render(request, 'app/parking_space/detail.html', {'parking_space': parking_space,
                                                             'reserves': reserves,
                                                             'time_start': time_start.strftime(date_format),
                                                             'time_end': time_end.strftime(date_format),
                                                             'dates': dates
                                                             })
