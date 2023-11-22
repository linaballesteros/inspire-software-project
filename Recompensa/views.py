from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import recompensa
from accounts.models import Empleado, Empleador
from .forms import ObjectForm

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
# Create your views here.
def Recompensas(request):
    print("Entro a la vista recompensas")
    user_type, data_user = get_user_type(request)
    print(user_type)
    return render(request, "Recompensas.html", {'user_type':user_type, 'data_user':data_user})

def CrearRecompensas(request):
    user_type, data_user = get_user_type(request)
    return render(request, "CrearRecompensas.html", {'user_type':user_type, 'data_user':data_user})
    
def VisualizarRecompensas(request):
    print("Visualizar Recompensas")
    
    Recompensas = recompensa.objects.all()
    Almuerzo="Almuerzo"  
    print("Recompensas:", Recompensas)
    user_type, data_user = get_user_type(request)
    return render(request, "VisualizarRecompensas.html", {'Recompensas': Recompensas,"Almuerzo":Almuerzo, 'user_type':user_type, 'data_user':data_user})


def CrearRecompensas_(request):
    print("Entro a la vista CrearRecompensas_")
    if request.method=="POST":
        form=ObjectForm(request.POST,request.FILES)
        print("post")
        if form.is_valid():
            new_object=form.save()
            print(form.errors)
            print("paso el valid")
        else:
            print(form.errors)
            print("no guardo nada")
    else:
        form=ObjectForm()
    user_type, data_user = get_user_type(request)
    return render(request, "CrearRecompensas.html", {"form":form,'user_type':user_type, 'data_user':data_user})
    
    
