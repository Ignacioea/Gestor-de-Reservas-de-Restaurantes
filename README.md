# Gestor-de-Reservas-de-Restaurantes
## Decisiones de Arquitectura y Justificación Técnica (Vistas CRUD)

De acuerdo con el modelo de datos implementado, todas las entidades principales del negocio (`Rol`, `Usuario`, `Restaurante`, `Sector`, `Mesa`, `Bloqueo` y `Reserva`) cuentan con sus respectivas vistas genéricas basadas en clases (`ListView`, `DetailView`, `CreateView`, `UpdateView` y `DeleteView`) completamente funcionales.

Por razones de diseño de base de datos, integridad referencial y lógica de negocio, se han omitido las vistas CRUD independientes para las siguientes dos entidades:

### 1. `CambioReserva` (Historial de Estados)
* **Rol en el modelo:** Tabla de trazabilidad encargada de registrar cada transición de estado de una reserva (`estado_anterior`, `estado_actual`, `fecha_cambio`, `motivo_cambio` y `usuario`).
* **Justificación técnica de omisión:** Al tratarse de un registro de auditoría del sistema, **no debe ser creado, editado ni eliminado manualmente** por los usuarios a través de formularios independientes, ya que esto comprometería la integridad histórica y la confiabilidad de los datos.

### 2. `ReservaMesa` (Tabla Intermedia)
* **Rol en el modelo:** Tabla puente que resuelve la relación Muchos a Muchos (`M:N`) entre `Reserva` y `Mesa` (con restricción de unicidad `UniqueConstraint`), permitiendo asignar una o múltiples mesas físicas a una misma reserva.
* **Justificación técnica de omisión:** Esta entidad no representa un recurso de negocio autónomo, sino una asociación dependiente del ciclo de vida de una reserva. Exponer un CRUD separado fragmentaría la experiencia de usuario y permitiría crear asignaciones huérfanas o inconsistentes fuera del flujo de validación de una reserva.
