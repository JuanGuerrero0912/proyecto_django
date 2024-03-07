from django.http import HttpResponse
from django.shortcuts import render, redirect
from mascota.models import Mascota, Adopcion,  HistorialMedico, SolicitudAdopcion, SeguimientoAdopcion
from inventario.models import Articulos, Entradas, Salidas
from donaciones.models import Donaciones
from login.models import Perfil
from homePage.forms import Perfil_Adoptante, Usuario_Adoptante, Usuario_Administrador, Perfil_Administrador, Usuario_Veterinario, Perfil_Veterinario, Perfil_Registro_Adoptante, Perfil_Registro 
from django.contrib.auth.models import User
from django.views.generic import View
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash
from login.forms import CustomUserCreationForms


# Create your views here.

#-------------------------------------------------------------------------------------
#ADMINISTRADOR: 
def Inicio_Admin(request):
    return render(request, "paginas_admin/inicio.html")
    

def Lista_usuarios(request):

    usuarios = Perfil.objects.filter(estado_perfil = 1)

    return render(request, "paginas_admin/lista_usuarios.html", {"usuarios": usuarios})

def Usuarios(request):
    return render(request, "paginas_admin/usuarios.html")

def Adopciones(request):
    return render(request, "paginas_admin/adopciones.html")

class Registrar_usuario_administrativo(View):

    def get(self, request):
        
        form = CustomUserCreationForms()
        formulario = Perfil_Registro()

        return render(request, "paginas_admin/registrar_usuario.html", {"form": form, "formulario": formulario})
    
    def post(self, request):

        form = CustomUserCreationForms(request.POST)
        username = request.POST.get("username")
        
        if form.is_valid():
  
            form.save()
            user = User.objects.get(username = username)
            formulario = Perfil_Registro(request.POST, request.FILES, instance=user.perfil)
            if formulario.is_valid():
                formulario.save()
                messages.success(request,"Usuario administrativo creado correctamente")
                return redirect('Lista_usuarios')

        else:
            messages.error(request, "Tienes campos que no cumplen con los requisitos que se te indican")
            
            return render(request, "paginas_admin/registrar_usuario.html", {"form": form, "formulario": formulario })

class Actualizar_usuario_administrativo(View):

    def get(self, request, id):

        usuario = User.objects.get(id = id)
        form = Usuario_Administrador(instance=usuario)
        formulario = Perfil_Registro(instance=usuario.perfil)
        

        return render(request, "paginas_admin/actualizar_usuario.html", {"form": form,"formulario": formulario, "usuario": usuario})

    def post(self, request, id):
        usuario = User.objects.get(id = id)
        form = Usuario_Administrador(request.POST,instance=usuario)
        formulario = Perfil_Registro(request.POST,request.FILES,instance=usuario.perfil)

        if form.is_valid() and formulario.is_valid():

            form.save()
            formulario.save()
            messages.success(request, "Usuario actualizado correctamente")
            return redirect('Lista_usuarios')
        
        else:
            messages.error(request, "No se pudo actualizar el usuario intentalo otra vez")
            
            return render(request, "paginas_admin/actualizar_usuario.html", {"form": form,"formulario": formulario, "usuario": usuario})

def ver_usuario_administrativo(request, id):

    usuario = User.objects.get(id = id)
    form = Usuario_Administrador(instance=usuario)
    formulario = Perfil_Registro(instance=usuario.perfil)

    return render(request, "paginas_admin/ver_usuario.html", {"form": form,"formulario": formulario, "usuario": usuario})

def inhabilitar_usuario(request, id):

    perfil = Perfil.objects.get(id = id)
    perfil.estado_perfil = 2
    perfil.save()
    messages.success(request,"Usuario inhabilitado correctamente")
    return redirect('Lista_usuarios')

def lista_usuarios_inhabilitados(request):
    usuarios = Perfil.objects.filter(estado_perfil = 2)
    return render(request, "paginas_admin/listado_usuarios_inhabilitados.html", {"usuarios": usuarios})

def habilitar_usuario(request, id):

    perfil = Perfil.objects.get(id = id)
    perfil.estado_perfil = 1
    perfil.save()
    messages.success(request,"Usuario habilitado correctamente")
    return redirect('Lista_usuarios_inhabilitados')


