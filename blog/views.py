from django.shortcuts import redirect, render, get_object_or_404
from .models import Post, Autor
from .forms import Autorform

# Create your views here.
def inicio(request):
    entradas = Post.objects.all()
    contexto = {"entradas": entradas}
    return render(request, "blog/inicio.html", contexto)

def autor_nuevo(request):
    if request.method == "POST":
        print(request.POST)
        form = Autorform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("autores")
    else:
        form = Autorform()

    return render(request, "blog/autor_nuevo.html", {"form": form})

def autor_editar(request, pk):

    autor = get_object_or_404(Autor, pk=pk)

    if request.method == "POST":
        print(request.POST)
        form = Autorform(request.POST, instance=autor)
        if form.is_valid():

            form.save()
            return redirect("autores")
    else:
        form = Autorform(instance=autor)

    return render(request, "blog/autor_nuevo.html", {"form": form})

def autor_eliminar(request_pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect("autores")
    else:
        return render(request, 'blog/autor_eliminar', {'autor':autor})

def detalle_post(request, pk):
    entrada = Post.objects.get(pk=pk)
    contexto = {"entrada": entrada}
    return render(request, "blog/detalle_post.html", contexto)

def post_autor(request, autor_pk):
    entrada = Post.objects.filter(autor=autor_pk)
    autor = get_object_or_404(Autor, pk=autor_pk)
    contexto = {"entrada": entrada, "autor": autor}
    return render(request, "blog/autor_post.html", contexto)

def autores(request):
    autores = Autor.objects.all()
    contexto = {"autores": autores}
    return render(request, "blog/autores.html", contexto)
