from accounts.models import Empleado, Empleador, RetosIniciados, RetosFinalizados
from badges.models import Recibir_insignia, Insignia
from datetime import datetime, timedelta

insignia1 = Insignia.objects.get(Nombre="Capacidad de Negociación")
insignia2 = Insignia.objects.get(Nombre="Comunicación efectiva")
insignia3 = Insignia.objects.get(Nombre="Trabajo en equipo")
insignia4 = Insignia.objects.get(Nombre="Gestión del tiempo")
insignia5 = Insignia.objects.get(Nombre="Adaptabilidad")


empleado1 = Empleado.objects.get(nombre_empleado="david")
empleado2 = Empleado.objects.get(nombre_empleado="Juan")
empleado3 = Empleado.objects.get(nombre_empleado="Sofía")
empleado4 = Empleado.objects.get(nombre_empleado="Pedro")
empleado5 = Empleado.objects.get(nombre_empleado="María")

fecha_inicial = datetime.now() - timedelta(days=300)

      
recibida = Recibir_insignia(insignia_id=insignia4,empleado_id=empleado5,fecha=fecha_inicial)
recibida.save()


for insignia in Recibir_insignia.objects.all():
    print(insignia.fecha)

"""
class Recibir_insignia(models.Model):  #Modelo de las asignaciones (Assertions)
    assertion_id = models.AutoField(primary_key=True)
    insignia_id = models.ForeignKey(Insignia,verbose_name='ID Insignia Otorgada',on_delete=models.CASCADE)
    empleado_id = models.ForeignKey(Empleado,verbose_name='ID empleado',on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
"""