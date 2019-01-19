from django.db import models

# Create your models here.

class Categorias(models.Model):
    
    id = models.AutoField(primary_key=True)
    nombreCategoria = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    tipoCategoria = models.CharField(max_length=10)
    estado = models.CharField(max_length=3)
    