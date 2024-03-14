from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from donaciones.models import Donaciones
from donaciones.forms import DonacionForms
from inventario.models import Articulos

# Create your views here.

class registrar_donacion(View):

    def get(self, request):

        formulario = DonacionForms()
        return render(request, 'crud_donaciones/registrar_donacion.html', {"formulario": formulario})
    
    def post(self, request):

        formulario = DonacionForms(request.POST)

        if formulario.is_valid():

            formulario.save()
            messages.success(request, "Donación agregada correctamente")
            return redirect('Lista_donaciones')
        
        else:
            
            messages.error(request, "Ocurrio un error al registrar la salida, intentalo de nuevo")
            
            return render(request, 'crud_donaciones/registrar_donacion.html', {"formulario": formulario})

class actualizar_donacion(View):

    def get(self, request, id):

        donacion = Donaciones.objects.get(id = id)
        formulario = DonacionForms(instance=donacion)

        return render(request, 'crud_donaciones/editar_donacion.html', {"formulario": formulario})
    
    def post(self, request, id):

        donacion = Donaciones.objects.get(id = id)
        formulario = DonacionForms(request.POST,instance=donacion)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Donación actualizada correctamente")
            return redirect('Lista_donaciones')
        
        else:
            for msj in formulario.error_messages:
                messages.error(request, formulario.error_messages[msj])
            
            return render(request, 'crud_donaciones/editar_donacion.html', {"formulario": formulario})
        
def inhabilitar_donacion(request, id):

    articulo = Donaciones.objects.get(id = id)
    articulo.estado_donacion = 2
    articulo.save()
    messages.success(request,"Donación inhabilitada correctamente")
    return redirect('Lista_donaciones')

def ver_donacion(request, id):

    donacion = Donaciones.objects.get(id = id)
    formulario = DonacionForms(instance=donacion)

    return render(request, 'crud_donaciones/ver_donacion.html', {"formulario": formulario})

def lista_donaciones_inhabilitadas(request):

    donaciones = Donaciones.objects.filter(estado_donacion = 2)
    return render(request, "crud_donaciones/lista_donaciones_inhabilitadas.html", {'donaciones': donaciones})

def habilitar_donacion(request, id):

    donacion = Donaciones.objects.get(id = id)
    donacion.estado_donacion = 1
    donacion.save()
    messages.success(request,"Donación habilitada correctamente")
    return redirect('Lista_donaciones_Inhabilitadas')

class mis_donaciones(View):

    def get(self, request):

        usuario = self.request.user
        donaciones = Donaciones.objects.filter(usuario = usuario)

        return render(request, "donaciones_adop/listado_donaciones_adop.html", {"donaciones": donaciones})

class mas_información(View):

    def get(self, request):

        articulos = Articulos.objects.filter(estado_articulo = 1)

        return render(request, "donaciones_adop/información_donacion_adop.html", {"articulos": articulos})