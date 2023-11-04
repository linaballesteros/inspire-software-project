from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Reto


def profile(request):
    return render(request, "profile.html")
