from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Reto
from django.contrib.auth.decorators import login_required
from .models import Empleado
from django.db import IntegrityError
# from .models import Empleador

# from .forms import EmpleadoForm, EmpleadoLoginForm
# from .forms import EmpleadorForm
# from .forms import LoginForm



def profile(request):
    return render(request, "profile.html")

def sign_up_type(request):
    return render(request, "sign_up_type.html")

def sign_up_employer(request):
    return render(request, "sign_up_employer.html")

def sign_up_employee(request):
    return render(request, "sign_up_employee.html")

def login_(request):
    return render(request, "login.html")

def login_view(request):
    
    if request.method == 'POST':
        print("pasó post uvu")

        user = authenticate(request, username=request.POST['username'], password=request.POST['password1'])

        if user is None:
            print("pasó nonee")
            return render(request,'login.html', {'error': 'Usuario o Contraseña Incorrectos'})
        else:
            print(user)
            login(request, user)
            print("pasó loginnn(rq)")

    return render(request, 'login.html')

@login_required
def profile(request):
    user = Empleado.objects.get(user=request.user)
    
    nombre_empleado = user.nombre_empleado
    imagen_empleado = user.imagen_empleado,
    organizacion_empleado = user.organizacion_empleado,
    cargo_empleado = user.cargo_empleado,
    tokens_empleado = user.tokens_empleado
    
    print(nombre_empleado)
    print(tokens_empleado)

    return render(request, 'profile.html', {
        'nombre_empleado' : user.nombre_empleado,
        'imagen_empleado' : user.imagen_empleado,
        'organizacion_empleado' : user.organizacion_empleado,
        'cargo_empleado' : user.cargo_empleado,
        'tokens_empleado' : user.tokens_empleado,
    })

def create_employee_(request): # for creating employees
    if request.method == 'POST':
        print("posttt")
        if request.POST['password1'] == request.POST['password2']:
            print("pasó el passwords")
            try:
                user = User.objects.create_user(request.POST['username'], 
                                                password = request.POST['password1'], 
                                                email = request.POST['email_empleado'])
                user.save()

                imagen_empleado = request.FILES.get('imagen_empleado')
                
                perfil = Empleado(user = user, 
                                  nombre_empleado = request.POST['nombre_empleado'], 
                                  imagen_empleado = imagen_empleado, 
                                  organizacion_empleado = request.POST['organizacion_empleado'], 
                                  cargo_empleado=request.POST['cargo_empleado'],
                                  tokens_empleado = 0)
                
                perfil.save()
                
                login(request, user)
                
                messages.success(request, "Registro completado." )
                print("pasó el login")
                return redirect("home2")
            
            except IntegrityError:
                return render(request, "sign_up_employee.html", {'error':'El nombre de usuario ya existe.'})
        else: 
            return render(request, "sign_up_employee.html", {'error':'Las contraseñas no coinciden.'})

    return render(request, 'sign_up_employee.html')

def create_employer_(request): # for creating employers
    if request.method == 'POST':
        form = EmpleadorForm(request.POST, request.FILES)
        print("posttt")
        if form.is_valid():
            new_object=form.save()
            print(form.errors)
            print("pasó el valid")
        else:
            print(form.errors)  
    else:
        form = EmpleadorForm()

    return render(request, 'sign_up_employer.html', {'form': form})

@login_required
def log_out(request):
    logout(request)
    return redirect('home2')