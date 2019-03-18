from django.shortcuts import render
from catalogos.models import Catalogos
# Create your views here.
from catalogos.serializers import CatalogosSerializer
from rest_framework import generics
from django.shortcuts import render

class CatalogosCreateView(generics.ListCreateAPIView):
    queryset = Catalogos.objects.all()
    serializer_class = CatalogosSerializer

class CatalogosUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Catalogos.objects.all()
    serializer_class = CatalogosSerializer