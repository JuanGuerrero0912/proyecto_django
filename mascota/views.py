from django.shortcuts import render, redirect
from mascota.forms import MascotaForm, AdopcionForm, HistorialMedicoForm, SolicitudAdopcionForm, SeguimientoAdopcionForm, SolicitudAdoptanteForm, Historial_medico_por_mascota
from django.views.generic import View
from django.contrib import messages
from mascota.models import Mascota, Adopcion, HistorialMedico, SolicitudAdopcion, SeguimientoAdopcion
from django.http import FileResponse
import os
from DoggyAtHome import settings
from login.models import Perfil
from django.core.paginator import Paginator


def mostrar_video(request):
    video_url = '/media/videoAdoptante.mp4' 
    return render(request, 'paginas_adoptante/inicio_adoptante.html', {'video_url': video_url})
# PERRITO:
class registrar_mascota(View):
    
    def get(self, request):
        formulario = MascotaForm()
        return render(request, 'crud_mascotas/registrar_mascota.html', {"formulario": formulario})
    
    def post(self, request):
        formulario = MascotaForm(request.POST, request.FILES)
        usuario = self.request.user
        if formulario.is_valid():
            mascota = formulario.save(commit=False)
            mascota.administrativo = usuario
            mascota.save()
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
        usuario = self.request.user

        if formulario.is_valid():
            mascota = formulario.save(commit=False)
            mascota.administrativo = usuario
            mascota.save()
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

def ver_mascota(request, id):
    mascota = Mascota.objects.get(id = id)
    formulario = MascotaForm(instance=mascota)
    return render(request, 'crud_mascotas/ver_mascota.html', {"formulario": formulario})

def lista_mascotas_inhabilitadas(request):
    mascotas = Mascota.objects.filter(estadoRegistro = 2) 
    return render(request, "crud_mascotas/lista_mascotas_inhabilitadas.html", {'entity': mascotas})

def habilitar_mascota(request, id):
    mascota = Mascota.objects.get(id = id)
    mascota.estadoRegistro= 1
    mascota.save()
    messages.success(request,"Mascota habilitada correctamente")
    return redirect('Lista_mascotas_inhabilitadas')

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

def ver_adopcion(request, id):
    adopcion = Adopcion.objects.get(id = id)
    formulario = AdopcionForm(instance=adopcion)
    return render(request, 'crud_mascotas/ver_adopcion.html', {"formulario": formulario})

def lista_adopciones_inhabilitadas(request):
    adopcion = Adopcion.objects.filter(estado_adopcion = 2) 
    return render(request, "crud_mascotas/lista_adopciones_inhabilitadas.html", {'entity': adopcion})

def habilitar_adopcion(request, id):

    adopcion = Adopcion.objects.get(id = id)
    adopcion.estado_adopcion= 1
    adopcion.save()
    messages.success(request,"Adopción habilitada correctamente")
    return redirect('Lista_adopciones_inhabilitadas')

# HISTORIAL MÉDICO:
class registrar_historial(View):
    
    def get(self, request):
        
        formulario = HistorialMedicoForm()
        return render(request, 'crud_mascotas/registrar_historial.html', {"formulario": formulario})
    
    def post(self, request):

        formulario = HistorialMedicoForm(request.POST, request.FILES)
        usuario = self.request.user
        if formulario.is_valid():

            historial = formulario.save(commit=False)
            historial.veterinario = usuario
            historial.save()
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
        usuario = self.request.user

        if formulario.is_valid():
            historial = formulario.save(commit=False)
            historial.veterinario = usuario
            historial.save()
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

def ver_historial(request, id):
    historial = HistorialMedico.objects.get(id = id)
    formulario = HistorialMedicoForm(instance=historial)
    return render(request, 'crud_mascotas/ver_historial.html', {"formulario": formulario})

def descargar_archivo(request, archivo_nombre):
    archivo_ruta = os.path.join(settings.MEDIA_ROOT, 'plantillas', archivo_nombre)
    return FileResponse(open(archivo_ruta, 'rb'))

def lista_historiales_inhabilitadas(request):
    historial = HistorialMedico.objects.filter(estado_historial = 2) 
    return render(request, "crud_mascotas/lista_historiales_inhabilitadas.html", {'entity': historial})

