from django.shortcuts import render

# Create your views here.
from geolocalizations.models import Geolocalizations

from geolocalizations.serializers import GeolocalizationsSerializer
from rest_framework import generics
from django.shortcuts import render
class GeolocalizationsCreateView(generics.ListCreateAPIView):
    queryset = Geolocalizations.objects.all()
    serializer_class = GeolocalizationsSerializer

class GeolocalizationsUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Geolocalizations.objects.all()
    serializer_class = GeolocalizationsSerializer