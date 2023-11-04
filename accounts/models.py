from django.db import models
from datetime import date
from challenges.models import Reto

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
    nombre =  models.CharField(max_length=100)
    email =  models.CharField(max_length=100)
    contrasena =  models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="uploads/")
    organizacion =  models.CharField(max_length=100)
    cargo =  models.CharField(max_length=100)
    tokens =  models.IntegerField()

class Empleador(models.Model):
    nombre =  models.CharField(max_length=100)
    email =  models.CharField(max_length=100)
    contrasena =  models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="uploads/")
    organizacion =  models.CharField(max_length=100)
    
    
    
    