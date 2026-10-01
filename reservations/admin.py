from django.contrib import admin
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

#registro de los modelos de datos en el administrador
admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Restaurante)
admin.site.register(Sector)
admin.site.register(Mesa)
admin.site.register(Bloqueo)
admin.site.register(Reserva)
admin.site.register(CambioReserva)
admin.site.register(ReservaMesa)
