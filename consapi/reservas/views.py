from django.shortcuts import render

# Create your views here.
from reservas.models import Reservas

from reservas.serializers import ReservasSerializer
from rest_framework import generics
from django.shortcuts import render
class ReservasCreateView(generics.ListCreateAPIView):
    queryset = Reservas.objects.all()
    serializer_class = ReservasSerializer

class ReservasUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservas.objects.all()
    serializer_class = ReservasSerializer