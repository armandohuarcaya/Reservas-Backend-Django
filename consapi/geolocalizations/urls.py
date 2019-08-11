from django.contrib import admin
from django.urls import path
from geolocalizations.views import GeolocalizationsCreateView, GeolocalizationsUpdateDelete

urlpatterns = [
    path('api/geolocalizations', GeolocalizationsCreateView.as_view()),
    path('api/geolocalizations/<pk>', GeolocalizationsUpdateDelete.as_view()),
]
