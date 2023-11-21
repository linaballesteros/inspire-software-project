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


def header(request):
    user = Empleado.objects.get(user=request.user)
    
    nombre_empleado = user.nombre_empleado
    imagen_empleado = user.imagen_empleado,
    organizacion_empleado = user.organizacion_empleado,
    cargo_empleado = user.cargo_empleado,
    tokens_empleado = user.tokens_empleado
    
    print(nombre_empleado)
    print(tokens_empleado)

    return render(request, 'header.html', {
        'nombre_empleado' : user.nombre_empleado,
        'imagen_empleado' : user.imagen_empleado,
        'organizacion_empleado' : user.organizacion_empleado,
        'cargo_empleado' : user.cargo_empleado,
        'tokens_empleado' : user.tokens_empleado,
    })
    
def home2(request):
    print(request.user)
    # context = get_user_data(request)
    return render(request, "home2.html")