from django.db import models
from datetime import date
from challenges.models import Reto
from django.contrib.auth.models import AbstractUser, Group, Permission

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
    nombre_empleado =  models.CharField(default="", max_length=100)
    email =  models.CharField(default="", max_length=100)
    contrasena =  models.CharField(default="", max_length=100)
    imagen_empleado = models.ImageField(upload_to="uploads/")
    organizacion_empleado =  models.CharField(default="", max_length=100)
    cargo_empleado =  models.CharField(default="", max_length=100)
    tokens_empleado =  models.IntegerField(default=0)
    
    def verificar_contrasena(self, contrasena_ingresada):
    # Lógica para verificar la contraseña
        return self.contrasena == contrasena_ingresada  

class Empleador(models.Model):
    nombre_empleador =  models.CharField(default="", max_length=100)
    email =  models.CharField(default="", max_length=100)
    contrasena =  models.CharField(default="", max_length=100)
    imagen_empleador = models.ImageField(upload_to="uploads/")
    organizacion_empleador =  models.CharField(default="", max_length=100)
    
    groups = models.ManyToManyField(Group, related_name='empleador_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='empleador_user_permissions', blank=True)
    def verificar_contrasena(self, contrasena_ingresada):
        # Lógica para verificar la contraseña
        return self.contrasena == contrasena_ingresada  
    
    


