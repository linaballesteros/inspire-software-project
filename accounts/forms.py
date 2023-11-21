from django import forms
from .models import Empleado
# from .models import Empleador
from django.contrib.auth.forms import UserCreationForm, User, AuthenticationForm
from django.db import transaction

class BlockFilterForm(forms.Form):
    block_checkboxes = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
    )