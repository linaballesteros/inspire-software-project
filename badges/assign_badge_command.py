from accounts.models import Empleado,Empleador, RetosFinalizados
from .models import Insignia, Recibir_insignia
from challenges.models import Reto
from datetime import date



def get_challenges(): #comando para obtener los retos y sus respectivas insignias
    retos_finalizados = RetosFinalizados.objects.all()
    reto_insignia = []
    for reto in retos_finalizados:
        insignia = Insignia.objects.get(Reto=reto.reto) 
        try:
            assertion = Recibir_insignia.objects.get(insignia_id=insignia,empleado_id=reto.empleado)
        except:
            assertion = None
        if assertion == None:
            tup = (reto,insignia)
            reto_insignia.append(tup)
    return reto_insignia


    
def create_assertion(empleado,insignia): #COmando para crear el assertion
    assertion = Recibir_insignia.objects.create(
        empleado_id = empleado,
        insignia_id = insignia

    )
    return assertion
    
    
    

            