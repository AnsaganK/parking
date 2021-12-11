from django.shortcuts import render


def base_page(request):
    return render(request, 'app/other/home.html')