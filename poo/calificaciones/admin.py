from django.contrib import admin
from .models import CalificacionTable

# Register your models here.


class CalificacionAdmin(admin.ModelAdmin):
    list_display = ('calificacion', 'tipo_calificacion')


admin.site.register(CalificacionTable, CalificacionAdmin)
