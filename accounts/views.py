from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from .models import Reto
from .models import Empleado
from .models import Empleador

from .forms import EmpleadoForm
from .forms import EmpleadorForm
from .forms import LoginForm


def profile(request):
    return render(request, "profile.html")

def sign_up_type(request):
    return render(request, "sign_up_type.html")

def sign_up_employer(request):
    return render(request, "sign_up_employer.html")

def sign_up_employee(request):
    return render(request, "sign_up_employee.html")

def login(request):
    return render(request, "login.html")

def login_view(request):
    if request.method == 'POST':
        print("entró al post")
        form = LoginForm(request.POST)
        if form.is_valid():
            print("entró a la validación del form")
            email = form.cleaned_data['email']
            contrasena = form.cleaned_data['contrasena']

            empleado = Empleado.objects.filter(email=email).first()
            empleador = Empleador.objects.filter(email=email).first()

            if empleado and empleado.verificar_contrasena(contrasena):
                print("entro a verificar contaseña")
                user = authenticate(request, email=email, password=contrasena)
                print(user)
            elif empleador and empleador.verificar_contrasena(contrasena):
                user = authenticate(request, email=email, password=contrasena)

            else:
                error_message = "Credenciales inválidas. Revisa tu correo o contraseña."
                return render(request, 'login.html', {'form': form, 'error_message': error_message})

            if user:
                print("entró al login")
                login(request, user)
                # Redirigir a alguna página después del inicio de sesión
                return redirect('view_challenges')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def create_employee_(request): # for creating employees
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, request.FILES)
        print("posttt")
        if form.is_valid():
            new_object=form.save()
            print(form.errors)
            print("pasó el valid")
        else:
            print(form.errors)  
    else:
        form = EmpleadoForm()

    return render(request, 'sign_up_employee.html', {'form': form})

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

