from django.contrib import admin
from .models import OpinionTable

# Register your models here.


class OpinionAdmin(admin.ModelAdmin):
    list_display = ('descripcion_opinion', )

admin.site.register(OpinionTable, OpinionAdmin)
