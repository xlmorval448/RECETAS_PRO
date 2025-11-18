from django.shortcuts import render
from .models import Ingrediente

# Create your views here.
def inicio(request):
    return render(request, 'app/inicio.html')

def ingredientes_lista(request):
    ingredientes = Ingrediente.objects.all('app/ingredientes_lista.html')
    
    return render (request)