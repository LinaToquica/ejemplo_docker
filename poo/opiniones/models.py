import django.db.models.deletion
from django.db import models
from accounts.models import PersonaTable
from lugares.models import LugarTable
from calificaciones.models import CalificacionTable

# Create your models here.


class OpinionTable(models.Model):
    descripcion_opinion = models.CharField(
        max_length=255, null=True, blank=True
    )
    usuario = models.ForeignKey(PersonaTable, on_delete=django.db.models.deletion.DO_NOTHING)
    lugar = models.ForeignKey(LugarTable, on_delete=django.db.models.deletion.DO_NOTHING)
    calificacion = models.ForeignKey(CalificacionTable, on_delete=django.db.models.deletion.DO_NOTHING)
    puntaje = models.IntegerField(default=0)
