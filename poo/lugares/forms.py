from django import forms
from .models import LugarTable


class LugarForm(forms.ModelForm):

    class Meta:
        model = LugarTable

        fields = [
            'nombre_lugar',
            'ciudad',
            'categoria',
            'direccion',
            'created_by',
            'fotos',
            'puntaje',
            'created_by'
        ]

        labels = {
            'nombre_lugar': 'Nombre del lugar',
            'ciudad': 'Ciudad',
            'categoria': 'Categoria',
            'direccion': 'Direccion',
            'created_by': 'Creado por',
            'fotos': 'Fotos',
            'puntaje': 'Puntaje'

        }

