from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Empleado, Empleador, RetosFinalizados, RetosIniciados

admin.site.register(Empleado)
admin.site.register(Empleador)
admin.site.register(RetosIniciados)
admin.site.register(RetosFinalizados)
