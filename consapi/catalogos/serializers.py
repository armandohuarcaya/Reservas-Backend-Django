from rest_framework.serializers import ModelSerializer
from catalogos.models import Catalogos

class CatalogosSerializer(ModelSerializer):
    class Meta:
        model = Catalogos
        fields = ('id', 'nombre', 'descripcion','image', 'estado')
