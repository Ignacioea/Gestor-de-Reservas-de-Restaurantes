from django.shortcuts import render 
from rest_framework import viewsets

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

from .serializer import(
    RolSerializer,
    UsuarioSerializer,
    RestauranteSerializer,
    SectorSerializer,
    MesaSerializer,
    BloqueoSerializer,
    ReservaSerializer,
    CambioReservaSerializer,
    ReservaMesaSerializer
)
# Create your views here.

def home(request):
    return render(request, "home.html")

#creación de vistas basadas en clase

class RolViewSet (viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer


class UsuarioViewSet (viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class RestauranteViewSet (viewsets.ModelViewSet):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer

class SectorViewSet (viewsets.ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer

class MesaViewSet (viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer

class BloqueoViewSet (viewsets.ModelViewSet):
    queryset = Bloqueo.objects.all()
    serializer_class = BloqueoSerializer

class ReservaViewSet (viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class CambioReservaViewSet (viewsets.ModelViewSet):
    queryset = CambioReserva.objects.all()
    serializer_class = CambioReservaSerializer

class ReservaMesaViewSet (viewsets.ModelViewSet):
    queryset = ReservaMesa.objects.all()
    serializer_class = ReservaMesaSerializer