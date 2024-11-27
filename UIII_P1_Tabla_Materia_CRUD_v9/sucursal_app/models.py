from django.db import models

# Create your models here.
class Sucursales(models.Model):
    ID_Sucursal = models.PositiveBigIntegerField(null=False, primary_key=True)
    Nombre = models.CharField(max_length=50, null=False)
    Direccion = models.CharField(null=False, max_length=100)
    Horario = models.CharField(null=False, max_length=100)
    Encargado = models.CharField(null=False, max_length=50)
    Correo = models.CharField(null=False, max_length=50)
    Telefono = models.PositiveBigIntegerField(null=False)

    def __str__(self):
        return self.Nombre