from django import forms
from .models import *
from django.forms import formset_factory


class FiltroIngredientesForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ["categoria", "mercado_habitual"]

    categoria = forms.ModelChoiceField(
        queryset=CategoriaIngrediente.objects.all(),
        required=False,
    )

    mercado_habitual = forms.ModelChoiceField(
        queryset=Mercado.objects.all(),
        required=False,
    )

    inicial_nombre = forms.CharField(
        max_length=1,
        required=False,
    )
    
class CrudForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ["nombre", "categoria", "mercado_habitual", "descripcion"] 