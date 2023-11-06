from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import ObjectForm
from .models import Reto

def home(request):
    return render(request, "home.html")

def home2(request):
    return render(request, "home2.html")

def ranking(request):
    return render(request, "ranking.html")

def shop(request):
    return render(request, "shop.html")

def challenges(request):
    return render(request, "challenges.html")

def create_challenge(request):
    return render(request, "create_challenge.html")

def edit_challenge(request):
    return render(request, "edit_challenge.html")

def create_challenge_(request): # for publishing challenges
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
    retos = Reto.objects.all()  
    print(retos)
    return render(request, "view_challenges.html", {'retos': retos})

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
        
        
        reto_a_editar.save() # save changes
        
        return render(request, 'edit_challenge.html', {'reto_a_editar' : reto_a_editar})
    
    elif request.method == "POST" and 'delete_reto' in request.POST:
         reto_a_eliminar = get_object_or_404(Reto, pk=reto_id)
         reto_a_eliminar.delete()
         
         return render(request, 'view_challenges.html', {'reto_a_editar' : reto_a_editar}) 
       
    else:
        form = ObjectForm()
        return render(request, 'edit_challenge.html', {'reto_a_editar' : reto_a_editar})

def login(request):
    return render(request, "login.html")

# Create your views here.
