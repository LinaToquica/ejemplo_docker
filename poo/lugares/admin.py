from django.contrib import admin
from .models import Ciudad, Categoria, Foto_lugar, LugarTable

# Register your models here.


class CiudadAdmin(admin.ModelAdmin):
    list_display = ('ciudad', )


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria',)


class Foto_lugarAdmin(admin.ModelAdmin):
    list_display = ('foto_path',)


class LugarAdmin(admin.ModelAdmin):
    list_display = ('nombre_lugar',)

admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Foto_lugar, Foto_lugarAdmin)
admin.site.register(LugarTable, LugarAdmin)
