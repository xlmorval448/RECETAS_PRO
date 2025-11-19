from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def ingredientes_lista(request):
    form = FiltroIngredientesForm(request.GET)
    ingredientes = Ingrediente.objects.all()

    if form.is_valid():
        categoria_seleccionada = form.cleaned_data.get('categoria')
        inicial_seleccionada = form.cleaned_data.get('inicial_nombre')

        if categoria_seleccionada:
            ingredientes = ingredientes.filter(categoria=categoria_seleccionada)

        if inicial_seleccionada:
            ingredientes = ingredientes.filter(nombre__istartswith=inicial_seleccionada)

    return render(request, "app/ingredientes_lista.html", {'ingredientes': ingredientes,'form': form})
