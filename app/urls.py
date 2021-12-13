from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.base_page, name='base_page'),
    path('parking', views.parking_list, name='parking_list'),
    path('parking/<slug:slug>', views.parking_detail, name='parking_detail'),
    path('parking/<slug:slug>/edit', views.parking_edit, name='parking_edit'),
    path('parking/<slug:slug>/delete', views.parking_delete, name='parking_delete'),
    path('parking/<slug:slug>/reserve/create', views.reserve_create, name='reserve_create'),

    path('reserve/search', views.reserve_search, name='reserve_search'),
    path('reserve/search/<uuid:unique_id>', views.reserve_search_api, name='reserve_search_api'),
    path('reserve/<uuid:unique_id>', views.reserve_detail, name='reserve_detail'),
    path('reserve/<uuid:unique_id>/edit', views.reserve_edit, name='reserve_edit'),

    path('cabinet', views.cabinet, name='cabinet'),
    path('cabinet/edit', views.profile_edit, name='profile_edit'),

    path('user', views.reserving_user_list, name='reserving_user_list'),
    path('user/<int:pk>/edit', views.reserving_user_edit, name='reserving_user_edit'),
    path('user/<int:pk>/delete', views.reserving_user_delete, name='reserving_user_delete'),
]