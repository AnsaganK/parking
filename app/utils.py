from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from datetime import datetime
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test
from pytils.third import six


def show_form_errors(request, errors):
    if not errors:
        messages.error(request, 'Error')
    for error in errors:
        messages.error(request, errors[error])


def get_paginator(request, queryset, count):
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    return queryset


def str_to_date(date, date_format='%Y-%m-%dT%H:%M'):
    return datetime.strptime(str(date), date_format)


def date_to_str(date, date_format='%Y-%m-%dT%H:%M'):
    return date.strftime(date_format)


def group_required(group):
    def check_perms(user):
        if isinstance(group, six.string_types):
            groups = (group,)
        else:
            groups = group
        if user.groups.exists() and user.groups.filter(name__in=groups).exists():
            return True
        return False

    return user_passes_test(check_perms)
