from django.db import models

# Modelo para las Ubicaciones
class Ubicacion(models.Model):
    id = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=255)  # Dirección del proyecto
    ciudad = models.CharField(max_length=100)  # Ciudad donde se encuentra el proyecto
    provincia = models.CharField(max_length=100)  # Provincia o estado
    pais = models.CharField(max_length=100)  # País
    codigo_postal = models.CharField(max_length=10)  # Código postal

    def __str__(self):
        return f"{self.direccion}, {self.ciudad}, {self.provincia}, {self.pais}"

# Modelo para los Proyectos
class Proyecto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)  # Nombre del proyecto
    descripcion = models.TextField()  # Descripción del proyecto
    fecha_inicio = models.DateField()  # Fecha de inicio del proyecto
    fecha_fin = models.DateField(null=True, blank=True)  # Fecha de finalización del proyecto (puede ser nula)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, related_name="proyectos")  # Relación con la ubicación
    ESTADO_CHOICES = [
        ('P', 'Planificación'),
        ('E', 'En Progreso'),
        ('C', 'Completado'),
        ('S', 'Suspendido'),
    ]
    estado = models.CharField(
        max_length=1,
        choices=ESTADO_CHOICES,
        default='P',
    )  # Estado del proyecto

    def __str__(self):
        return f"{self.nombre} - {self.get_estado_display()}"

# Modelo para los Presupuestos
class Presupuesto(models.Model):
    id = models.AutoField(primary_key=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="presupuestos")  # Relación con el proyecto
    monto = models.DecimalField(max_digits=15, decimal_places=2)  # Monto del presupuesto
    descripcion = models.TextField()  # Descripción del presupuesto
    fecha_creacion = models.DateField(auto_now_add=True)  # Fecha de creación del presupuesto
    TIPO_CHOICES = [
        ('I', 'Inicial'),
        ('A', 'Ajustado'),
        ('F', 'Final'),
    ]
    tipo = models.CharField(
        max_length=1,
        choices=TIPO_CHOICES,
        default='I',
    )  # Tipo de presupuesto

    def __str__(self):
        return f"Presupuesto {self.get_tipo_display()} - {self.proyecto.nombre}"

# Modelo para los Permisos
class Permiso(models.Model):
    id = models.AutoField(primary_key=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="permisos")  # Relación con el proyecto
    tipo_permiso = models.CharField(max_length=100)  # Tipo de permiso (ejemplo: construcción, ambiental)
    fecha_emision = models.DateField()  # Fecha de emisión del permiso
    fecha_vencimiento = models.DateField()  # Fecha de vencimiento del permiso
    ESTADO_CHOICES = [
        ('V', 'Vigente'),
        ('E', 'Expirado'),
        ('R', 'Revocado'),
    ]
    estado = models.CharField(
        max_length=1,
        choices=ESTADO_CHOICES,
        default='V',
    )  # Estado del permiso

    def __str__(self):
        return f"Permiso {self.tipo_permiso} - {self.proyecto.nombre} ({self.get_estado_display()})"