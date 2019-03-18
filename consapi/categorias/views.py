from categorias.models import Categorias

#from locales.models import Locales
#from canchas.models import Canchas
#from reservas.models import Reservas
from categorias.serializers import CategoriasSerializer
#from locales.serializers import LocalesSerializer
#from canhas.serializers import CanchasSerializer
#from reservas.serializers import ReservasSerializer
from rest_framework import generics
from django.shortcuts import render


# Create your views here.

class CategoriasCreateView(generics.ListCreateAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer

class CategoriasUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer


#
#
#
#class LocalesCreateView(generics.ListCreateAPIView):
#    queryset = Locales.objects.all()
#    serializer_class = LocalesSerializer
#
#class LocalesUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Locales.objects.all()
#    serializer_class = LocalesSerializer
#
#class CanchasCreateView(generics.ListCreateAPIView):
#    queryset = Canchas.objects.all()
#    serializer_class = CanchasSerializer
#
#class CanchasUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Canchas.objects.all()
#    serializer_class = CanchasSerializer
#
#class ReservasCreateView(generics.ListCreateAPIView):
#    queryset = Reservas.objects.all()
#    serializer_class = ReservasSerializer
#
#class ReservasUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Reservas.objects.all()
#    serializer_class = ReservasSerializer