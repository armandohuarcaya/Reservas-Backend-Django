from django.contrib import admin
from django.urls import path
from reservas.views import ReservasCreateView, ReservasUpdateDelete

urlpatterns = [
    path('api/reservas', ReservasCreateView.as_view()),
    path('api/reservas/<pk>', ReservasUpdateDelete.as_view()),
]
