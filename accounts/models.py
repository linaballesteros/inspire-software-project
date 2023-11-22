from django.db import models
from datetime import date
from challenges.models import Reto
from django.contrib.auth.models import User

HABILIDADES_LISTA = [
    ("Comunicación efectiva", "Comunicación efectiva"),
    ("Trabajo en equipo", "Trabajo en equipo"),
    ("Resolución de conflictos", "Resolución de conflictos"),
    ("Pensamiento crítico", "Pensamiento crítico"),
    ("Creatividad", "Creatividad"),
    ("Adaptabilidad", "Adaptabilidad"),
    ("Gestión del tiempo", "Gestión del tiempo"),
    ("Liderazgo", "Liderazgo"),
    ("Empatía", "Empatía"),
    ("Habilidades de presentación", "Habilidades de presentación"),
    ("Toma de decisiones", "Toma de decisiones"),
    ("Escucha activa", "Escucha activa"),
    ("Colaboración", "Colaboración"),
    ("Autoconfianza", "Autoconfianza"),
    ("Resiliencia", "Resiliencia"),
    ("Pensamiento analítico", "Pensamiento analítico"),
    ("Capacidad de negociación", "Capacidad de negociación"),
    ("Habilidades interpersonales", "Habilidades interpersonales"),
    ("Gestión del estrés", "Gestión del estrés"),
    ("Planificación y organización", "Planificación y organización"),
]

class Empleado(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    nombre_empleado = models.CharField(max_length=100, default='John Doe')
    imagen_empleado = models.ImageField(upload_to="uploads/")
    organizacion_empleado = models.CharField(max_length=100, default='organización')
    cargo_empleado = models.CharField(max_length=100, default='Empleado')
    tokens_empleado = models.IntegerField(default=0)
    tipo_usuario = models.CharField(max_length=100, default='empleado')
    retos_activos = models.IntegerField(default=0)
    retos_finalizados = models.IntegerField(default=0)
    
    def retos_iniciados(self):
        return RetosIniciados.objects.filter(empleado=self)
class Empleador(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    nombre_empleador =  models.CharField(default="", max_length=100)
    imagen_empleador = models.ImageField(upload_to="uploads/")
    organizacion_empleador =  models.CharField(default="", max_length=100)
    tipo_usuario = models.CharField(max_length=100, default='empleador')

class RetosIniciados(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    reto = models.ForeignKey(Reto, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField(auto_now_add=True) # cuando inició el reto

class RetosFinalizados(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    reto = models.ForeignKey(Reto, on_delete=models.CASCADE)
    fecha_finalizacion = models.DateTimeField(auto_now_add=True) # cuando finalizó el reto