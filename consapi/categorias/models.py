from django.db import models

# Create your models here.

class Categorias(models.Model):
    
    id = models.AutoField(primary_key=True)
    nombreCategoria = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=2000)
    tipoCategoria = models.CharField(max_length=10)
    image = models.ImageField(upload_to='profile_image', blank=True, null=True)
    estado = models.CharField(max_length=1)
    def __str__(self):
        return self.nombreCategoria


#
#
#
#class Locales(models.Model):
#    id = models.AutoField(primary_key=True)
#    nombre = models.CharField(max_length=30)
#    direccion = models.CharField(max_length=30)
#    ruc = models.IntegerField(max_length=11)
#    email = models.EmailField(max_length=50)
#    celular = models.IntegerField(max_length=9)
#    estado = models.IntegerField(max_length=1)
#
#    def __str__(self):
#        return self.nombre
#
#class Canchas(models.Model):
#    id = models.AutoField(primary_key=True)
#    nombre = models.CharField(max_length=30)
#    numero = models.IntegerField(max_length=2)
#    celular = models.IntegerField(max_length=9)
#    estado = models.IntegerField(max_length=1)
#
#    def __str__(self):
#        return self.nombre
#
#class Reservas(models.Model):
#    id = models.AutoField(primary_key=True)
#    fecInicio = models.DateField()
#    time = models.TimeField((u"Conversation Time"), auto_now_add=True, blank=True, null=True)
#    estado = models.IntegerField(max_length=1)
#
#    def __str__(self):
#        return self.estado

