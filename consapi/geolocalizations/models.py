from django.db import models

# Create your models here.

class Geolocalizations(models.Model):
    # ESTADO_CHOICES = ('1', 'Hombre'), ('2', 'Mujer') , ('3', 'Otros')
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    lat = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)
    arrastrable = models.CharField(max_length=5)
    estado = models.CharField(max_length=1)
    

    def __str__(self):
        return self.nombre