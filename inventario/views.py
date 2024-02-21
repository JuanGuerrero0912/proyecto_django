from django.shortcuts import render, redirect
from inventario.forms import ArticulosForm
from django.views.generic import View
from django.contrib import messages
from inventario.models import Articulos

# Create your views here.

class registrar_articulo(View):
    
    def get(self, request):
        
        formulario = ArticulosForm()

        return render(request, 'crud_articulos/registrar_articulo.html', {"formulario": formulario})
    
    def post(self, request):

        formulario = ArticulosForm(request.POST)
        
        if formulario.is_valid():

            formulario.save()
            messages.success(request, "Articulo agregado correctamente")
            return redirect('Lista_articulos')
        
        else:
            for msj in formulario.error_messages:
                messages.error(request, formulario.error_messages[msj])
            
            return render(request, 'crud_articulos/registrar_articulo.html', {"formulario": formulario})

class actualizar_articulo(View):

    def get(self, request, id):

        articulo = Articulos.objects.get(id = id)
        formulario = ArticulosForm(instance=articulo)

        return render(request, 'crud_articulos/editar_articulo.html', {"formulario": formulario})
    
    def post(self, request, id):

        articulo = Articulos.objects.get(id = id)
        formulario = ArticulosForm(request.POST, instance=articulo)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Articulo actualizado correctamente")
            return redirect('Lista_articulos')
        
        else:
            for msj in formulario.error_messages:
                messages.error(request, formulario.error_messages[msj])
            
            return render(request, 'crud_articulos/editar_articulo.html', {"formulario": formulario})

def inhabilitar_articulo(request, id):

    articulo = Articulos.objects.get(id = id)
    articulo.estado_articulo = 2
    articulo.save()
    messages.success(request,"Articulo inhabilitado correctamente")
    return redirect('Lista_articulos')

        

    