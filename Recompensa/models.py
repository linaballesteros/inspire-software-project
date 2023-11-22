from django.db import models

# Create your models here.

class recompensa(models.Model):
    nombre=models.CharField(max_length=100)
    logo =models.CharField(max_length=100,default="")
    tokens =  models.IntegerField()
    descripcion=models.CharField(max_length=200,default="")
    
    
