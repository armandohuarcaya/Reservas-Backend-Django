from django.db import models

# Create your models here.
class Catalogos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=200)
    image = models.ImageField(upload_to='profile_images', blank=True, null=True)
    estado = models.IntegerField(max_length=1)

    def __str__(self):
        return self.nombre