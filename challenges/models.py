from django.db import models
from datetime import date

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

CANTIDAD_PARTICIPANTES = [(1, 1), (2, 2), (3, 3), (4, 4), (5,5), (6, 6)]





# Create your models here.
class Reto(models.Model):
    nombre =  models.CharField(max_length=100)
    descripcion =  models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="uploads/")
    fecha_publicacion = models.DateField(default=date.today)
    fecha_vencimiento = models.DateField(default=date.today)
    nombre_insignia =  models.CharField(max_length=100)
    categoria_insignia = models.CharField(max_length=100, default='', choices=HABILIDADES_LISTA)  
    tokens =  models.IntegerField()
    limite_participantes = models.IntegerField(default=6, choices=CANTIDAD_PARTICIPANTES) 
    cantidad_ganadores = models.IntegerField()
    
    