def habilitar_historial(request, id):
    historial = HistorialMedico.objects.get(id = id)
    historial.estado_historial= 1
    historial.save()
    messages.success(request,"Historial habilitado correctamente")
    return redirect('Lista_historiales_inhabilitadas')

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

def ver_solicitud(request, id):
    solicitud = SolicitudAdopcion.objects.get(id = id)
    formulario = SolicitudAdopcionForm(instance=solicitud)
    return render(request, 'crud_mascotas/ver_solicitud.html', {"formulario": formulario})

def lista_solicitudes_inhabilitadas(request):
    solicitud = SolicitudAdopcion.objects.filter(estado_solicitud = 2) 
    return render(request, "crud_mascotas/lista_solicitudes_inhabilitadas.html", {'entity': solicitud})

def habilitar_solicitud(request, id):
    solicitud = SolicitudAdopcion.objects.get(id = id)
    solicitud.estado_solicitud= 1
    solicitud.save()
    messages.success(request,"Solicitud habilitada correctamente")
    return redirect('Lista_solicitudes_inhabilitadas')

#SEGUIMIENTO

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
            if seguimiento.fase == 4 and seguimiento.estado_fase == 1:
                
                id_mascota = seguimiento.solicitud_adopcion.mascota.id
                lista_adopciones = Adopcion.objects.filter(mascota = id_mascota).count()

                if lista_adopciones < 1:
                    adopcion = Adopcion(mascota = seguimiento.solicitud_adopcion.mascota, 
                                    adoptante = seguimiento.solicitud_adopcion.adoptante)
                    adopcion.save()
                    mascota = Mascota.objects.get(id = id_mascota)
                    mascota.estadoMascota = 3
                    mascota.save()
                else:
                    id_mascota = seguimiento.solicitud_adopcion.mascota.id
                    lista_adopcion = Adopcion.objects.filter(mascota = id_mascota).count()
                    if lista_adopcion > 0:
                        adopcion = Adopcion.objects.get(mascota = id_mascota)
                        adopcion.estado_adopcion = 1
                        adopcion.save()
                        mascota = Mascota.objects.get(id = id_mascota)
                        mascota.estadoMascota = 3
                        mascota.save()
            if seguimiento.fase == 3:

                id_mascota = seguimiento.solicitud_adopcion.mascota.id
                lista_adopcion = Adopcion.objects.filter(mascota = id_mascota).count()
                if lista_adopcion > 0:
                    adopcion = Adopcion.objects.get(mascota = id_mascota)
                    adopcion.estado_adopcion = 2
                    adopcion.save()
                    mascota = Mascota.objects.get(id = id_mascota)
                    mascota.estadoMascota = 1
                    mascota.save()
            if seguimiento.fase == 2:

                id_mascota = seguimiento.solicitud_adopcion.mascota.id
                lista_adopcion = Adopcion.objects.filter(mascota = id_mascota).count()
                if lista_adopcion > 0:
                    adopcion = Adopcion.objects.get(mascota = id_mascota)
                    adopcion.estado_adopcion = 2
                    adopcion.save()
                    mascota = Mascota.objects.get(id = id_mascota)
                    mascota.estadoMascota = 1
                    mascota.save()
            if seguimiento.fase == 1:
                id_mascota = seguimiento.solicitud_adopcion.mascota.id
                lista_adopcion = Adopcion.objects.filter(mascota = id_mascota).count()
                if lista_adopcion > 0:
                    adopcion = Adopcion.objects.get(mascota = id_mascota)
                    adopcion.estado_adopcion = 2
                    adopcion.save()
                    mascota = Mascota.objects.get(id = id_mascota)
                    mascota.estadoMascota = 1
                    mascota.save()
            if seguimiento.estado_fase == 2:
                id_mascota = seguimiento.solicitud_adopcion.mascota.id
                lista_adopcion = Adopcion.objects.filter(mascota = id_mascota).count()
                if lista_adopcion > 0:
                    adopcion = Adopcion.objects.get(mascota = id_mascota)
                    adopcion.estado_adopcion = 2
                    adopcion.save()
                    mascota = Mascota.objects.get(id = id_mascota)
                    mascota.estadoMascota = 1
                    mascota.save()
            if seguimiento.estado_fase == 3:
                id_mascota = seguimiento.solicitud_adopcion.mascota.id
                lista_adopcion = Adopcion.objects.filter(mascota = id_mascota).count()
                if lista_adopcion > 0:
                    adopcion = Adopcion.objects.get(mascota = id_mascota)
                    adopcion.estado_adopcion = 2
                    adopcion.save()
                    mascota = Mascota.objects.get(id = id_mascota)
                    mascota.estadoMascota = 1
                    mascota.save()
            
                
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

