from django.shortcuts import render 
from rest_framework import viewsets
from django.urls import reverse_lazy
from . import forms as fo
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from . import models as mod 
from . import serializer as ser
# Create your views here.

def home(request):
    return render(request, "home.html")

#ROLES
class RolListView(ListView):
    model = mod.Rol
    template_name = "roles/lista_roles.html"
    context_object_name="roles"

class RolCreateView(CreateView):
    model = mod.Rol
    form_class = fo.RolForm
    template_name = "roles/form_rol.html"
    success_url = reverse_lazy("roles")

class RolUpdateView(UpdateView):
    model = mod.Rol
    form_class = fo.RolForm
    template_name = "roles/form_rol.html"
    success_url = reverse_lazy("roles")

class RolDeleteView(DeleteView):
    model = mod.Rol
    template_name = "roles/eliminar_rol.html"
    success_url = reverse_lazy("roles")

class RolViewSet (viewsets.ModelViewSet):
    queryset = mod.Rol.objects.all()
    serializer_class = ser.RolSerializer

#USUARIOS
class UsuarioListView(ListView):
    model = mod.Usuario
    template_name = "usuarios/lista_usuario.html"
    context_object_name="usuarios"

class UsuarioCreateView(CreateView):
    model = mod.Usuario
    form_class = fo.UsuarioForm
    template_name = "usuarios/form_usuario.html"
    success_url = reverse_lazy("usuarios")

class UsuarioUpdateView(UpdateView):
    model = mod.Usuario
    form_class = fo.UsuarioForm
    template_name = "usuarios/form_usuario.html"
    success_url = reverse_lazy("usuarios")

class UsuarioDeleteView(DeleteView):
    model = mod.Usuario
    template_name = "usuarios/eliminar_usuario.html"
    success_url = reverse_lazy("usuarios")

class UsuarioViewSet (viewsets.ModelViewSet):
    queryset = mod.Usuario.objects.all()
    serializer_class = ser.UsuarioSerializer

#RESTAURANTE
class RestauranteListView(ListView):
    model = mod.Restaurante
    template_name = "restaurante/lista_restaurante.html"
    context_object_name="restaurante"

class RestauranteCreateView(CreateView):
    model = mod.Restaurante
    form_class = fo.RestauranteForm
    template_name = "restaurante/form_restaurante.html"
    success_url = reverse_lazy("restaurante")

class RestauranteUpdateView(UpdateView):
    model = mod.Restaurante
    form_class = fo.RestauranteForm
    template_name = "restaurante/form_restaurante.html"
    success_url = reverse_lazy("restaurante")

class RestauranteDeleteView(DeleteView):
    model = mod.Restaurante
    template_name = "restaurante/eliminar_restaurante.html"
    success_url = reverse_lazy("restaurante")


class RestauranteViewSet (viewsets.ModelViewSet):
    queryset = mod.Restaurante.objects.all()
    serializer_class = ser.RestauranteSerializer

#SECTOR

class SectorListView(ListView):
    model = mod.Sector
    template_name = "sectores/lista_sector.html"
    context_object_name="sector"

class SectorCreateView(CreateView):
    model = mod.Sector
    form_class = fo.SectorForm
    template_name = "sectores/form_sector.html"
    success_url = reverse_lazy("sector")

class SectorUpdateView(UpdateView):
    model = mod.Sector
    form_class = fo.SectorForm
    template_name = "sectores/form_sector.html"
    success_url = reverse_lazy("sector")

class SectorDeleteView(DeleteView):
    model = mod.Sector
    template_name = "sectores/eliminar_sector.html"
    success_url = reverse_lazy("sector")

class SectorViewSet (viewsets.ModelViewSet):
    queryset = mod.Sector.objects.all()
    serializer_class = ser.SectorSerializer

#MESAS
class MesaViewSet (viewsets.ModelViewSet):
    queryset = mod.Mesa.objects.all()
    serializer_class = ser.MesaSerializer

#BLOQUEO
class BloqueoViewSet (viewsets.ModelViewSet):
    queryset = mod.Bloqueo.objects.all()
    serializer_class = ser.BloqueoSerializer

#MESAS
class ReservaViewSet (viewsets.ModelViewSet):
    queryset = mod.Reserva.objects.all()
    serializer_class = ser.ReservaSerializer

class CambioReservaViewSet (viewsets.ModelViewSet):
    queryset = mod.CambioReserva.objects.all()
    serializer_class = ser.CambioReservaSerializer

class ReservaMesaViewSet (viewsets.ModelViewSet):
    queryset = mod.ReservaMesa.objects.all()
    serializer_class = ser.ReservaMesaSerializer