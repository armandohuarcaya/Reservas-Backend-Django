from django.shortcuts import render

# Create your views here.
from naturalpersons.models import NaturalPersons

from naturalpersons.serializers import NaturalPersonsSerializer
from rest_framework import generics
from django.shortcuts import render
class NaturalPersonsCreateView(generics.ListCreateAPIView):
    queryset = NaturalPersons.objects.all()
    serializer_class = NaturalPersonsSerializer

class NaturalPersonsUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = NaturalPersons.objects.all()
    serializer_class = NaturalPersonsSerializer