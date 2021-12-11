from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.base_page, name='base_page'),
]