from django.urls import path
from .views import TripListAPIView, TripDetailAPIView,DestinationListAPIView,CityListAPIView
from . import views

urlpatterns = [
    path('trips/', TripListAPIView.as_view(), name='trip-list'),
    path('trips/<int:pk>/', TripDetailAPIView.as_view(), name='trip-detail'),
    path('api/destinations/', DestinationListAPIView.as_view()),
    path('api/cities/', CityListAPIView.as_view(), name='city-list'),
]