from django import forms
from .models import *


class FiltroIngredientesForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ["categoria"]

    categoria = forms.ModelChoiceField(
        queryset=CategoriaIngrediente.objects.all(),
        required=False,
    )
    
    inicial_nombre = forms.CharField(
        max_length=1,
        required=False,
    )