from django import forms
from .models import PersonaTable


class ClienteForm(forms.ModelForm):

    class Meta:
        model = PersonaTable

        fields = [
            'first_name',
            'last_name',
            'email',
            'fecha_nacimiento',

        ]

        labels = {
            'first_name': 'Primer nombre',
            'last_name': 'Segundo nombre',
            'email': 'Correo electronico',
            'fecha_nacimiento': 'Fecha de nacimiento',
        }


class AdminForm(forms.ModelForm):

    class Meta:
        model = PersonaTable

        fields = [
            'first_name',
            'last_name',
            'email',
            'fecha_nacimiento',
            'rol',
            'status',
            'is_super_admin'

        ]

        labels = {
            'first_name': 'Primer nombre',
            'last_name': 'Segundo nombre',
            'email': 'Correo electronico',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'rol': 'Rol',
            'status': 'status',
            'is_super_admin': 'Es super administrador?',
        }
