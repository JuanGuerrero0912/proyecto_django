from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from usuario.models import Usuario

# Create your views here.

def interfaz_login(request):
    if request.method=="POST":
        user = Usuario()
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(usuario = nombre_usuario, password = contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('Inicio_Admin')
            else:
                messages.error(request, "Usuario no valido")
        else:
            messages.error(request, "Información incorrecta")
    form = AuthenticationForm()
    return render(request, "paginas_login/login.html", {"form": form})

def registro(request):
    return render(request, "paginas_login/registro.html")

def cerrar_sesion(request):
    logout(request)
    return redirect('Inicio')