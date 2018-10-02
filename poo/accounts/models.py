
from django.db import models
import django.db.models.deletion

# Create your models here.
from calificaciones.models import CalificacionTable


class Rol(models.Model):
    rol = models.CharField(
        max_length=255, null=True, blank=True
    )

    def __str__(self):
        """Return string representation."""
        return self.rol


class Status(models.Model):
    status = models.CharField(
        max_length=255, null=True, blank=True
    )

    def __str__(self):
        """Return string representation."""
        return self.status


class PersonaTable(models.Model):
    """
    Persona
    """
    first_name = models.CharField(
        max_length=255, null=True, blank=True
    )
    last_name = models.CharField(
        max_length=255, null=True, blank=True
    )
    email = models.EmailField(
        max_length=255, unique=True, db_index=True
    )

    fecha_nacimiento = models.DateField(null=True, blank=True, verbose_name='Fecha_nacimiento')

    rol = models.ForeignKey(Rol, related_name='rol_persona', on_delete=django.db.models.deletion.DO_NOTHING)

    status = models.ForeignKey(Status, related_name='status_persona', on_delete=django.db.models.deletion.DO_NOTHING)

    is_super_admin = models.BooleanField(default=False)

    calificacion = models.ForeignKey(CalificacionTable, blank=True, null=True,
                                     related_name='status_persona', on_delete=django.db.models.deletion.DO_NOTHING)

    def __str__(self):
        """Return string representation."""
        return self.email



