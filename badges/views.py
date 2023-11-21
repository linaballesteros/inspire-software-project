from django.shortcuts import render

def main(request):
    return render(request, "main.html")

def create_badge(request):
    return render(request, "create_badge.html")

def edit_badge(request):
    insignias=None
    return render(request, "edit_badge.html", {"insignias": insignias})

def assign_badge(request):
    return render(request, "assign_badge.html")
