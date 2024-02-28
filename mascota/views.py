from django.shortcuts import render, redirect
from mascota.forms import MascotaForm, AdopcionForm, HistorialMedicoForm, SolicitudAdopcionForm, SeguimientoAdopcionForm
from django.views.generic import View
from django.contrib import messages
from mascota.models import Mascota, Adopcion, HistorialMedico, SolicitudAdopcion, SeguimientoAdopcion
from django.http import FileResponse
import os
from DoggyAtHome import settings


# PERRITO:
class registrar_mascota(View):
    
    def get(self, request):
        formulario = MascotaForm()
        return render(request, 'crud_mascotas/registrar_mascota.html', {"formulario": formulario})
    
    def post(self, request):
        formulario = MascotaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Mascota agregada correctamente")
            return redirect('Lista_mascotas')      
        else:
            for msj in formulario.error_messages:
                messages.error(request, formulario.error_messages[msj])           
            return render(request, 'crud_mascotas/registrar_mascota.html', {"formulario": formulario})
        
class actualizar_mascota(View):

    def get(self, request, id):

        mascota = Mascota.objects.get(id = id)
        formulario = MascotaForm(instance=mascota)
        return render(request, 'crud_mascotas/editar_mascota.html', {"formulario": formulario})
    
    def post(self, request, id):

        mascota = Mascota.objects.get(id = id)
        formulario = MascotaForm(request.POST, request.FILES, instance=mascota)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Mascota actualizada correctamente")
            return redirect('Lista_mascotas')
        
        else:
            for msj in formulario.error_messages:
                messages.error(request, formulario.error_messages[msj])
            
            return render(request, 'crud_mascotas/editar_mascota.html', {"formulario": formulario})
        
def inhabilitar_mascota(request, id):

    mascota = Mascota.objects.get(id = id)
    mascota.estadoRegistro= 2
    mascota.save()
    messages.success(request,"Mascota inhabilitada correctamente")
    return redirect('Lista_mascotas')

# ADOPCION:
class registrar_adopcion(View):
    
    def get(self, request):
        formulario = AdopcionForm()
        return render(request, 'crud_mascotas/registrar_adopcion.html', {"formulario": formulario})
    
    def post(self, request):
        formulario = AdopcionForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Adopción agregada correctamente")
            return redirect('Lista_adopciones')      
        else:
            for msj in formulario.error_messages:
                messages.error(request, formulario.error_messages[msj])           
            return render(request, 'crud_mascotas/registrar_adopcion.html', {"formulario": formulario})
        
class actualizar_adopcion(View):

    def get(self, request, id):

        adopcion = Adopcion.objects.get(id = id)
        formulario = AdopcionForm(instance=adopcion)
        return render(request, 'crud_mascotas/editar_adopcion.html', {"formulario": formulario})
    
    def post(self, request, id):

        adopcion = Adopcion.objects.get(id = id)
        formulario = AdopcionForm(request.POST, instance=adopcion)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Adopción actualizada correctamente")
            return redirect('Lista_adopciones')
        
        else:
            for msj in formulario.error_messages:
                messages.error(request, formulario.error_messages[msj])
            
            return render(request, 'crud_mascotas/editar_adopcion.html', {"formulario": formulario})
        
def inhabilitar_adopcion(request, id):

    adopcion = Adopcion.objects.get(id = id)
    adopcion.estado_adopcion= 2
    adopcion.save()
    messages.success(request,"Adopción inhabilitada correctamente")
    return redirect('Lista_adopciones')


# HISTORIAL MÉDICO:
class registrar_historial(View):
    
    def get(self, request):
        
        formulario = HistorialMedicoForm()
        return render(request, 'crud_mascotas/registrar_historial.html', {"formulario": formulario})
    
    def post(self, request):

        formulario = HistorialMedicoForm(request.POST, request.FILES)
        if formulario.is_valid():

            formulario.save()
            messages.success(request, "Historial agregado correctamente")
            return redirect('Lista_historial_medico')
        
        else:
            for msj in formulario.error_messages:
                messages.error(request, formulario.error_messages[msj])
            
            return render(request, 'crud_mascotas/registrar_historial.html', {"formulario": formulario})

class actualizar_historial(View):

    def get(self, request, id):

        historial = HistorialMedico.objects.get(id = id)
        formulario = HistorialMedicoForm(instance=historial)
        return render(request, 'crud_mascotas/editar_historial.html', {"formulario": formulario})
    
    def post(self, request, id):

        historial = HistorialMedico.objects.get(id = id)
        formulario = HistorialMedicoForm(request.POST, request.FILES, instance=historial)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Historial actualizado correctamente")
            return redirect('Lista_historial_medico')
        
        else:
            for msj in formulario.error_messages:
                messages.error(request, formulario.error_messages[msj])
            
            return render(request, 'crud_mascotas/editar_historial.html', {"formulario": formulario})

