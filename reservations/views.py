from django.shortcuts import render 
from rest_framework import viewsets
from django.urls import reverse_lazy
from .forms import RolForm
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from . import models as mod 
from . import serializer as ser
# Create your views here.

def home(request):
    return render(request, "home.html")

#rol
class RolListView(ListView):
    model = mod.Rol
    template_name = "roles/lista_roles.html"
    context_object_name="roles"

class RolCreateView(CreateView):
    model = mod.Rol
    form_class = RolForm
    template_name = "roles/form_rol.html"
    success_url = reverse_lazy("roles")

class RolUpdateView(UpdateView):
    model = mod.Rol
    form_class = RolForm
    template_name = "roles/form_rol.html"
    success_url = reverse_lazy("roles")

class RolDeleteView(DeleteView):
    model = mod.Rol
    template_name = "roles/eliminar_rol.html"
    success_url = reverse_lazy("roles")

class RolViewSet (viewsets.ModelViewSet):
    queryset = mod.Rol.objects.all()
    serializer_class = ser.RolSerializer

class UsuarioViewSet (viewsets.ModelViewSet):
    queryset = mod.Usuario.objects.all()
    serializer_class = ser.UsuarioSerializer


class RestauranteViewSet (viewsets.ModelViewSet):
    queryset = mod.Restaurante.objects.all()
    serializer_class = ser.RestauranteSerializer

class SectorViewSet (viewsets.ModelViewSet):
    queryset = mod.Sector.objects.all()
    serializer_class = ser.SectorSerializer

class MesaViewSet (viewsets.ModelViewSet):
    queryset = mod.Mesa.objects.all()
    serializer_class = ser.MesaSerializer

class BloqueoViewSet (viewsets.ModelViewSet):
    queryset = mod.Bloqueo.objects.all()
    serializer_class = ser.BloqueoSerializer

class ReservaViewSet (viewsets.ModelViewSet):
    queryset = mod.Reserva.objects.all()
    serializer_class = ser.ReservaSerializer

class CambioReservaViewSet (viewsets.ModelViewSet):
    queryset = mod.CambioReserva.objects.all()
    serializer_class = ser.CambioReservaSerializer

class ReservaMesaViewSet (viewsets.ModelViewSet):
    queryset = mod.ReservaMesa.objects.all()
    serializer_class = ser.ReservaMesaSerializer