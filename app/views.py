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

    return render(request, "app/ingredientes_lista.html", {'ingredientes': ingredientes,'form': form})


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
    receta_obj = get_object_or_404(Receta, pk=pk)
    # Obtenemos todos los objetos IngredienteReceta relacionados con la receta
    ingredientes_receta = receta_obj.ingredientereceta_set.all()
    
    if request.method == 'POST':
        # Instanciamos el formulario con los datos POST
        form = IngredienteRecetaForm(request.POST)
        
        if form.is_valid():
            # Obtenemos los datos limpios
            nueva_cantidad = form.cleaned_data['cantidad']
            ingrediente_obj = form.cleaned_data['ingrediente'] # Objeto Ingrediente
            nueva_medida = form.cleaned_data['medida'] # Nueva medida (se usará si se crea o actualiza)

            try:
                # 1. Intentar encontrar un IngredienteReceta existente para esta Receta y este Ingrediente
                ingrediente_receta_existente = IngredienteReceta.objects.get(
                    receta=receta_obj,
                    ingrediente=ingrediente_obj
                )

                # 2. Si existe: Usamos F() para realizar la suma de forma atómica en la base de datos.
                # Esto es más seguro, especialmente en entornos concurrentes.
                ingrediente_receta_existente.cantidad = F('cantidad') + nueva_cantidad
                ingrediente_receta_existente.medida = nueva_medida # Opcionalmente, actualizamos la medida
                ingrediente_receta_existente.save()
                
                # Nota: Es recomendable llamar a .refresh_from_db() si se necesita el valor actualizado 
                # de 'cantidad' inmediatamente en esta vista, aunque para el redirect no es necesario.
                
            except ObjectDoesNotExist:
                # 3. Si no existe: Creamos un nuevo IngredienteReceta.
                nuevo_ingrediente_receta = form.save(commit=False)
                nuevo_ingrediente_receta.receta = receta_obj
                # Los campos 'ingrediente', 'cantidad' y 'medida' ya están seteados por form.save(commit=False)
                nuevo_ingrediente_receta.save()
                
            # Redirigir a la misma página para ver los cambios y limpiar el formulario
            return redirect('receta', pk=pk)
    else:
        form = IngredienteRecetaForm() # Formulario vacío para GET

    # Renderizar la plantilla con los datos necesarios
    return render(request, 'app/receta.html', {
        'receta': receta_obj,
        'ingredientes': ingredientes_receta,
        'form': form
    })

# def eliminar_ingrediente_receta(request, pk):
#     receta = get_object_or_404(Receta, pk=pk)
#     ingredientes =  Ingrediente.objects.exclude(id__in=receta.ingredientes.all())

#     if request.method == 'POST':
#         ingrediente = request.POST.get('ingrediente_id')
#         receta.ingredientes.add(ingrediente)
#         return redirect('receta', pk=pk)

#     return render(request, 'app/receta.html', {'receta': receta,"ingredientes":ingredientes})