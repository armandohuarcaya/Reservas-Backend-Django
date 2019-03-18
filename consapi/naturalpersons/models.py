from django.db import models

# Create your models here.

class NaturalPersons(models.Model):
    # ESTADO_CHOICES = ('1', 'Hombre'), ('2', 'Mujer') , ('3', 'Otros')
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apePater = models.CharField(max_length=30)
    apeMater = models.CharField(max_length=30)
    edad = models.CharField(max_length=30)
    fecNacim = models.DateField()
    dni = models.IntegerField(max_length=8)
    email = models.EmailField(max_length=50)
    celular = models.IntegerField(max_length=9)
    image = models.ImageField(upload_to='profile_imagess', blank=True, null=True)
    estado = models.IntegerField(max_length=1)

    def __str__(self):
        return self.nombre