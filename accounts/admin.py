from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Empleado

admin.site.register(Empleado)