def ver_seguimiento(request, id):
    seguimiento = SeguimientoAdopcion.objects.get(id = id)
    formulario = SeguimientoAdopcionForm(instance=seguimiento)
    return render(request, 'crud_mascotas/ver_seguimiento.html', {"formulario": formulario})

def lista_seguimientos_inhabilitados(request):
    seguimiento = SeguimientoAdopcion.objects.filter(estado_seguimiento = 2) 
    return render(request, "crud_mascotas/lista_seguimientos_inhabilitados.html", {'entity': seguimiento})

def habilitar_seguimiento(request, id):
    seguimiento = SeguimientoAdopcion.objects.get(id = id)
    seguimiento.estado_seguimiento= 1
    seguimiento.save()
    messages.success(request,"Seguimiento habilitado correctamente")
    return redirect('Lista_seguimientos_inhabilitados')

def historiales_medicos_por_perrito(request, id):

    historial = HistorialMedico.objects.filter(mascota = id)
    mascota = Mascota.objects.get(id = id)
    return render(request, "crud_mascotas/historial_por_perrito.html", {"historial": historial, "mascota": mascota})

class registrar_historial_medico_por_perrito(View):
    
    def get(self, request, id):
        
        formulario = Historial_medico_por_mascota()
        mascota = Mascota.objects.get(id = id)
        return render(request, 'crud_mascotas/registrar_historial_por_mascota.html', {"formulario": formulario, "mascota": mascota})
    
    def post(self, request, id):

        formulario = Historial_medico_por_mascota(request.POST, request.FILES)
        usuario = self.request.user
        mascota = Mascota.objects.get(id = id)
        if formulario.is_valid():

            historial = formulario.save(commit=False)
            historial.veterinario = usuario
            historial.mascota = mascota
            historial.save()
            messages.success(request, "Historial agregado correctamente")
            return redirect('Historial_Por_Mascota', id = mascota.id)
        
        else:
            for msj in formulario.error_messages:
                messages.error(request, formulario.error_messages[msj])
            
            return render(request, 'crud_mascotas/registrar_historial_por_mascota.html', {"formulario": formulario})

class actualizar_historial_por_mascota(View):

    def get(self, request, id, id_historial):

        historial = HistorialMedico.objects.get(id = id_historial)
        formulario = HistorialMedicoForm(instance=historial)
        mascota = Mascota.objects.get(id = id)
        return render(request, 'crud_mascotas/editar_historial_por_mascota.html', {"formulario": formulario, "mascota": mascota})
    
    def post(self, request, id ,id_historial):

        historial = HistorialMedico.objects.get(id = id_historial)
        formulario = HistorialMedicoForm(request.POST, request.FILES, instance=historial)
        usuario = self.request.user
        mascota = Mascota.objects.get(id = id)

        if formulario.is_valid():
            historial = formulario.save(commit=False)
            historial.veterinario = usuario
            historial.mascota = mascota
            historial.save()
            messages.success(request, "Historial actualizado correctamente")
            return redirect('Historial_Por_Mascota', id = mascota.id)
        
        else:
            for msj in formulario.error_messages:
                messages.error(request, formulario.error_messages[msj])
            
            return render(request, 'crud_mascotas/editar_historial_por_mascota.html', {"formulario": formulario})

def ver_historial_por_mascota(request, id, id_historial):

    historial = HistorialMedico.objects.get(id = id_historial)
    formulario = HistorialMedicoForm(instance=historial)
    mascota = Mascota.objects.get(id = id)
    return render(request, 'crud_mascotas/ver_historial_por_mascota.html', {"formulario": formulario, "mascota": mascota})

def inhabilitar_historial_por_mascota(request, id):
    historial = HistorialMedico.objects.get(id = id)
    id_mascota = historial.mascota.id
    mascota = Mascota.objects.get(id = id_mascota)
    historial.estado_historial= 2
    historial.save()
    messages.success(request,"Historial inhabilitado correctamente")
    return redirect('Historial_Por_Mascota', id = mascota.id)

