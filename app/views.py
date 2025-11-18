from django.shortcuts import render
from .models import Ingrediente, CategoriaIngrediente
from .forms import FiltroIngredientesForm 

# Create your views here.
def inicio(request):
    return render(request, "app/inicio.html")


def ingredientes_lista(request):
    form = FiltroIngredientesForm(request.GET)
    ingredientes = Ingrediente.objects.all()

    if form.is_valid():
        categoria_seleccionada = form.cleaned_data.get('categoria')

        if categoria_seleccionada:
            ingredientes = ingredientes.filter(categoria=categoria_seleccionada)

    contexto = {'ingredientes': ingredientes,'form': form,}

    return render(request, "app/ingredientes_lista.html", contexto)