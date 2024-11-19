from django.db import models

# Create your models here.
class Clientes(models.Model):
    ID_cliente = models.PositiveBigIntegerField(null=False, primary_key=True)
    Nombre = models.CharField(max_length=50, null=False)
    Correo = models.CharField(null=False, max_length=50)
    Forma_de_pago = models.CharField(null=False, max_length=20)
    Productos = models.CharField(null=False, max_length=50)
    Saldo = models.PositiveBigIntegerField(null=False)
    Direccion = models.CharField(null=False, max_length=100)

    def __str__(self):
        return self.Nombre