def lista_historiales_inhabilitadas_por_mascota(request, id):
    historial = HistorialMedico.objects.filter(estado_historial = 2)
    perrito = Mascota.objects.get(id = id)
    return render(request, "crud_mascotas/lista_historiales_inhabilitados_por_mascota.html", {'entity': historial, "perrito": perrito})

def habilitar_historial_por_mascota(request, id):
    historial = HistorialMedico.objects.get(id = id)
    id_mascota = historial.mascota.id
    mascota = Mascota.objects.get(id = id_mascota)
    historial.estado_historial= 1
    historial.save()
    messages.success(request,"Historial inhabilitado correctamente")
    return redirect('Lista_historiales_inhabilitados_por_mascota', id = mascota.id)



def seguimiento_por_perrito(request, id):
    peticion = SeguimientoAdopcion.objects.filter(solicitud_adopcion__mascota = id)
    mascota = Mascota.objects.get(id=id)
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(peticion, 3)
        peticion = paginator.page(page)
    except:
        pass

    return render(request, "crud_mascotas/seguimiento_por_perrito.html", {"entity": peticion, "mascota": mascota, "paginator": paginator})


        # VETERINARIO
def ver_adopcion_vete(request, id):
    adopcion = Adopcion.objects.get(id = id)
    formulario = AdopcionForm(instance=adopcion)
    return render(request, 'crud_mascotas_vet/ver_adopcion_vete.html', {"formulario": formulario})

def adopcion_inhabilitada_vete(request):
    adopcion = Adopcion.objects.filter(estado_adopcion = 2) 
    return render(request, "crud_mascotas_vet/adopcion_inhabilitada_vete.html", {'entity': adopcion})

class registrar_mascota_vete(View):
    
    def get(self, request):

        formulario = MascotaForm()
        return render(request, 'crud_mascotas_vet/registrar_mascota.html', {"formulario": formulario})
    
    def post(self, request):
        formulario = MascotaForm(request.POST, request.FILES)
        usuario = self.request.user
        if formulario.is_valid():
            mascota = formulario.save(commit=False)
            mascota.administrativo = usuario
            mascota.save()
            messages.success(request, "Mascota agregada correctamente")
            return redirect('Lista_mascotas_vete')      
        else:
            for msj in formulario.error_messages:
                messages.error(request, formulario.error_messages[msj])           
            return render(request, 'crud_mascotas_vet/registrar_mascota.html', {"formulario": formulario})
        
class actualizar_mascota_vete(View):

    def get(self, request, id):

        mascota = Mascota.objects.get(id = id)
        formulario = MascotaForm(instance=mascota)
        return render(request, 'crud_mascotas_vet/editar_mascota.html', {"formulario": formulario})
    
    def post(self, request, id):

        mascota = Mascota.objects.get(id = id)
        formulario = MascotaForm(request.POST, request.FILES, instance=mascota)
        usuario = self.request.user

        if formulario.is_valid():
            mascota = formulario.save(commit=False)
            mascota.administrativo = usuario
            mascota.save()
            messages.success(request, "Mascota actualizada correctamente")
            return redirect('Lista_mascotas_vete')
        
        else:
            for msj in formulario.error_messages:
                messages.error(request, formulario.error_messages[msj])
            
            return render(request, 'crud_mascotas_vet/editar_mascota.html', {"formulario": formulario})
        
def inhabilitar_mascota_vet(request, id):
    mascota = Mascota.objects.get(id = id)
    mascota.estadoRegistro= 2
    mascota.save()
    messages.success(request,"Mascota inhabilitada correctamente")
    return redirect('Lista_mascotas_vete')

def ver_mascota_vet(request, id):
    mascota = Mascota.objects.get(id = id)
    formulario = MascotaForm(instance=mascota)
    return render(request, 'crud_mascotas_vet/ver_mascota.html', {"formulario": formulario})

def lista_mascotas_inhabilitadas_vet(request):
    mascotas = Mascota.objects.filter(estadoRegistro = 2) 
    return render(request, "crud_mascotas_vet/lista_mascotas_inhabilitadas.html", {'entity': mascotas})

