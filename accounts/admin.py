from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Empleado, Empleador

admin.site.register(Empleado)
admin.site.register(Empleador)

