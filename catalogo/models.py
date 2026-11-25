from django.db import models


class Producto(models.Model):
    ESTADOS = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]

    nombre = models.CharField(max_length=120, db_index=True)
    codigo = models.CharField(max_length=40, unique=True)
    categoria = models.CharField(max_length=60, db_index=True, default='General')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    estado = models.CharField(max_length=15, choices=ESTADOS, default='activo', db_index=True)
    creado_en = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-creado_en']

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"