def inhabilitar_historial(request, id):
    historial = HistorialMedico.objects.get(id = id)
    historial.estado_historial= 2
    historial.save()
    messages.success(request,"Historial inhabilitado correctamente")
    return redirect('Lista_historial_medico')

#descarga archivos
from django.http import FileResponse
import os

def descargar_archivo(request, archivo_nombre):
    # Ruta absoluta al archivo que deseas descargar
    archivo_ruta = os.path.join(settings.MEDIA_ROOT, 'plantillas', archivo_nombre)
    # Abre el archivo y lo devuelve como una respuesta de archivo
    return FileResponse(open(archivo_ruta, 'rb'))


# SOLICITUD
class registrar_solicitud(View):
    
    def get(self, request):
        
        formulario = SolicitudAdopcionForm()
        return render(request, 'crud_mascotas/registrar_solicitud.html', {"formulario": formulario})
    
    def post(self, request):

        formulario = SolicitudAdopcionForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Solicitud agregada correctamente")
            return redirect('Lista_solicitudes_adopcion')
        
        else:
            for msj in formulario.error_messages:
                messages.error(request, formulario.error_messages[msj])
            
            return render(request, 'crud_mascotas/registrar_solicitud.html', {"formulario": formulario})

class actualizar_solicitud(View):

    def get(self, request, id):

        solicitud = SolicitudAdopcion.objects.get(id = id)
        formulario = SolicitudAdopcionForm(instance=solicitud)
        return render(request, 'crud_mascotas/editar_solicitud.html', {"formulario": formulario})
    
    def post(self, request, id):

        solicitud = SolicitudAdopcion.objects.get(id = id)
        formulario = SolicitudAdopcionForm(request.POST, request.FILES, instance=solicitud)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Solicitud actualizada correctamente")
            return redirect('Lista_solicitudes_adopcion')
        
        else:
            for msj in formulario.error_messages:
                messages.error(request, formulario.error_messages[msj])
            
            return render(request, 'crud_mascotas/editar_solicitud.html', {"formulario": formulario})

def inhabilitar_solicitud(request, id):
    solicitud = SolicitudAdopcion.objects.get(id = id)
    solicitud.estado_solicitud= 2
    solicitud.save()
    messages.success(request,"Solicitud inhabilitada correctamente")
    return redirect('Lista_solicitudes_adopcion')

#SEGUIMIENTO
class registrar_seguimiento(View):
    
    def get(self, request):
        
        formulario = SeguimientoAdopcionForm()
        return render(request, 'crud_mascotas/registrar_seguimiento.html', {"formulario": formulario})
    
    def post(self, request):

        formulario = SeguimientoAdopcionForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Seguimiento agregado correctamente")
            return redirect('Lista_seguimientos_proceso')
        
        else:
            for msj in formulario.error_messages:
                messages.error(request, formulario.error_messages[msj])
            
            return render(request, 'crud_mascotas/registrar_seguimiento.html', {"formulario": formulario})

class actualizar_seguimiento(View):

    def get(self, request, id):

        seguimiento = SeguimientoAdopcion.objects.get(id = id)
        formulario = SeguimientoAdopcionForm(instance=seguimiento)
        return render(request, 'crud_mascotas/editar_seguimiento.html', {"formulario": formulario})
    
    def post(self, request, id):

        seguimiento = SeguimientoAdopcion.objects.get(id = id)
        formulario = SeguimientoAdopcionForm(request.POST, request.FILES, instance=seguimiento)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Seguimiento actualizado correctamente")
            return redirect('Lista_seguimientos_proceso')
        
        else:
            for msj in formulario.error_messages:
                messages.error(request, formulario.error_messages[msj])
            
            return render(request, 'crud_mascotas/editar_seguimiento.html', {"formulario": formulario})

def inhabilitar_seguimiento(request, id):
    seguimiento = SeguimientoAdopcion.objects.get(id = id)
    seguimiento.estado_seguimiento= 2
    seguimiento.save()
    messages.success(request,"Seguimiento inhabilitado correctamente")
    return redirect('Lista_seguimientos_proceso')


def historiales_medicos_por_perrito(request, id):

    historial = HistorialMedico.objects.filter(
        mascota = id
    )
    return render(request, "crud_mascotas/historial_por_perrito.html", {"historial": historial})

def seguimiento_por_perrito(request, id):

    solicitud_adopcion = SolicitudAdopcion.objects.filter(
        mascota = id
    )

    return render(request, "crud_mascotas/seguimiento_por_perrito.html", {"solicitud_adopcion": solicitud_adopcion})