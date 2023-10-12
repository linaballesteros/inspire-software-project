from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home.html")

def my_profile(request):
    return render(request, "profile.html")

def ranking(request):
    return render(request, "ranking.html")

def shop(request):
    return render(request, "shop.html")

def challenges(request):
    return render(request, "challenges.html")

def login(request):
    return render(request, "login.html")

def sign_up(request):
    return render(request, "sign_up.html")

# Create your views here.
