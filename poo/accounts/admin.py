from django.contrib import admin
from accounts.models import PersonaTable, Status, Rol

# Register your models here.


class PersonaAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email')


class StatusAdmin(admin.ModelAdmin):
    list_display = ('status', )


class RolAdmin(admin.ModelAdmin):
    list_display = ('rol', )


admin.site.register(PersonaTable, PersonaAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Rol, RolAdmin)
