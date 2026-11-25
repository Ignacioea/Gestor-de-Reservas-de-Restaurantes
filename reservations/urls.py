from django.urls import path, include
from . import views

from rest_framework import routers

from reservations import views

enrutador = routers.DefaultRouter()

enrutador.register(r"roles", views.RolViewSet)
enrutador.register(r"usuario", views.UsuarioViewSet)
enrutador.register(r"restaurante", views.RestauranteViewSet)
enrutador.register(r"sector", views.SectorViewSet)
enrutador.register(r"mesa", views.MesaViewSet)
enrutador.register(r"bloqueo", views.BloqueoViewSet)
enrutador.register(r"reserva", views.ReservaViewSet)
enrutador.register(r"cambio-reserva", views.CambioReservaViewSet)
enrutador.register(r"reserva-mesa", views.ReservaMesaViewSet)


urlpatterns = [
    #vistas de DRF
    path("api/", include(enrutador.urls)),

    #vistas de templates (HTML)
    #ROLES
    path("roles/", views.RolListView.as_view(), name="roles"),
    path("roles/crear/", views.RolCreateView.as_view(), name="crear_rol"),
    path("roles/editar/<int:pk>/", views.RolUpdateView.as_view(), name="editar_rol"),
    path("roles/eliminar/<int:pk>/", views.RolDeleteView.as_view(), name="eliminar_rol"),

    #USUARIOS
    path("usuarios/", views.UsuarioListView.as_view(), name="usuarios"),
    path("usuarios/crear", views.UsuarioCreateView.as_view(), name="crear_usuarios"),
    path("usuarios/editar/<int:pk>/", views.UsuarioUpdateView.as_view(), name="editar_usuarios"),
    path("usuarios/eliminar/<int:pk>/", views.UsuarioDeleteView.as_view(), name="eliminar_usuarios"),

    #RESTAURANTES
    path("restaurante/", views.RestauranteListView.as_view(), name="restaurante"),
    path("restaurante/crear", views.RestauranteCreateView.as_view(), name="crear_restaurante"),
    path("restaurante/editar/<int:pk>/", views.RestauranteUpdateView.as_view(), name="editar_restaurante"),
    path("restaurante/eliminar/<int:pk>/", views.RestauranteDeleteView.as_view(), name="eliminar_restaurante"),

    #SECTORES
    path("sector/", views.SectorListView.as_view(), name="sector"),
    path("sector/crear", views.SectorCreateView.as_view(), name="crear_sector"),
    path("sector/editar/<int:pk>/", views.SectorUpdateView.as_view(), name="editar_sector"),
    path("sector/eliminar/<int:pk>/", views.SectorDeleteView.as_view(), name="eliminar_sector"),

    #MESAS
    path("mesa/", views.MesaListView.as_view(), name="mesa"),
    path("mesa/crear", views.MesaCreateView.as_view(), name="crear_mesa"),
    path("mesa/editar/<int:pk>/", views.MesaUpdateView.as_view(), name="editar_mesa"),
    path("mesa/eliminar/<int:pk>/", views.MesaDeleteView.as_view(), name="eliminar_mesa"),

    #reservas
    path("reserva/", views.ReservaListView.as_view(), name="reserva"),
    path("reserva/crear", views.ReservaCreateView.as_view(), name="crear_reserva"),
    path("reserva/editar/<int:pk>/", views.ReservaUpdateView.as_view(), name="editar_reserva"),
    path("reserva/eliminar/<int:pk>/", views.ReservaDeleteView.as_view(), name="eliminar_reserva"),
    #reservas
    path("bloqueo/", views.BloqueoListView.as_view(), name="bloqueo"),
    path("bloqueo/crear", views.BloqueoCreateView.as_view(), name="crear_bloqueo"),
    path("bloqueo/editar/<int:pk>/", views.BloqueoUpdateView.as_view(), name="editar_bloqueo"),
    path("bloqueo/eliminar/<int:pk>/", views.BloqueoDeleteView.as_view(), name="eliminar_bloqueo"),
              
           
]