from django.contrib import admin
from django.urls import path
from categorias.views import CategoriasCreateView, CategoriasUpdateDelete
#from locales.views import LocalesCreateView, LocalesUpdateDelete
#from canchas.views import CanchasCreateView, CanchasUpdateDelete
#from reservas.views import ReservasCreateView, ReservasUpdateDelete
urlpatterns = [
    path('api/categorias', CategoriasCreateView.as_view()),
    path('api/categorias/<pk>', CategoriasUpdateDelete.as_view()),
#   path('api/locales', LocalesCreateView.as_view()),
 #   path('api/locales/<pk>', LocalesUpdateDelete.as_view()),
 #   path('api/canchas', CanchasCreateView.as_view()),
 #   path('api/canchas/<pk>', CanchasUpdateDelete.as_view()),
 #   path('api/reservas', ReservasCreateView.as_view()),
 #   path('api/reservas/<pk>', ReservasUpdateDelete.as_view()),
]
