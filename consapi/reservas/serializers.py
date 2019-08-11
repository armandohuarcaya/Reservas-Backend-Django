from rest_framework.serializers import ModelSerializer
from reservas.models import Reservas

class ReservasSerializer(ModelSerializer):
    class Meta:
        model = Reservas
        fields = ('id', 'hora_reserv', 'estado')