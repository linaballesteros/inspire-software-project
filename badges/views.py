from django.shortcuts import render, redirect
from .models import Insignia, Recibir_insignia
from accounts.models import Empleado, Empleador, RetosFinalizados
from .forms import BadgeForm
from django.contrib.auth.decorators import login_required
from .assign_badge_command import create_assertion, get_challenges
from django.contrib.auth.models import User
from challenges.models import Reto

@login_required
def main(request):
    return render(request, "main.html")

@login_required
def create_badge(request):  #Creación de insignias
    
    retos = Reto.objects.all() 
    reto_sin_crear = []
    for reto in retos: #obtención de retos aun no logados con insignia
        try:
            badge = Insignia.objects.get(Reto=reto)
        except:
            badge=None
        if badge==None:
            reto_sin_crear.append(reto)
            
        
    if request.method == 'POST':
        form = BadgeForm(request.POST, request.FILES)
        if form.is_valid():
            badge_class = form.save(commit=False)
            empleador = Empleador.objects.get(user=request.user)
            badge_class.Emisor = empleador
            badge_class.Habilidades = badge_class.Reto.categoria_insignia
            badge_class.save()          
            return redirect('main_page')
        else:
            print(form.errors)
        return render(request,'create_badge.html',{'form':form, 'Retos':reto_sin_crear})
    else:
        form = BadgeForm(request.POST, request.FILES)
        return render(request,'create_badge.html',{'form':form,'Retos':reto_sin_crear})
            

@login_required
def edit_badge(request): #eliminar insignia
    insignias=Insignia.objects.all()
    if request.method == 'POST':()
        
        
    return render(request, "edit_badge.html", {"insignias": insignias})

def delete_badge(request,insignia_id,id): #view para el delete en la base de datos
    to_delete = Insignia.objects.get(insignia_id=insignia_id)
    to_delete.delete()
    return redirect('edit_badge')

@login_required
def assign_badge(request): #asignar insignia 
    to_assert = get_challenges()
    return render(request, "assign_badge.html",{'list':to_assert})

def assertion(request, insignia_id,id): #Creación del assertion
    badge = Insignia.objects.get(insignia_id=insignia_id)
    user = User.objects.get(id=id)
    empleado = Empleado.objects.get(user=user)
    create_assertion(empleado,badge)
    return redirect('assign_badge')
    

def get_user_type(request): #obtener el tipo del usuario
    try:
        empleado = Empleado.objects.get(user=request.user)
        return 'empleado', {
            'nombre_empleado': empleado.nombre_empleado,
            'imagen_empleado': empleado.imagen_empleado,
            'organizacion_empleado': empleado.organizacion_empleado,
            'cargo_empleado': empleado.cargo_empleado,
            'tokens_empleado': empleado.tokens_empleado,
        }
    except:
        try:
            empleador = Empleador.objects.get(user=request.user)
            return 'empleador', {
                'nombre_empleador': empleador.nombre_empleador,
                'imagen_empleador': empleador.imagen_empleador,
                'organizacion_empleador': empleador.organizacion_empleador,
            }
        except: # controlar el error en caso de que no se haya registrado y quiera ingresar al perfil
            return None, None
