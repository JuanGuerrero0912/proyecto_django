from django.shortcuts import render

# Create your views here.

def Inicio_Admin(request):
    return render(request, "paginas_admin/inicio.html")