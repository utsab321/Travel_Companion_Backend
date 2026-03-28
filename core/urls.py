from django.urls import path
from .views import create_destination, city_list

urlpatterns = [
    path('destinations/', create_destination),
    path('cities/', city_list),
]