def habilitar_mascota_vet(request, id):
    mascota = Mascota.objects.get(id = id)
    mascota.estadoRegistro= 1
    mascota.save()
    messages.success(request,"Mascota habilitada correctamente")
    return redirect('Lista_mascotas_inhabilitadas_vet')


class registrar_historial_vete(View):
    
    def get(self, request):
        formulario = HistorialMedicoForm()
        return render(request, 'crud_mascotas_vet/registrar_historial.html', {"formulario": formulario})
    
    def post(self, request):

        formulario = HistorialMedicoForm(request.POST, request.FILES)
        usuario = self.request.user
            
        if formulario.is_valid():
            historial = formulario.save(commit=False)
            historial.veterinario = usuario
            historial.save()
            messages.success(request, "Historial agregado correctamente")
            return redirect('Lista_historial_vete')
        
        else:
            for msj in formulario.error_messages:
                messages.error(request, formulario.error_messages[msj])
            
            return render(request, 'crud_mascotas_vet/registrar_historial.html', {"formulario": formulario})

class actualizar_historial_vete(View):

    def get(self, request, id):

        historial = HistorialMedico.objects.get(id = id)
        formulario = HistorialMedicoForm(instance=historial)
        return render(request, 'crud_mascotas_vet/editar_historial.html', {"formulario": formulario})
    
    def post(self, request, id):

        historial = HistorialMedico.objects.get(id = id)
        formulario = HistorialMedicoForm(request.POST, request.FILES, instance=historial)
        usuario = self.request.user

        if formulario.is_valid():
            historial = formulario.save(commit=False)
            historial.veterinario = usuario
            historial.save()
            messages.success(request, "Historial actualizado correctamente")
            return redirect('Lista_historial_vete')
        
        else:
            for msj in formulario.error_messages:
                messages.error(request, formulario.error_messages[msj])
            
            return render(request, 'crud_mascotas_vet/editar_historial.html', {"formulario": formulario})

def inhabilitar_historial_vete(request, id):
    historial = HistorialMedico.objects.get(id = id)
    historial.estado_historial= 2
    historial.save()
    messages.success(request,"Historial inhabilitado correctamente")
    return redirect('Lista_historial_vete')

def ver_historial_vete(request, id):
    historial = HistorialMedico.objects.get(id = id)
    formulario = HistorialMedicoForm(instance=historial)
    return render(request, 'crud_mascotas_vet/ver_historial.html', {"formulario": formulario})


def lista_historial_inhabilitado_vet(request):
    historial = HistorialMedico.objects.filter(estado_historial = 2) 
    return render(request, "crud_mascotas_vet/lista_historial_inhabilitado.html", {'entity': historial})

def habilitar_historial_vete(request, id):
    historial = HistorialMedico.objects.get(id = id)
    historial.estado_historial= 1
    historial.save()
    messages.success(request,"Historial habilitado correctamente")
    return redirect('Lista_historial_inhabilitado_vet')

def historiales_medicos_por_perrito_vet(request, id):

    historial = HistorialMedico.objects.filter(mascota = id)
    mascota = Mascota.objects.get(id = id)
    return render(request, "crud_mascotas_vet/historial_por_perrito_veterinario.html", {"historial": historial, "mascota": mascota})

class registrar_historial_medico_por_perrito_veter(View):
    
    def get(self, request, id):
        
        formulario = Historial_medico_por_mascota()
        mascota = Mascota.objects.get(id = id)
        return render(request, 'crud_mascotas_vet/registrar_historial_por_mascota_veter.html', {"formulario": formulario, "mascota": mascota})
    
    def post(self, request, id):

        formulario = Historial_medico_por_mascota(request.POST, request.FILES)
        usuario = self.request.user
        mascota = Mascota.objects.get(id = id)
        if formulario.is_valid():

            historial = formulario.save(commit=False)
            historial.veterinario = usuario
            historial.mascota = mascota
            historial.save()
            messages.success(request, "Historial agregado correctamente")
            return redirect('historiales_medicos_por_perrito_vet', id = mascota.id)
        
        else:
            for msj in formulario.error_messages:
                messages.error(request, formulario.error_messages[msj])
            
            return render(request, 'crud_mascotas_vet/registrar_historial_por_mascota_veter.html', {"formulario": formulario})


