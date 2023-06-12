from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='nombre_instructor')
    email = models.EmailField()
    celular = models.CharField(max_length=12, verbose_name='fono_instructor')
    

    def __str__(self):
        return self.nombre