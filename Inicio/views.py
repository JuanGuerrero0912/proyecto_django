from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "paginas/inicio.html")

def nosotros(request):
    return render(request, "paginas/nosotros.html")

def perritos(request):
    return render(request, "paginas/perritos.html")

def noticias(request):
    return render(request, "paginas/noticias.html")

def donaciones(request):
    return render(request, "paginas/donaciones.html")

def trabaja_con_nosotros(request):
    return render(request, "paginas/trabajaconnosotros.html")