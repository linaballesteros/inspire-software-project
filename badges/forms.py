from .models import Insignia, Recibir_insignia
from accounts.models import Reto
from django import forms

class BadgeForm(forms.ModelForm): #Form para crear una Insignia
    class Meta:
        model = Insignia
        fields = ['Nombre','Reto','Imagen']

        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Reto'].queryset = Reto.objects.all() 
        