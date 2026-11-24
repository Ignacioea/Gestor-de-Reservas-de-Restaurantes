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


]