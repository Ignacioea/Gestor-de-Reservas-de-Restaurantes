from django import forms
from django.contrib.auth.hashers import make_password
from . import models as mod

class RolForm(forms.ModelForm):
    class Meta:
        model = mod.Rol
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

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = mod.Usuario
        fields = [
            'nombre',
            'apellido',
            'email',
            'telefono',
            'password_hash',
            'rol',
            'estado',
        ]
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre...',
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellido...',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'correo@ejemplo.com',
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '+56 9 1234 5678',
                }
            ),
            'password_hash': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Contraseña...',
                }
            ),
            'rol': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                }
            ),
        }

    # Encriptar contraseña antes de guardarla en password_hash
    def save(self, commit=True):
        usuario = super().save(commit=False)
        if self.cleaned_data.get('password_hash'):
            usuario.password_hash = make_password(self.cleaned_data['password_hash'])
        if commit:
            usuario.save()
        return usuario

class RestauranteForm(forms.ModelForm):
    class Meta:
        model = mod.Restaurante
        fields = [
            'nombre',
            'direccion',
            'telefono',
            'capacidad_total',
            'estado',
        ]
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del local o sucursal...'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Dirección completa...'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '+56 9 1234 5678'
                }
            ),
            'capacidad_total': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ej: 80',
                    'min': '1'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
        }


class SectorForm(forms.ModelForm):
    class Meta:
        model = mod.Sector
        fields = [
            'restaurante',
            'nombre',
            'descripcion',
        ]
        widgets = {
            'restaurante': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ej: Terraza, Salón Principal, VIP...',
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descripción o características del sector (opcional)...',
                    'rows': '3',
                }
            ),
        }