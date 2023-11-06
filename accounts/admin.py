from django.contrib import admin
from .models import Empleado
from .models import Empleador
# Register your models here.
admin.site.register(Empleado)
admin.site.register(Empleador)