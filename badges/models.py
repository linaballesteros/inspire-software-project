from django.db import models
from accounts.models import Empleado, Empleador
from challenges.models import Reto
from accounts.models import HABILIDADES_LISTA

class Insignia(models.Model):  #Modelo de las insignias (BadgeClasses)
    insignia_id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=(50))
    Emisor = models.ForeignKey(Empleador, verbose_name='ID Emisor', on_delete=models.CASCADE)
    Habilidades = models.CharField(max_length=100, default='', choices=HABILIDADES_LISTA)
    Reto = models.ForeignKey(Reto, verbose_name='ID Reto',on_delete=models.CASCADE)
    Imagen = models.ImageField(upload_to='uploads/')
    
class Recibir_insignia(models.Model):  #Modelo de las asignaciones (Assertions)
    assertion_id = models.AutoField(primary_key=True)
    insignia_id = models.ForeignKey(Insignia,verbose_name='ID Insignia Otorgada',on_delete=models.CASCADE)
    empleado_id = models.ForeignKey(Empleado,verbose_name='ID empleado',on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    