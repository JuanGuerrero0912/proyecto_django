from django.shortcuts import render, redirect
from inventario.forms import ArticulosForm, EntradasForm, SalidasForm
from django.views.generic import View
from django.contrib import messages
from inventario.models import Articulos, Entradas, Salidas

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

def ver_articulo(request, id):
    articulo = Articulos.objects.get(id = id)
    formulario = ArticulosForm(instance=articulo)

    return render(request, 'crud_articulos/ver_articulo.html', {"formulario": formulario})

def lista_articulos_inhabilitados(request):

    articulos = Articulos.objects.filter(estado_articulo = 2)
    return render(request, 'crud_articulos/lista_articulos_inhabilitados.html', {"articulos": articulos})

def habilitar_articulo(request, id):
    articulo = Articulos.objects.get(id = id)
    articulo.estado_articulo = 1
    articulo.save()
    messages.success(request,"Articulo habilitado correctamente")
    return redirect('Lista_articulos_Inhabilitados')

        
class registrar_Entrada(View):

    def get(self, request):

        formulario = EntradasForm()

        return render(request, "crud_entradas/registrar_entrada.html", {"formulario": formulario})
    
    def post(self, request):

        formulario = EntradasForm(request.POST)

        if formulario.is_valid():

            formulario.save()
            messages.success(request, "Entrada agregada correctamente")
            return redirect('Lista_entradas')
        
        else:
            for msj in formulario.error_messages:
                messages.error(request, formulario.error_messages[msj])
            
            return render(request, 'crud_entradas/registrar_entrada.html', {"formulario": formulario})


class actualizar_entrada(View):

    def get(self, request, id):

        entrada = Entradas.objects.get(id = id)
        formulario = EntradasForm(instance=entrada)

        return render(request, 'crud_entradas/editar_entrada.html', {"formulario": formulario})

    def post(self,  request, id):

        entrada = Entradas.objects.get(id=id)
        formulario = EntradasForm(request.POST , instance=entrada)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Entrada actualizada correctamente")
            return redirect('Lista_entradas')
        
        else:
            for msj in formulario.error_messages:
                messages.error(request, formulario.error_messages[msj])
            
            return render(request, 'crud_entradas/registrar_entrada.html', {"formulario": formulario})

def inhabilitar_entrada(request, id):

    entrada = Entradas.objects.get(id = id)
    entrada.estado_entrada = 2
    entrada.save()
    messages.success(request, "Entrada inhabilitada correctamente")
    return redirect('Lista_entradas')

def Lista_entradas_inhabilitadas(request):

    entradas = Entradas.objects.filter(estado_entrada = 2) 

    return render(request, "crud_entradas/lista_entradas_inhabilitadas.html", {'entradas': entradas})

def habilitar_entrada(request, id):
    entrada = Entradas.objects.get(id = id)
    entrada.estado_entrada = 1
    entrada.save()
    messages.success(request, "Entrada habilitada correctamente")
    return redirect('Lista_entradas_Inhabilitadas')

def ver_entrada(request, id):
    entrada = Entradas.objects.get(id = id)
    formulario = EntradasForm(instance=entrada)

    return render(request, 'crud_entradas/ver_entrada.html', {"formulario": formulario})

class registrar_salida(View):

    def get(self, request):

        formulario = SalidasForm()

        return render(request, 'crud_salidas/registrar_salida.html', {"formulario": formulario})

    def post(self, request):

        formulario = SalidasForm(request.POST)

        if formulario.is_valid():

            formulario.save()
            messages.success(request, "Salida agregada correctamente")
            return redirect('Lista_salidas')
        
        else:
            for msj in formulario.error_messages:
                messages.error(request, formulario.error_messages[msj])

            return render(request, 'crud_salidas/registrar_salida.html', {"formulario": formulario})

class actualizar_salida(View):

    def get(self, request, id):

        salida = Salidas.objects.get(id = id)
        formulario = SalidasForm(instance=salida)

        return render(request, 'crud_salidas/editar_salida.html', {"formulario": formulario})
    
    def post(self, request, id):

        salida = Salidas.objects.get(id = id)
        formulario = SalidasForm(request.POST,instance=salida)

        if formulario.is_valid():

            formulario.save()
            messages.success(request, "Salida actualizada correctamente")
            return redirect('Lista_salidas')
        
        else:
            for msj in formulario.error_messages:
                messages.error(request, formulario.error_messages[msj])

            return render(request, 'crud_salidas/editar_salida.html', {"formulario": formulario})

def inhabilitar_salida(request, id):

    salida = Salidas.objects.get(id = id)
    salida.estado_salida = 2
    salida.save()
    messages.success(request, "Salida inhabilitada correctamente")
    return redirect('Lista_salidas')

def ver_salida(request, id):
    salida = Salidas.objects.get(id = id)
    formulario = SalidasForm(instance=salida)

    return render(request, 'crud_salidas/ver_salida.html', {"formulario": formulario})

def lista_salidas_inhabilitadas(request):
    salidas = Salidas.objects.filter(estado_salida = 2)
    return render(request, 'crud_salidas/lista_salidas_inhabilitadas.html', {"salidas": salidas})

def habilitar_salida(request, id):

    salida = Salidas.objects.get(id = id)
    salida.estado_salida = 1
    salida.save()
    messages.success(request, "Salida habilitada correctamente")
    return redirect('Lista_salidas_Inhabilitadas')