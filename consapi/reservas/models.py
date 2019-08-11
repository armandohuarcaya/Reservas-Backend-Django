from django.db import models

# Create your models here.

class Reservas(models.Model):
    # ESTADO_CHOICES = ('1', 'Hombre'), ('2', 'Mujer') , ('3', 'Otros')
    id = models.AutoField(primary_key=True)
    hora_reserv = models.CharField(max_length=100)
    precio = models.CharField(max_length=4)
    estado = models.CharField(max_length=1)
    

    def __str__(self):
        return self.hora_reserv