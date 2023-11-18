from django import forms
from .models import Empleado
from .models import Empleador
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

class BlockFilterForm(forms.Form):
    block_checkboxes = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
    )

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre_empleado', 'email', 'contrasena', 'imagen_empleado', 'organizacion_empleado', 'cargo_empleado'] 

class EmpleadorForm(forms.ModelForm):
    class Meta:
        model = Empleador
        fields = ['nombre_empleador', 'email', 'contrasena', 'imagen_empleador', 'organizacion_empleador'] 

class LoginForm(forms.Form):
    email = forms.EmailField()
    contrasena = forms.CharField(widget=forms.PasswordInput)

