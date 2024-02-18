from django.shortcuts import render, redirect
from inventario.models import Articulos

# Create your views here.

def registrar_articulo(request):
    
    
    
    return render(request, 'crud_articulos/registrar_articulo.html')