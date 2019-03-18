from rest_framework.serializers import ModelSerializer
from categorias.models import Categorias

#from locales.models import Locales
#from canchas.models import Canchas
#from reservas.models import Reservas

class CategoriasSerializer(ModelSerializer):
    class Meta:
        model = Categorias
        fields = ('id', 'nombreCategoria', 'descripcion', 'tipoCategoria', 'image', 'estado')


#class LocalesSerializer(ModelSerializer):
#    class Meta:
#        model = Locales
#        fields = ('id', 'nombre', 'direccion', 'ruc', 'email', 'celular', 'estado')
#
#class CanchasSerializer(ModelSerializer):
#    class Meta:
#        model = Canchas
#        fields = ('id', 'nombre', 'numero', 'celular','estado')
#
#class ReservasSerializer(ModelSerializer):
#    class Meta:
#        model = Reservas
#        fields = ('id', 'fecInicio', 'time', 'estado')