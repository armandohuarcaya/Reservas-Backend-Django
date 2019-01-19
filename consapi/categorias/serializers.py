from rest_framework.serializers import ModelSerializer
from categorias.models import Categorias

class CategoriasSerializer(ModelSerializer):
    class Meta:
        model = Categorias
        fields = ('id', 'nombreCategoria', 'descripcion', 'tipoCategoria', 'estado')