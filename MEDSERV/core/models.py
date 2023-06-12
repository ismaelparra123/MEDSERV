from django.db import models

# Create your models here.


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='nombre')
    email = models.EmailField()
    celular = models.CharField(max_length=12, verbose_name='fono')

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100,verbose_name='nombre')
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="prod", null=True)
    
    def __str__(self):
        return self.nombre