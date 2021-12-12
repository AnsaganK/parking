from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.base_page, name='base_page'),
    path('parking', views.parking_list, name='parking_list'),
    path('parking/<slug:slug>', views.parking_detail, name='parking_detail'),
    path('parking/<slug:slug>/reserve/create', views.reserve_create, name='reserve_create'),
]