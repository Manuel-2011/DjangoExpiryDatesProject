from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_vencimiento = models.DateField()
    fecha_creado = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    fecha_salida = models.DateTimeField(null=True)
    usuario_crea = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL, related_name='productos_creados', null=True)
    usuario_elimina = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL, related_name='productos_eliminados', null=True)

    def __str__(self):
        return self.nombre
