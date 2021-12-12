from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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
