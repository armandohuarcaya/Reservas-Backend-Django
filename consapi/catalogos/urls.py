from django.contrib import admin
from django.urls import path
from catalogos.views import CatalogosCreateView, CatalogosUpdateDelete
urlpatterns = [
    path('api/catalogos', CatalogosCreateView.as_view()),
    path('api/catalogos/<pk>', CatalogosUpdateDelete.as_view()),
 ]