from django.db import models
import django.db.models.deletion
from accounts.models import PersonaTable


# Create your models here.
from calificaciones.models import CalificacionTable


class Ciudad(models.Model):
    ciudad = models.CharField(
        max_length=255, null=True, blank=True
    )
    departamento = models.CharField(
        max_length=255, null=True, blank=True
    )

    def __str__(self):
        """Return string representation."""
        return self.ciudad


class Categoria(models.Model):
    categoria = models.CharField(
        max_length=255, null=True, blank=True
    )
    descripcion_categoria = models.TextField(
        'Descripción de la categoria del lugar', null=True, blank=True
        )

    def __str__(self):
        """Return string representation."""
        return self.categoria


class Foto_lugar(models.Model):
    foto_path = models.ImageField(upload_to='static/gallery/')


class LugarTable(models.Model):
    nombre_lugar = models.CharField(
        max_length=255, null=True, blank=True
    )
    ciudad = models.ForeignKey(Ciudad, on_delete=django.db.models.deletion.DO_NOTHING)
    categoria = models.ForeignKey(Categoria, on_delete=django.db.models.deletion.DO_NOTHING)
    direccion = models.CharField(
        max_length=255, null=True, blank=True
    )
    created_by = models.ForeignKey(PersonaTable, on_delete=django.db.models.deletion.DO_NOTHING)
    fotos = models.ManyToManyField(Foto_lugar, blank=True, null=True)
    puntaje = models.IntegerField(default=0, null=True, blank=True)
    es_lugar_aprobado = models.BooleanField(default=False)
    calificacion = models.ForeignKey(CalificacionTable, on_delete=django.db.models.deletion.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        """Return string representation."""
        return self.nombre_lugar





