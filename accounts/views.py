from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Reto
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Empleado, RetosIniciados, RetosFinalizados     
from django.db import IntegrityError
from .models import Empleador

# from .forms import EmpleadoForm, EmpleadoLoginForm
# from .forms import EmpleadorForm
# from .forms import LoginForm


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


def profile(request):
    
   tipo_usuario, data_usuario = get_user_type(request)
   
   
   if tipo_usuario is None: # Ambas consultas no tienen resultados, está loggeado como admin o no se ha loggeado y no como empleador o empleado
       print("debuggg")
       return redirect("login_view")
   
   if tipo_usuario == 'empleado':
       # Para mostrar los retos que se encuentran en Estado = Iniciado en el perfil
       empleado = request.user.empleado
       retos_iniciados_usuario = RetosIniciados.objects.filter(empleado=empleado)
       retos_iniciados = Reto.objects.filter(id__in=retos_iniciados_usuario.values('reto_id'), estado='ACTIVO')
       cantidad_retos_iniciados = retos_iniciados_usuario.count()

       
       print(retos_iniciados)
       print("-------")
       print(retos_iniciados_usuario)
       
       retos_finalizados_usuario = RetosFinalizados.objects.filter(empleado=empleado)
       retos_finalizados = Reto.objects.filter(id__in=retos_iniciados_usuario.values('reto_id'), estado='FINALIZADO')
       cantidad_retos_finalizados = retos_finalizados_usuario.count()
       
       # Para mostrar los retos que se encuentran en estado = Finalizado en el perfil
       return render(request, 'profile_employee.html', {'data_usuario':data_usuario, 'retos_iniciados':retos_iniciados, 'retos_iniciados_usuario':retos_iniciados_usuario, 'cantidad_retos_iniciados':cantidad_retos_iniciados, 'retos_finalizados':retos_finalizados, 'retos_finalizados_usuario':retos_finalizados_usuario, 'cantidad_retos_finalizados':cantidad_retos_finalizados})
   
   elif tipo_usuario == 'empleador':
       return render(request, 'profile_employer.html', data_usuario)

def create_employer_(request): # for creating employees
    if request.method == 'POST':
        print("posttt")
        if request.POST['password1'] == request.POST['password2']:
            print("pasó el passwords")
            try:
                user = User.objects.create_user(request.POST['username'], 
                                                password = request.POST['password1'], 
                                                email = request.POST['email_empleador'])
                user.save()

                imagen_empleador = request.FILES.get('imagen_empleador')
                
                perfil = Empleador(user = user, 
                                  nombre_empleador = request.POST['nombre_empleador'], 
                                  imagen_empleador= imagen_empleador, 
                                  organizacion_empleador = request.POST['organizacion_empleador'], 
                                  tipo_usuario = 'empleador')
                
                perfil.save()
                
                login(request, user)
                
                messages.success(request, "Registro completado." )
                print("pasó el login")
                return redirect("home2")
            
            except IntegrityError:
                return render(request, "sign_up_employer.html", {'error':'El nombre de usuario ya existe.'})
        else: 
            return render(request, "sign_up_employer.html", {'error':'Las contraseñas no coinciden.'})

    return render(request, 'sign_up_employer.html')

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
                                  tokens_empleado = 0,
                                  tipo_usuario='empleado')
                
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

@login_required
def log_out(request):
    logout(request)
    return redirect('home2')