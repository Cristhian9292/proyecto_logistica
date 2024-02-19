from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    numero_telefono = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre

class Transportista(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_vehiculo = models.CharField(max_length=50)
    numero_contacto = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre
    
class Paquete(models.Model):
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    dimensiones = models.CharField(max_length=50)
    direccion_origen = models.CharField(max_length=255)
    direccion_destino = models.CharField(max_length=255)
    ESTADO_ENTREGA_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Enviado', 'Enviado'),
        ('Entregado', 'Entregado'),
    ]
    estado_entrega = models.CharField(max_length=20, choices=ESTADO_ENTREGA_CHOICES, default='Pendiente')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    transportista = models.ForeignKey(Transportista, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"Paquete #{self.id}"