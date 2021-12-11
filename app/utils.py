from django.contrib import messages


def show_form_errors(request, errors):
    if not errors:
        messages.error(request, 'Error')
    for error in errors:
        messages.error(request, errors[error])