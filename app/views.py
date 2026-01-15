from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
class IngredienteListaView(ListView):
    template_name = "app/ingredientes_lista.html"
    context_object_name = "ingredientes"
    model = Ingrediente
    paginate_by = 3


class IngredienteMostrarView(DetailView):
    template_name = "app/ingrediente_mostrar.html"
    context_object_name = "ingrediente"
    model = Ingrediente


class IngredienteEditarView(UpdateView):
    template_name = "app/ingrediente_editar.html"
    model = Ingrediente
    form_class = IngredienteForm
    success_url = reverse_lazy("ingredientes_lista")
    context_object_name = "ingrediente"


class IngredienteEliminarView(DeleteView):
    template_name = "app/ingrediente_eliminar.html"
    model = Ingrediente
    success_url = reverse_lazy("ingredientes_lista")


class IngredienteNuevoView(SuccessMessageMixin, CreateView):
    template_name = "app/ingrediente_nuevo.html"
    model = Ingrediente
    form_class = IngredienteForm
    success_url = reverse_lazy("ingredientes_lista")
    success_message = "Guardado correctamente"


def relaciones(request):
    recetas = Receta.objects.all()
    ingredientes = Ingrediente.objects.all()
    return render(
        request,
        "app/relaciones.html",
        {"recetas": recetas, "ingredientes": ingredientes},
    )


def receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    ingredientes = Ingrediente.objects.exclude(recetas=receta)
    formulario = IngredienteRecetaForm(request.POST)
    formulario.fields["ingrediente"].queryset = ingredientes
    ingrediente_receta = IngredienteReceta.objects.filter(receta=receta)

    if request.method == "POST":
        ingrediente_receta = formulario.save(commit=False)
        ingrediente_receta.receta = receta
        ingrediente_receta.save()
        return redirect("receta", pk=pk)
    else:
        formulario = IngredienteRecetaForm()

    formulario.fields["ingrediente"].queryset = ingredientes
    contexto = {
        "receta": receta,
        "ingredientes": ingredientes,
        "ingrediente_receta": ingrediente_receta,
        "formulario": formulario,
    }
    return render(request, "app/receta.html", contexto)
