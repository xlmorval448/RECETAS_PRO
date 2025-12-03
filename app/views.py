from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.forms import formset_factory


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

    return render(request, "app/index.html", {'ingredientes': ingredientes,'form': form})


def ingrediente_crud(request, pk):
    ingrediente = get_object_or_404(Ingrediente, pk=pk)
    
    if request.method == 'POST':
        crud_form = CrudForm(request.POST, instance=ingrediente)

        if crud_form.is_valid():
            crud_form.save()
            return redirect('ingredientes_lista')
    else:
        crud_form = CrudForm(instance=ingrediente)
        
    return render(request, "app/ingrediente_crud.html", {'ingrediente': ingrediente,'crud_form': crud_form,'editando': True})

def ingrediente_eliminar(request, pk):
    ingrediente = get_object_or_404(Ingrediente, pk=pk)

    if request.method == 'POST':
        ingrediente.delete()
        return redirect('ingredientes_lista') 
    
    return render(request, 'app/confirmar_borrado.html', {'ingrediente': ingrediente})

def ingrediente_nuevo(request):
    formularioCrud = formset_factory(CrudForm, extra=3)
    
    if request.method == 'POST':
        formularios = formularioCrud(request.POST)
        if formularios.is_valid():
            for form in formularios:
                if form.has_changed():
                    form.save()
            return redirect('ingredientes_lista')    
        
    else:
        formularios = formularioCrud()

    return render(request, "app/ingrediente_nuevo.html", {"formularios": formularios})

def relaciones(request):
    recetas = Receta.objects.all()
    ingredientes =  Ingrediente.objects.all()
    return render(request, "app/relaciones.html", {"recetas":recetas,"ingredientes":ingredientes})

def receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    ingredientes =  Ingrediente.objects.exclude(id__in=receta.ingredientes.all())

    if request.method == 'POST':
        ingrediente = request.POST.get('ingrediente_id')
        receta.ingredientes.add(ingrediente)
        return redirect('receta', pk=pk)
    
    return render(request, 'app/receta.html', {'receta': receta,"ingredientes":ingredientes})

def eliminar_ingrediente_receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    ingredientes =  Ingrediente.objects.exclude(id__in=receta.ingredientes.all())

    if request.method == 'POST':
        ingrediente = request.POST.get('ingrediente_id')
        receta.ingredientes.add(ingrediente)
        return redirect('receta', pk=pk)
    
    return render(request, 'app/receta.html', {'receta': receta,"ingredientes":ingredientes})