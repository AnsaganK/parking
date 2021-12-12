from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect, reverse
from pytils.translit import slugify
from app.forms import ParkingSpaceForm, ReserveForm, ReservingUserForm
from app.models import ParkingSpace, ReservingUser, Reserve
from app.utils import show_form_errors, get_paginator, str_to_date, date_to_str
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
    try:
        time_start = str_to_date(request.GET.get('time_start'))
        time_end = str_to_date(request.GET.get('time_end'))
    except Exception as e:
        print(e)
        time_start = datetime.now()
        time_end = datetime.now() + timedelta(days=7)

    date = time_start
    reserves = parking_space.reserves.all()
    while date.date() < time_end.date() + timedelta(days=1):
        dates[date] = reserves.filter(
            Q(time_start__lte=date, time_end__gte=date) |
            Q(time_start__day=date.day, time_start__month=date.month, time_start__year=date.year) |
            Q(time_end__day=date.day, time_end__month=date.month, time_end__year=date.year)
        )
        date += timedelta(days=1)
    return render(request, 'app/parking_space/detail.html', {'parking_space': parking_space,
                                                             'reserves': reserves,
                                                             'time_start': date_to_str(time_start),
                                                             'time_end': date_to_str(time_end),
                                                             'dates': dates
                                                             })


@login_required()
def reserve_create(request, slug):
    parking_space = get_object_or_404(ParkingSpace, slug=slug)
    if request.method == 'POST':
        form = ReserveForm(request.POST)
        if form.is_valid():
            reserve = form.save(commit=False)
            cd = form.cleaned_data
            time_start = cd['time_start']
            time_end = cd['time_end']
            post = request.POST
            reserves = parking_space.reserves.filter(
                (Q(time_start__gt=time_start) & Q(time_end__lt=time_end)) |
                (Q(time_start__lt=time_start) & Q(time_end__gt=time_end)) |
                (Q(time_start__lt=time_start) & Q(time_end__gt=time_start)) |
                (Q(time_start__lt=time_end) & Q(time_end__gt=time_end))
            )
            if reserves:
                messages.warning(request, 'Already booked for this time')
                return redirect(parking_space.get_absolute_url())
            try:
                reserving_user_id = int(post['reserving_user'])
                reserving_user = ReservingUser.objects.get(id=reserving_user_id)
            except KeyError:
                reserving_user = ReservingUser(first_name=post['first_name'],
                                               last_name=post['last_name'],
                                               email=post['email'],
                                               phone=post['phone'])
                reserving_user.save()

            reserve.reserving_emlpoyee = request.user
            reserve.reserving_user = reserving_user
            reserve.parking_space = parking_space
            reserve.save()
            messages.success(request, 'Reserved')
        else:
            show_form_errors(request, form.errors)
        return redirect(parking_space.get_absolute_url())
    reserving_users = ReservingUser.objects.all()
    return render(request, 'app/reserve/create.html',
                  {'parking_space': parking_space, 'reserving_users': reserving_users})


@login_required()
def reserving_user_list(request):
    reserving_users = ReservingUser.objects.all()
    return render(request, 'app/reserving_user/list.html', {'reserving_users': reserving_users})


@login_required()
def reserving_user_edit(request, pk):
    reserving_user = get_object_or_404(ReservingUser, id=pk)
    if request.method == 'POST':
        form = ReservingUserForm(request.POST, instance=reserving_user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User changed')
        else:
            show_form_errors(request, form.errors)
        return redirect(reverse('app:reserving_user_list'))
    return render(request, 'app/reserving_user/edit.html', {'reserving_user': reserving_user})


@login_required()
def reserving_user_delete(request, pk):
    reserving_user = get_object_or_404(ReservingUser, id=pk)
    reserving_user.delete()
    messages.success(request, 'User deleted')
    return redirect(reverse('app:reserving_user_list'))


@login_required()
def cabinet(request):
    return render(request, 'app/employee/cabinet.html')
