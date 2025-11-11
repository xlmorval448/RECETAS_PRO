from django.shortcuts import render, get_object_or_404
from .models import Post, Autor

# Create your views here.
def inicio(request):
    entradas = Post.objects.all()
    contexto = {'entradas': entradas}
    return render(request,'blog/inicio.html',contexto )

def detalle_post(request, pk):
    entrada = Post.objects.get(pk=pk)
    contexto = {'entrada': entrada}
    return render(request,'blog/detalle_post.html', contexto)

def post_autor(request, autor_pk):
    entrada = Post.objects.filter(autor=autor_pk)
    autor = get_object_or_404(Autor,pk = autor_pk )
    contexto = {'entrada': entrada, 'autor':autor}
    return render(request,'blog/post_autor.html', contexto)

def autores(request):
    autores = Autor.objects.all()
    contexto = {'autores': autores}
    return render(request, 'blog/autores.html', contexto)