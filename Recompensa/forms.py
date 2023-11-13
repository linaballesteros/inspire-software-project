from django import forms
from .models import recompensa

class BlockFilterForm(forms.Form):
    block_checkboxes = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
    )

class ObjectForm(forms.ModelForm):
    class Meta:
        model = recompensa
        fields = ['nombre', 'logo', 'tokens'] 
