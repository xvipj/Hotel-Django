from django.db import models

# Create your models here.
class Reserva(models.Model):
    fecha_entrada = models.DateField(verbose_name="Fecha de Entrada")
    fecha_salida = models.DateField(verbose_name="Fecha de Salida")
    numero_adultos = models.PositiveIntegerField(verbose_name="Número de Adultos")
    numero_ninos = models.PositiveIntegerField(verbose_name="Número de Niños", default=0)

    def __str__(self):
        return f"Reserva del {self.fecha_entrada} al {self.fecha_salida} - {self.numero_adultos} adultos y {self.numero_ninos} niños"