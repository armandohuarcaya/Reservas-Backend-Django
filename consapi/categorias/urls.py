from django.contrib import admin
from django.urls import path
from categorias.views import CategoriasCreateView, CategoriasUpdateDelete

urlpatterns = [
    path('api/categorias', CategoriasCreateView.as_view()),
    path('api/categorias/<pk>', CategoriasUpdateDelete.as_view()),
]
