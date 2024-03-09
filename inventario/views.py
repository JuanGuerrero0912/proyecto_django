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

        usuario = self.request.user
        formulario = ArticulosForm(request.POST, request.FILES)
        
        if formulario.is_valid():

            articulo = formulario.save(commit=False)
            articulo.usuario = usuario
            articulo.save()
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
        usuario = self.request.user

        if formulario.is_valid():
            articulo = formulario.save(commit=False)
            articulo.usuario = usuario
            articulo.save()
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
        usuario = self.request.user

        if formulario.is_valid():

            entrada = formulario.save(commit=False)
            entrada.administrador = usuario
            entrada.save()
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
        usuario = self.request.user

        if formulario.is_valid():
            entrada = formulario.save(commit=False)
            entrada.administrador = usuario
            entrada.save()
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
        usuario = self.request.user
        art = request.POST.get("articulo")
        cant = request.POST.get("cantidad_salida")
        cant = int(cant)

        if formulario.is_valid():

            articulo = Articulos.objects.get(id = art)
            stock = articulo.get_stock
            if stock >= cant:
                salida = formulario.save(commit=False)
                salida.administrativo = usuario
                salida.save()
                messages.success(request, "Salida agregada correctamente")
                return redirect('Lista_salidas')
            else:
                messages.error(request, f"La cantidad de salida es mayor al stock existente. Quedan {stock} unidades de  {articulo.nombre} ")

                return render(request, 'crud_salidas/registrar_salida.html', {"formulario": formulario})
        
        else:
            
            messages.error(request, "La salida no se pudo registrar")

            return render(request, 'crud_salidas/registrar_salida.html', {"formulario": formulario})

class actualizar_salida(View):

    def get(self, request, id):

        salida = Salidas.objects.get(id = id)
        formulario = SalidasForm(instance=salida)

        return render(request, 'crud_salidas/editar_salida.html', {"formulario": formulario})
    
    def post(self, request, id):

        salida = Salidas.objects.get(id = id)
        cant_ant = salida.cantidad_salida
        formulario = SalidasForm(request.POST,instance=salida)
        usuario = self.request.user
        art = request.POST.get("articulo")
        cant = request.POST.get("cantidad_salida")
        cant = int(cant)

        if formulario.is_valid():

            articulo = Articulos.objects.get(id = art)
            stock = articulo.get_stock
            stock_nue = stock + cant_ant
            if stock_nue >= cant:
                salida = formulario.save(commit=False)
                salida.administrativo = usuario
                salida.save()
                messages.success(request, "Salida actualizada correctamente")
                return redirect('Lista_salidas')
            else:
                messages.error(request, f"La cantidad de salida es mayor al stock existente. Quieres actualizar la cantidad que estava en {cant_ant} por {cant}, y solo quedan {stock} existencias")

                return render(request, 'crud_salidas/editar_salida.html', {"formulario": formulario})
        
        else:
            messages.error(request, "La salida no se pudo actualizar")

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
    cant = salida.cantidad_salida
    art = salida.articulo.id
    articulo = Articulos.objects.get(id = art)
    stock = articulo.get_stock
    if stock >= cant:
        salida.save()
        messages.success(request, "Salida habilitada correctamente")
        return redirect('Lista_salidas_Inhabilitadas')
    else:
        messages.error(request, f"No se puede habilitar esta salida, ya que la cantidad de la salida es de {cant} y la cantidad de existencias es de {stock}")
        return redirect('Lista_salidas_Inhabilitadas')

#-------------------------------------------------------------------------------------

        #VETERINARIO: 

class registrar_salida_veter(View):

    def get(self, request):

        formulario = SalidasForm()

        return render(request, 'salidas_veterinario/registrar_salida_veter.html', {"formulario": formulario})

    def post(self, request):

        formulario = SalidasForm(request.POST)
        usuario = self.request.user
        art = request.POST.get("articulo")
        cant = request.POST.get("cantidad_salida")
        cant = int(cant)

        if formulario.is_valid():
            articulo = Articulos.objects.get(id = art)
            stock = articulo.get_stock
            if stock >= cant:
                salida = formulario.save(commit=False)
                salida.administrativo = usuario
                salida.save()
                messages.success(request, "Salida agregada correctamente")
                return redirect('Salidas_veterinario')
            
            else:
                messages.error(request, f"La cantidad de salida es mayor al stock existente. Quedan {stock} unidades de  {articulo.nombre} ")

                return render(request, 'salidas_veterinario/registrar_salida_veter.html', {"formulario": formulario})
            
        else:
            messages.error(request, "La salida no se pudo registrar")

            return render(request, 'salidas_veterinario/registrar_salida_veter.html', {"formulario": formulario})
        
def ver_salida_veter(request, id):
    salida = Salidas.objects.get(id = id)
    formulario = SalidasForm(instance=salida)

    return render(request, 'salidas_veterinario/ver_salida_veter.html', {"formulario": formulario})

class actualizar_salida_veter(View):

    def get(self, request, id):

        salida = Salidas.objects.get(id = id)
        formulario = SalidasForm(instance=salida)

        return render(request, 'salidas_veterinario/editar_salida_veter.html', {"formulario": formulario})
    
    def post(self, request, id):

        salida = Salidas.objects.get(id = id)
        cant_ant = salida.cantidad_salida
        formulario = SalidasForm(request.POST,instance=salida)
        usuario = self.request.user
        art = request.POST.get("articulo")
        cant = request.POST.get("cantidad_salida")
        cant = int(cant)

        if formulario.is_valid():
            articulo = Articulos.objects.get(id = art)
            stock = articulo.get_stock
            stock_nue = stock + cant_ant
            if stock_nue >= cant:
                salida = formulario.save(commit=False)
                salida.administrativo = usuario
                salida.save()
                messages.success(request, "Salida actualizada correctamente")
                return redirect('Salidas_veterinario')
            
            else:
                messages.error(request, f"La cantidad de salida es mayor al stock existente. Quieres actualizar la cantidad que estava en {cant_ant} por {cant}, y solo quedan {stock} existencias")

                return render(request, 'salidas_veterinario/editar_salida_veter.html', {"formulario": formulario})
        else:
            messages.error(request, "La salida no se pudo actualizar")

            return render(request, 'salidas_veterinario/editar_salida_veter.html', {"formulario": formulario})