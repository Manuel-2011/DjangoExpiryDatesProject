from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_vencimiento = models.DateField()
    fecha_creado = models.DateField(auto_now_add=True)
    fecha_salida = models.DateTimeField(null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Historico(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_vencimiento = models.DateField()
    fecha_creado = models.DateField()
    fecha_salida = models.DateTimeField(auto_now_add=True)
    usuario_elimina = models.ForeignKey(User, on_delete=models.CASCADE)