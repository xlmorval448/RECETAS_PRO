from django import forms
from .models import Ingrediente, CategoriaIngrediente


class FiltroIngredientesForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ["categoria"]

        categoria = forms.ModelChoiceField(
            queryset=CategoriaIngrediente.objects.all(),
            label="Filtrar por Categoría",
            required=False,
        )
