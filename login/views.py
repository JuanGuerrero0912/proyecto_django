from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from login.models import Perfil
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from login.forms import CustomUserCreationForms
from homePage.forms import Perfil_Registro_Adoptante


# Create your views here.

#-------------------------------------------------------------------------------------
#Login y Registro: 
def interfaz_login(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username = nombre_usuario, password = contra)
            if usuario is not None:
                usu = User.objects.get(username = nombre_usuario)
                perfil = Perfil.objects.get(user = usu)
                if perfil.rol == 1:
                    login(request, usuario)
                    return redirect('Inicio_Admin')
                elif perfil.rol == 2:
                    login(request, usuario)
                    return redirect('Inicio_Veter')
                elif perfil.rol == 3:
                    login(request, usuario)
                    return redirect('Inicio_Adoptante')
                else:
                    messages.error(request, "No es posible ingresar")
            else:
                messages.error(request, "Usuario no valido")
        else:
            messages.error(request, "Usuario y/o contraseña incorrectos.")
    form = AuthenticationForm()
    return render(request, "paginas_login/login.html", {"form": form})

class VRegistro(View):
    def get(self, request):
        form = CustomUserCreationForms()
        formulario = Perfil_Registro_Adoptante()
        
        return render(request, "paginas_login/registro.html", {"form": form, "formulario": formulario})

    def post(self, request):
        
        form = CustomUserCreationForms(request.POST)
        username = request.POST.get("username")

        if form.is_valid():
            
            usuario = form.save()
            login(request, usuario)
            user = User.objects.get(username = username)
            formulario = Perfil_Registro_Adoptante(request.POST, request.FILES, instance =user.perfil)
            if formulario.is_valid():
                formulario.save()
                messages.success(request,"Tu registro ha sido exitoso")
                return redirect('Inicio_Adoptante')
            else:
                messages.error(request, "Tienes campos que no cumplen con los requisitos que se te indican")

                return render(request, "paginas_login/registro.html", {"form": form, "formulario": formulario })
        
        else:
            formulario = Perfil_Registro_Adoptante()
            messages.error(request, "Tienes campos que no cumplen con los requisitos que se te indican")
            
            return render(request, "paginas_login/registro.html", {"form": form, "formulario": formulario})

def cerrar_sesion(request):
    
    logout(request)
    messages.success(request,"Gracias por utilizar la web de la fundación, esperamos que vuelvas pronto.")
    return redirect('Inicio')

#-------------------------------------------------------------------------------------
#Crear usuarios administradores:
