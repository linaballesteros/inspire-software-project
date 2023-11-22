from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import datetime, timedelta, timezone
from .forms import ObjectForm
from .models import Reto
from django.contrib.auth.forms import AuthenticationForm
from accounts.models import Empleado, Empleador, RetosIniciados, RetosFinalizados
from badges.models import Recibir_insignia, Insignia
from django.contrib.auth.decorators import login_required

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

def ranking(request):
    return render(request, "ranking.html")

def challenges(request):
    tipo_usuario, data_usuario = get_user_type(request)

    retos = Reto.objects.all()  

    
    if tipo_usuario is None: # Ambas consultas no tienen resultados, está loggeado como admin o no se ha loggeado y no como empleador o empleado
       return redirect("login_view")
    
    if tipo_usuario == 'empleado':
       return render(request, 'challenges_employee.html', data_usuario)
    
    elif tipo_usuario == 'empleador':
       return render(request, 'challenges_employer.html', data_usuario)


def create_challenge(request):
    
    return render(request, "create_challenge.html")

def create_challenge_(request): # for publishing challenges
    print("entro en la funcion de lina")
    if request.method == 'POST':
        form = ObjectForm(request.POST, request.FILES)
        print("posttt")
        if form.is_valid():
            new_object=form.save()
            print(form.errors)
            print("pasó el valid")
        else:
            print(form.errors)  
    else:
        form = ObjectForm()

    return render(request, 'create_challenge.html', {'form': form})

def view_challenges(request):
    tipo_usuario, data_usuario = get_user_type(request)

    retos = Reto.objects.all()  
    print(retos)
    print(tipo_usuario)
    
    if tipo_usuario is None: # Ambas consultas no tienen resultados, está loggeado como admin o no se ha loggeado y no como empleador o empleado
       return redirect("login_view")
    
    if tipo_usuario == 'empleado':
       return render(request, 'view_challenges_employee.html', {'data_usuario':data_usuario, 'retos': retos})
    
    elif tipo_usuario == 'empleador':
        return render(request, "view_challenges_employer.html", {'retos': retos})

def edit_challenge(request, reto_id): # UPDATE RETO
    reto_a_editar = get_object_or_404(Reto, pk=reto_id)
    print("entro antes del if")
    if request.method == "POST" and 'save_changes' in request.POST:
        print("entró al post del edit")
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        imagen = request.FILES.get('imagen')  
        fecha_publicacion = request.POST.get('fecha_publicacion')
        fecha_vencimiento = request.POST.get('fecha_vencimiento')
        nombre_insignia = request.POST.get('nombre_insignia')
        categoria_insignia = request.POST.getlist('categoria_insignia')
        tokens = request.POST.get('tokens')
        limite_participantes = request.POST.get('limite_participantes')  
        cantidad_ganadores = request.POST.get('cantidad_ganadores')  
        
        # updating data of objects in django admin
        reto_a_editar.nombre = nombre
        reto_a_editar.descripcion = descripcion
        
        if imagen:
            reto_a_editar.imagen = imagen
            
        reto_a_editar.fecha_publicacion = fecha_publicacion
        reto_a_editar.fecha_vencimiento = fecha_vencimiento
        reto_a_editar.nombre_insignia = nombre_insignia
        reto_a_editar.categoria_insignia = categoria_insignia
        reto_a_editar.tokens = tokens
        reto_a_editar.limite_participantes = limite_participantes 
        reto_a_editar.cantidad_ganadores = cantidad_ganadores 
        
        
        reto_a_editar.save() # guardar los cambios
        
        return render(request, 'edit_challenge.html', {'reto_a_editar' : reto_a_editar})
    
    elif request.method == "POST" and 'delete_reto' in request.POST:
         reto_a_eliminar = get_object_or_404(Reto, pk=reto_id)
         reto_a_eliminar.delete()
         
         return render(request, 'view_challenges.html', {'reto_a_editar' : reto_a_editar}) 
       
    else:
        form = ObjectForm()
        return render(request, 'edit_challenge.html', {'reto_a_editar' : reto_a_editar})


def show_progress(request):
    fecha_actual = datetime.now(timezone.utc)

    
    inicio_trimestre = fecha_actual - timedelta(days=90)
    inicio_semestre = fecha_actual - timedelta(days=180)
    inicio_anual = fecha_actual - timedelta(days=365)

    # Filtra las insignias según las fechas
    insignias = Recibir_insignia.objects.filter()

    trimestre = {}
    semestre = {}
    anual = {}

    trimestre_empleados = {}
    semestre_empleados = {}
    anual_empleados = {}

    checked = []
    for insignia in Insignia.objects.filter():
        if str(insignia.Nombre) not in checked:
            trimestre[str(insignia.Nombre)] = 0
            semestre[str(insignia.Nombre)] = 0
            anual[str(insignia.Nombre)] = 0
            checked.append(str(insignia.Nombre))

    checked = []
    for empleado in Empleado.objects.filter():
        if str(empleado.nombre_empleado) not in checked:
            trimestre_empleados[str(empleado.nombre_empleado)] = 0
            semestre_empleados[str(empleado.nombre_empleado)] = 0
            anual_empleados[str(empleado.nombre_empleado)] = 0
            checked.append(str(empleado.nombre_empleado))

    for insignia in insignias:  
        fecha_insignia_utc = insignia.fecha.replace(tzinfo=timezone.utc)
        if fecha_insignia_utc >= inicio_trimestre:
            trimestre[str(Insignia.objects.get(pk=insignia.insignia_id.pk).Nombre)] += 1
            trimestre_empleados[str(Empleado.objects.get(pk=insignia.empleado_id.pk).nombre_empleado)] += 1
        if fecha_insignia_utc >= inicio_semestre:
            semestre[str(Insignia.objects.get(pk=insignia.insignia_id.pk).Nombre)] += 1
            semestre_empleados[str(Empleado.objects.get(pk=insignia.empleado_id.pk).nombre_empleado)] += 1
        if fecha_insignia_utc >= inicio_anual:
            anual[str(Insignia.objects.get(pk=insignia.insignia_id.pk).Nombre)] += 1
            anual_empleados[str(Empleado.objects.get(pk=insignia.empleado_id.pk).nombre_empleado)] += 1
    
    trimestre_empleados_nombres = list(trimestre_empleados.keys())
    trimestre_empleados_cantidad = list(trimestre_empleados.values())

    trimestre_zipped = zip(trimestre_empleados_nombres, trimestre_empleados_cantidad)

    semestre_empleados_nombres = list(semestre_empleados.keys())
    semestre_empleados_cantidad = list(semestre_empleados.values())

    semestre_zipped = zip(semestre_empleados_nombres, semestre_empleados_cantidad)

    anual_empleados_nombres = list(anual_empleados.keys())
    anual_empleados_cantidad = list(anual_empleados.values())

    anual_zipped = zip(anual_empleados_nombres, anual_empleados_cantidad)


    return render(request, "show_progress.html", {'trimestre': trimestre, 'semestre': semestre, 'anual': anual, "trimestre_zipped":trimestre_zipped, "semestre_zipped":semestre_zipped, "anual_zipped":anual_zipped})
# Create your views here.
def start_challenge(request, reto_id):
    reto = get_object_or_404(Reto, id=reto_id)
    empleado = request.user.empleado
    
     # ver si el reto ya fue iniciado antes de
    if not RetosIniciados.objects.filter(empleado=empleado, reto=reto).exists():
        RetosIniciados.objects.create(empleado=empleado, reto=reto)
    
    # Actualiza el estado del reto a "Iniciado" en el botón
    reto.estado = 'INICIADO'
    reto.save()

    return HttpResponse(status=204)  # Respuesta sin contenido, solo para no tener errores para retornar

def end_challenge(request, reto_id):
    reto = get_object_or_404(Reto, id=reto_id)
    empleado = request.user.empleado
    
    
    if RetosIniciados.objects.filter(empleado=empleado, reto=reto).exists(): # si ya fue iniciado, quitarlo de iniciados para actualizar la información del perfil
        reto_iniciado = RetosIniciados.objects.get(empleado=empleado, reto=reto)
        reto_iniciado.delete()
        
        if not RetosFinalizados.objects.filter(empleado=empleado, reto=reto).exists(): # ver si el reto ya fue finalizado antes de
            RetosFinalizados.objects.create(empleado=empleado, reto=reto)
    
    # Actualiza el estado del reto a "Finalizado    "
    reto.estado = 'FINALIZADO'
    reto.save()
    
    # actualizar los tokens del empleado cuando finaliza un reto
    cantidad_tokens_reto = reto.tokens
    tokens = empleado.tokens_empleado
    tokens += cantidad_tokens_reto
    empleado.tokens_empleado = tokens
    empleado.save()

    return HttpResponse(status=204)  # Respuesta sin contenido, solo para no tener errores para retornar

