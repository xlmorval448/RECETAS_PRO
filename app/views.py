from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

# Create your views here.
def ingredientes_lista(request):
    form = FiltroIngredientesForm(request.GET)
    ingredientes = Ingrediente.objects.all()

    if form.is_valid():
        categoria_seleccionada = form.cleaned_data.get('categoria')
        inicial_seleccionada = form.cleaned_data.get('inicial_nombre')
        mercado_habitual = form.cleaned_data.get('mercado_habitual')

        if categoria_seleccionada:
            ingredientes = ingredientes.filter(categoria=categoria_seleccionada)

        if mercado_habitual:
            ingredientes = ingredientes.filter(mercado_habitual=mercado_habitual)

        if inicial_seleccionada:
            ingredientes = ingredientes.filter(nombre__istartswith=inicial_seleccionada)

    return render(request, "app/ingredientes_lista.html", {'ingredientes': ingredientes,'form': form})


def ingrediente_crud(request, pk):
    ingrediente = get_object_or_404(Ingrediente, pk=pk)
    
    if request.method == 'POST':
        crud_form = CrudForm(request.POST, instance=ingrediente)

        if crud_form.is_valid():
            crud_form.save()
            return redirect('ingrediente_lista')
    else:
        crud_form = CrudForm(instance=ingrediente)
        
    return render(request, "app/ingredientes_detalle_editar.html", {'ingrediente': ingrediente,'crud_form': crud_form,'es_edicion': True})

def ingrediente_eliminar(request, pk):
    ingrediente = get_object_or_404(Ingrediente, pk=pk)
    ingrediente.delete()
    return redirect('ingrediente_lista')