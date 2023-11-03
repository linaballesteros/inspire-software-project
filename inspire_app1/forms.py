from django import forms
from .models import Reto

class BlockFilterForm(forms.Form):
    block_checkboxes = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
    )

class ObjectForm(forms.ModelForm):
    class Meta:
        model = Reto
        fields = ['nombre', 'descripcion', 'imagen', 'fecha_publicacion', 'fecha_vencimiento', 'nombre_insignia', 'categoria_insignia', 'tokens', 'limite_participantes', 'cantidad_ganadores'] 
