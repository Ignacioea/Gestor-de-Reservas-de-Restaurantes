from django import forms
from .models import Rol

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del Rol (Ej: Garzón, Administrador)...',
                    'type': 'text'
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descripción o funciones del rol...',
                    'rows': '3'
                }
            )
        }