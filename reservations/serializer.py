from rest_framework import serializers
from .models import(
    Rol,
    Usuario,
    Restaurante,
    Sector,
    Mesa,
    Bloqueo,
    Reserva,
    CambioReserva,
    ReservaMesa
    )

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model= Rol
        fields = ("__all__")

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ("__all__")

class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = ("__all__")

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ("__all__")

class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = ("__all__")

class BloqueoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bloqueo
        fields = ("__all__")

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ("__all__")

class CambioReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CambioReserva
        fields = ("__all__")

class ReservaMesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaMesa
        fields = ("__all__")