def Lista_adoptantes(request):

    usuarios = Perfil.objects.filter(estado_perfil = 1)

    return render(request, "paginas_admin/lista_adoptantes.html", {"usuarios": usuarios})

class registrar_usuario_adoptante(View):

    def get(self, request):

        form = CustomUserCreationForms()
        formulario = Perfil_Registro_Adoptante()
        
        return render(request, "paginas_admin/registrar_adoptante.html", {"form": form,"formulario": formulario})
    
    def post(self, request):

        form = CustomUserCreationForms(request.POST)
        username = request.POST.get("username")
        if form.is_valid():
  
            form.save()
            user = User.objects.get(username = username)
            formulario = Perfil_Registro_Adoptante(request.POST, request.FILES, instance=user.perfil)
            if formulario.is_valid():
                formulario.save()
                messages.success(request,"Adoptante creado correctamente")
                return redirect('Lista_adoptantes')

        else:
            messages.error(request, "Tienes campos que no cumplen con los requisitos que se te indican")          
            return render(request, "paginas_admin/registrar_adoptante.html", {"form": form, "formulario": formulario })
        
class Actualizar_adoptante(View):

    def get(self, request, id):

        usuario = User.objects.get(id = id)
        form = Usuario_Administrador(instance=usuario)
        formulario = Perfil_Registro_Adoptante(instance=usuario.perfil)
        
        return render(request, "paginas_admin/actualizar_adoptante.html", {"form": form,"formulario": formulario, "usuario": usuario})
    
    def post(self, request, id):
        usuario = User.objects.get(id = id)
        form = Usuario_Administrador(request.POST,instance=usuario)
        formulario = Perfil_Registro_Adoptante(request.POST,request.FILES,instance=usuario.perfil)

        if form.is_valid() and formulario.is_valid():

            form.save()
            formulario.save()
            messages.success(request, "Adoptante actualizado correctamente")
            return redirect('Lista_adoptantes')
        
        else:
            messages.error(request, "No se pudo actualizar el usuario intentalo otra vez")
            
            return render(request, "paginas_admin/actualizar_adoptante.html", {"form": form,"formulario": formulario, "usuario": usuario})

def ver_adoptante(request, id):

    usuario = User.objects.get(id = id)
    form = Usuario_Administrador(instance=usuario)
    formulario = Perfil_Registro_Adoptante(instance=usuario.perfil)
        
    return render(request, "paginas_admin/ver_adoptante.html", {"form": form,"formulario": formulario, "usuario": usuario})


def inhabilitar_adoptante(request, id):

    perfil = Perfil.objects.get(id = id)
    perfil.estado_perfil = 2
    perfil.save()
    messages.success(request,"Adoptante inhabilitado correctamente")
    return redirect('Lista_adoptantes')

def lista_adoptantes_inhabilitados(request):

    usuarios = Perfil.objects.filter(estado_perfil = 2)
    return render(request, "paginas_admin/listado_adoptantes_inhabilitados.html", {"usuarios": usuarios})

def habilitar_adoptante(request, id):

    perfil = Perfil.objects.get(id = id)
    perfil.estado_perfil = 1
    perfil.save()
    messages.success(request,"Adoptante habilitado correctamente")
    return redirect('Lista_adoptantes_inhabilitados')


def Lista_adopciones(request):
    adopciones = Adopcion.objects.all()
    mascotas = Mascota.objects.all()
    mascotas_rescatadas = Mascota.objects.filter(estadoRegistro = 1).count()
    adopciones_finalizadas = Adopcion.objects.filter(estado_adopcion = 1).count()
    adopciones_rechazadas = SolicitudAdopcion.objects.filter(estado_proceso = 3).count()
    adopciones_proceso = SolicitudAdopcion.objects.filter(estado_proceso = 2).count()
    porcentaje_adoptados = (mascotas_rescatadas / adopciones_finalizadas) * 100

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(mascotas, 3)
        mascotas =  paginator.page(page)
    except:
        pass
    return render(request, "paginas_admin/lista_adopciones.html", 
                  {"entity": adopciones, "paginator": paginator,
                    "mascotas_rescatadas": mascotas_rescatadas,
                    "adopciones_finalizadas": adopciones_finalizadas,
                    "adopciones_rechazadas": adopciones_rechazadas,
                    "adopciones_proceso": adopciones_proceso,
                    "porcentaje_adoptados": porcentaje_adoptados})


def Registrar_adoptante(request):
    return render(request, "paginas_admin/registrar_adoptante.html")

def Registrar_adopcion(request):
    return render(request, "paginas_admin/registrar_adopcion.html")

def Lista_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, "paginas_admin/lista_mascotas.html", {"entity": mascotas})

def Lista_historial_medico(request):
    historiales = HistorialMedico.objects.all()
    return render(request, "paginas_admin/lista_historial_medico.html", {"entity": historiales})

def Lista_solicitudes_adopcion(request):
    solicitudes = SolicitudAdopcion.objects.all()
    return render(request, "paginas_admin/lista_solicitudes_adopcion.html", {"entity": solicitudes})

def Lista_seguimientos_proceso(request):
    seguimientos = SeguimientoAdopcion.objects.all()
    return render(request, "paginas_admin/lista_seguimientos_proceso.html", {"entity": seguimientos})

def Lista_donaciones(request):

    donaciones = Donaciones.objects.all()

    return render(request, "paginas_admin/lista_donaciones.html", {'donaciones': donaciones})

def Lista_articulos(request):

    articulos = Articulos.objects.all()

    return render(request, "paginas_admin/lista_articulos.html", {'articulos': articulos})

def Lista_entradas(request):

    entradas = Entradas.objects.all()

    return render(request, "paginas_admin/lista_entradas.html", {'entradas': entradas})

def Lista_salidas(request):

    salidas = Salidas.objects.all()

    return render(request, "paginas_admin/lista_salidas.html", {'salidas': salidas})

def Donaciones_Interfaz(request):
    return render(request, "paginas_admin/donaciones.html")

def Inventario(request):
    return render(request, "paginas_admin/inventario.html")


def Perritos_admin(request):

    mascotas = Mascota.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(mascotas, 3)
        mascotas =  paginator.page(page)
    except:
        pass

    return render(request, "paginas_admin/perritos_admin.html", {"entity": mascotas, "paginator": paginator})

class Actualizar_Perfil_Administrador(View):

    def get(self, request):
        usuario = self.request.user
        formulario_user = Usuario_Administrador(instance=usuario)
        formulario = Perfil_Administrador(instance=usuario.perfil)

        return render(request, "paginas_admin/perfil_administrador.html", {"formulario_user": formulario_user, "formulario":formulario})

    def post(self, request):

        usuario = self.request.user
        formulario_user = Usuario_Administrador(request.POST,instance=usuario)
        formulario = Perfil_Administrador(request.POST,request.FILES,instance=usuario.perfil)

        if formulario_user.is_valid() and formulario.is_valid():
            formulario_user.save()
            formulario.save()
            messages.success(request, "Pefil actualizado correctamente")
            return redirect('Perfil_Administrador')
        
        else:
            messages.error(request, "No se pudo actualizar el perfil")
            return render(request, "paginas_admin/perfil_administrador.html", {"formulario_user": formulario_user, "formulario":formulario})

class CambioContraseñaAdministrador(PasswordChangeView):

    template_name = "paginas_admin/cambio_contraseña_administrador.html"
    success_url = reverse_lazy('Perfil_Administrador')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['password_changed'] = self.request.session.get('password_changed', False)
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Cambio de contraseña exitoso")
        update_session_auth_hash(self.request, form.user)
        self.request.session['password_changed'] = True
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "No se pudo cambiar la contraseña, intentelo nuevamente")
        return super().form_valid(form)


#-------------------------------------------------------------------------------------
#VETERINARIO: 

def Inicio_Veterinario(request):
    return render(request, "paginas_veter/inicio_veter.html")

def Adopciones_vete(request):
    return render(request, "paginas_veter/adopciones.html")

def Lista_adopciones_vete(request):
    adopciones = Adopcion.objects.all()
    return render(request, "paginas_veter/lista_adopciones.html", {"entity": adopciones})

def Lista_mascotas_vete(request):
    mascotas = Mascota.objects.all()
    return render(request, "paginas_veter/lista_mascotas.html", {"entity": mascotas})

def Lista_historial_vete(request):
    historiales = HistorialMedico.objects.all()
    return render(request, "paginas_veter/lista_historial.html", {"entity": historiales})

def Perritos_vete(request):

    mascotas = Mascota.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(mascotas, 3)
        mascotas =  paginator.page(page)
    except:
        pass

    return render(request, "paginas_veter/perritos.html", {"entity": mascotas, "paginator": paginator})

def vista_articulos_veterinario(request):

    articulos = Articulos.objects.all()

    return render(request, "paginas_veter/lista_articulos_veter.html", {'articulos': articulos})

def inventario_veter(request):

    return render(request, "paginas_veter/inventario_veter.html")

def vista_salidas_veterinario(request):

    salidas = Salidas.objects.all()

    return render(request, "paginas_veter/lista_salidas_veter.html", {'salidas': salidas})

class Actualizar_Perfil_Veterinario(View):

    def get(self, request):

        usuario = self.request.user
        formulario_user = Usuario_Adoptante(instance=usuario)
        formulario = Perfil_Adoptante(instance=usuario.perfil)

        return render(request, "paginas_veter/perfil_veterinario.html",{"formulario_user": formulario_user, "formulario":formulario})

    def post(self, request):

        usuario = self.request.user
        formulario_user = Usuario_Veterinario(request.POST, instance=usuario)
        formulario = Perfil_Veterinario(request.POST, request.FILES,instance=usuario.perfil)

        if formulario_user.is_valid() and formulario.is_valid():
            formulario_user.save()
            formulario.save()
            messages.success(request, "Pefil actualizado correctamente")
            return redirect('Perfil_Veterinario')
        
        else:
            messages.error(request, "No se pudo actualizar el perfil")
            return render(request, "paginas_veter/perfil_veterinario.html",{"formulario_user": formulario_user, "formulario":formulario})
        
class CambioContraseñaVeterinario(PasswordChangeView):
    template_name = "paginas_veter/cambio_contraseña_veterinario.html"
    success_url = reverse_lazy('Perfil_Veterinario')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['password_changed'] = self.request.session.get('password_changed', False)
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Cambio de contraseña exitoso")
        update_session_auth_hash(self.request, form.user)
        self.request.session['password_changed'] = True
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "No se pudo cambiar la contraseña, intentelo nuevamente")
        return super().form_valid(form)

#-------------------------------------------------------------------------------------
#ADOPTANTE: 

def Inicio_Adoptante(request):
    return render(request, "paginas_adoptante/inicio_adoptante.html")

class VPerfilRegistro(View):

    def get(self, request):

        usuario = self.request.user
        formulario = Perfil_Adoptante(instance=usuario.perfil)

        return render(request, "paginas_adoptante/registro_perfil.html", {"formulario": formulario})
    
    def post(self, request):

        usuario = self.request.user
        formulario = Perfil_Adoptante(request.POST, request.FILES,instance=usuario.perfil)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Datos guardados correctamente")
            return redirect('Inicio_Adoptante')
        else:
            messages.error(request, "No se pudo guardar los datos")
            return render(request, "paginas_adoptante/registro_perfil.html", {"formulario": formulario})

class Actualizar_Perfil_Adoptante(View):

    def get(self, request):

        usuario = self.request.user
        formulario_user = Usuario_Adoptante(instance=usuario)
        formulario = Perfil_Adoptante(instance=usuario.perfil)

        return render(request, "paginas_adoptante/perfil_adoptante.html",{"formulario_user": formulario_user, "formulario":formulario})
    
    def post(self, request):
        
        usuario = self.request.user
        formulario_user = Usuario_Adoptante(request.POST, instance=usuario)
        formulario = Perfil_Adoptante(request.POST, request.FILES,instance=usuario.perfil)


        if formulario_user.is_valid() and formulario.is_valid():
            formulario_user.save()
            formulario.save()
            messages.success(request, "Pefil actualizado correctamente")
            return redirect('Perfil_Adoptante')
        
        else:
            messages.error(request, "No se pudo actualizar el perfil")
            return render(request, "paginas_adoptante/perfil_adoptante.html",{"formulario_user": formulario_user, "formulario":formulario})

class CambioContraseñaADoptante(PasswordChangeView):
    template_name = "paginas_adoptante/cambio_contraseña_adoptante.html"
    success_url = reverse_lazy('Perfil_Adoptante')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['password_changed'] = self.request.session.get('password_changed', False)
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Cambio de contraseña exitoso")
        update_session_auth_hash(self.request, form.user)
        self.request.session['password_changed'] = True
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "No se pudo cambiar la contraseña, intentelo nuevamente")
        return super().form_valid(form)





        