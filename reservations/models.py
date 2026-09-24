from django.db import models

# Create your models here.

class Rol(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    class Meta:
        db_table_comment = "Roles de usuario en la plataforma (cliente, Administrador, Garzón)"
        
    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20)
    password_hash = models.CharField(max_length=255)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=False)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    class Meta:
        db_table_comment = "información de los clientes y personal del restaurante"
            
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Restaurante(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    capacidad_total = models.IntegerField()
    estado = models.BooleanField(default=True)

    class Meta:
        db_table_comment = "Datos principales de cada local o sucursal"
            
    def __str__(self):
        return f"{self.nombre}, ubicado en {self.direccion}"

class Sector(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)

    class Meta:
        db_table_comment = "ambientes disponibles dentro de cada restaurante (Terraza, inferior, VIP, etc.)"
            
    def __str__(self):
        return f"{self.nombre} {self.restaurante.nombre}"

class Mesa(models.Model):
    codigo_mesa = models.CharField(max_length=10)
    capacidad_min = models.IntegerField()
    capacidad_max = models.IntegerField()
    estado = models.BooleanField(default=True)
    sector = models.ForeignKey(Sector, on_delete = models.CASCADE)

    class Meta:
        db_table_comment = "Mobiliario físico y capacidad asignable para cada sector"
            
    def __str__(self):
        return f"{self.codigo_mesa} {self.sector.nombre}"

class Bloqueo(models.Model):
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    motivo = models.CharField(max_length=100)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)

    class Meta:
        db_table_comment = "Excepciones de disponibilidad (puede ser por mantención, avería o eventos privados)"
  
    def __str__(self):
        return f"Bloqueo: {self.mesa.nombre}: {self.motivo}"

class Reserva(models.Model):
    codigo_reserva = models.CharField(max_length=15)
    fecha_reserva = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin_estimada= models.TimeField()
    cantidad_personas = models.IntegerField()
    estado = models.CharField(max_length=20)
    comentario = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurante, on_delete = models.CASCADE)

    class Meta:
        db_table_comment = "Registro central de las reservas realizadas por los clientes"
      
    def __str__(self):
        return self.codigo_reserva

class CambioReserva(models.Model):
    estado_anterior = models.CharField(max_length=20)
    estado_actual = models.CharField(max_length=20)
    motivo_cambio = models.CharField(max_length=255)
    fecha_cambio = models.DateTimeField(auto_now_add=True)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)

    class Meta:
        db_table_comment = "Historial de auditoría para cambios de estado en las reservas"
      
    def __str__(self):
        return f"cambio en {self.reserva.codigo_reserva}, cambio de estado: {self.estado_anterior} -> {self.estado_actual} por el motivo de {self.motivo_cambio}"

class ReservaMesa(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete = models.CASCADE)
    mesa = models.ForeignKey(Mesa, on_delete = models.CASCADE)

    class Meta:
        db_table_comment = "tabla intermedia para asociar una o múltiples mesas físicas a una reserva"
        constraints = [
            models.UniqueConstraint(
                fields=["reserva", "mesa"],
                name = "unique_reserva_mesa"
            )
        ]
    def __str__(self):
        return f"Reserva {self.reserva.codigo_reserva} asignada a Mesa {self.mesa.codigo_mesa}"

    