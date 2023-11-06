from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Reto
from .models import Empleado
from .models import Empleador

def profile(request):
    return render(request, "profile.html")

def sign_up_type(request):
    return render(request, "sign_up_type.html")

def sign_up_employer(request):
    return render(request, "sign_up_employer.html")

def sign_up_employee(request):
    return render(request, "sign_up_employee.html")