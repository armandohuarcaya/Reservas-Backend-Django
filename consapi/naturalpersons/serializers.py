from rest_framework.serializers import ModelSerializer
from naturalpersons.models import NaturalPersons

class NaturalPersonsSerializer(ModelSerializer):
    class Meta:
        model = NaturalPersons
        fields = ('id', 'nombre', 'apePater', 'apeMater', 'edad', 'fecNacim', 'dni', 'email', 'celular', 'image', 'estado')
