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
    path("", include(enrutador.urls)),
]