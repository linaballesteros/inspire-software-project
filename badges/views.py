from django.shortcuts import render, redirect
from .models import Insignia, Recibir_insignia
from accounts.models import Empleado, Empleador, RetosFinalizados
from .forms import BadgeForm
from django.contrib.auth.decorators import login_required
from .assign_badge_command import create_assertion, get_challenges
from django.contrib.auth.models import User

@login_required
def main(request):
    return render(request, "main.html")

@login_required
def create_badge(request):  #Creación de insignias
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
        return render(request,'create_badge.html',{'form':form})
    else:
        form = BadgeForm(request.POST, request.FILES)
        return render(request,'create_badge.html',{'form':form})
            

@login_required
def edit_badge(request):
    insignias=Insignia.objects.all()
    if request.method == 'POST':()
        
        
    return render(request, "edit_badge.html", {"insignias": insignias})

def delete_badge(request,insignia_id,id):
    to_delete = Insignia.objects.get(insignia_id=insignia_id)
    to_delete.delete()
    return redirect('edit_badge')

@login_required
def assign_badge(request):
    to_assert = get_challenges()
    return render(request, "assign_badge.html",{'list':to_assert})

def assertion(request, insignia_id,id):
    badge = Insignia.objects.get(insignia_id=insignia_id)
    user = User.objects.get(id=id)
    empleado = Empleado.objects.get(user=user)
    create_assertion(empleado,badge)
    return redirect('assign_badge')
    

def get_user_type(request):
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