class actualizar_historial_por_mascota_veter(View):

    def get(self, request, id, id_historial):

        historial = HistorialMedico.objects.get(id = id_historial)
        formulario = Historial_medico_por_mascota(instance = historial)
        mascota = Mascota.objects.get(id = id)
        return render(request, 'crud_mascotas_vet/editar_historial_por_mascota_veter.html', {"formulario": formulario, "mascota": mascota})
    
    def post(self, request, id, id_historial):

        historial = HistorialMedico.objects.get(id = id_historial)
        formulario = Historial_medico_por_mascota(request.POST, request.FILES ,instance = historial)
        usuario = self.request.user
        mascota = Mascota.objects.get(id = id)

        if formulario.is_valid():
            historial = formulario.save(commit=False)
            historial.veterinario = usuario
            historial.mascota = mascota
            historial.save()
            messages.success(request, "Historial actualizado correctamente")
            return redirect('historiales_medicos_por_perrito_vet', id = mascota.id)
        
        else:
            for msj in formulario.error_messages:
                messages.error(request, formulario.error_messages[msj])
            
            return render(request, 'crud_mascotas_vet/editar_historial_por_mascota_veter.html', {"formulario": formulario, "mascota": mascota})

def ver_historial_por_mascota_veter(request, id, id_historial):

    historial = HistorialMedico.objects.get(id = id_historial)
    formulario = Historial_medico_por_mascota(instance=historial)
    mascota = Mascota.objects.get(id = id)
    return render(request, 'crud_mascotas_vet/ver_historial_por_mascota_veter.html', {"formulario": formulario, "mascota": mascota})


def inhabilitar_historial_por_mascota_veter(request, id):
    historial = HistorialMedico.objects.get(id = id)
    id_mascota = historial.mascota.id
    mascota = Mascota.objects.get(id = id_mascota)
    historial.estado_historial= 2
    historial.save()
    messages.success(request,"Historial inhabilitado correctamente")
    return redirect('historiales_medicos_por_perrito_vet', id = mascota.id)


def lista_historiales_inhabilitadas_por_mascota_veter(request, id):
    historial = HistorialMedico.objects.filter(estado_historial = 2)
    perrito = Mascota.objects.get(id = id)
    return render(request, "crud_mascotas_vet/lista_historiales_inhabilitados_por_mascota_veter.html", {'entity': historial, "perrito": perrito})

def habilitar_historial_por_mascota_veter(request, id):
    historial = HistorialMedico.objects.get(id = id)
    id_mascota = historial.mascota.id
    mascota = Mascota.objects.get(id = id_mascota)
    historial.estado_historial= 1
    historial.save()
    messages.success(request,"Historial inhabilitado correctamente")
    return redirect('Lista_Historial_Inhabilitados_por_mascota_veter', id = mascota.id)


def seguimiento_por_perrito_vet(request, id):
    peticion = SeguimientoAdopcion.objects.filter(solicitud_adopcion__mascota = id)
    mascota = Mascota.objects.get(id=id)
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(peticion, 3)
        peticion = paginator.page(page)
    except:
        pass

    return render(request, "crud_mascotas_vet/seguimiento_por_perrito_veter.html", {"entity": peticion, "mascota": mascota, "paginator": paginator})

#ADOPTANTE--------------------------------------------------------

class registrar_solicitud_adoptante(View):
    def get(self, request):

        formulario = SolicitudAdoptanteForm()

        return render(request, "crud_adoptante/registrar_solicitud_adoptante.html", {"formulario": formulario})
    
    def post(self, request):

        formulario = SolicitudAdoptanteForm(request.POST, request.FILES)
        usuario = self.request.user

        if formulario.is_valid():

            solicitud = formulario.save(commit=False)
            solicitud.adoptante = usuario
            solicitud.save()
            messages.success(request, "Solicitud enviada correctamente")
            return redirect('perritos_adop')
        
        else:
            for campo, errores in formulario.errors.items():  # Itera sobre los campos y sus errores
                for error in errores:  # Itera sobre los errores de cada campo
                    messages.error(request, f"{campo}: {error}")  # Agrega el mensaje de error al contexto de mensajes
            return render(request, 'crud_adoptante/registrar_solicitud_adoptante.html', {"formulario": formulario}) 

