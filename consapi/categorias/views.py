from categorias.models import Categorias
from categorias.serializers import CategoriasSerializer
from rest_framework import generics
from django.shortcuts import render


# Create your views here.

class CategoriasCreateView(generics.ListCreateAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer

class CategoriasUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer