from django.contrib import admin
from django.urls import path
from naturalpersons.views import NaturalPersonsCreateView, NaturalPersonsUpdateDelete

urlpatterns = [
    path('api/naturalpersons', NaturalPersonsCreateView.as_view()),
    path('api/naturalpersons/<pk>', NaturalPersonsUpdateDelete.as_view()),
]
