from rest_framework.serializers import ModelSerializer
from geolocalizations.models import Geolocalizations

class GeolocalizationsSerializer(ModelSerializer):
    class Meta:
        model = Geolocalizations
        fields = ('id', 'nombre', 'lat', 'lng', 'arrastrable', 'image', 'estado')