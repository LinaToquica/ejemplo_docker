from django.db import models
from .utils import TIPO_CALIFICACION
# Create your models here.


class CalificacionTable(models.Model):
    calificacion = models.CharField(
        max_length=255, null=True, blank=True
    )
    min_puntaje = models.IntegerField(
        null=True, blank=True,
    )
    max_puntaje = models.IntegerField(
        null=True, blank=True
    )

    tipo_calificacion = models.CharField(
        max_length=255, null=True, blank=True, choices=TIPO_CALIFICACION
    )

    def __str__(self):
        """Return string representation."""
        return self.calificacion

