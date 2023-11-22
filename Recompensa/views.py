from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import recompensa
from .forms import ObjectForm


# Create your views here.
def Recompensas(request):
    print("Entro a la vista recompensas")
    return render(request, "Recompensas.html")
def CrearRecompensas(request):
    return render(request,"CrearRecompensas.html")
    
def VisualizarRecompensas(request):
    print("Visualizar Recompensas")
    
    Recompensas = recompensa.objects.all()
    Almuerzo="Almuerzo"  
    print("Recompensas:", Recompensas)
    return render(request, "VisualizarRecompensas.html", {'Recompensas': Recompensas,"Almuerzo":Almuerzo})


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
    
    return render(request,"CrearRecompensas.html",{"form":form})
    
    
