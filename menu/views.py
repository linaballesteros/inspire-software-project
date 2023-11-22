from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from challenges.models import Reto
from django.contrib.auth.decorators import login_required
from accounts.models import Empleado
from django.db import IntegrityError

# Create your views here.
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

def header(request):
    
    tipo_usuario, data_usuario = get_user_type(request)

    return render(request, 'header.html', {'tipo_usuario':tipo_usuario,'data_usuario':data_usuario})
    
def home2(request):
    
    print("-a-")
    print(request.user)
    print("aaa")
    #   print(request.user.type)
    # context = get_user_data(request)
    return render(request, "home2.html")