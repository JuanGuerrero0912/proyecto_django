from django.shortcuts import render
from mascota.models import Mascota
from django.core.paginator import Paginator

# Create your views here.

def Inicio_Admin(request):
    return render(request, "paginas_admin/inicio.html")

def Lista_usuarios(request):
    return render(request, "paginas_admin/lista_usuarios.html")

def Usuarios(request):
    return render(request, "paginas_admin/usuarios.html")

def Adopciones(request):
    return render(request, "paginas_admin/adopciones.html")

def Registrar_usuario(request):
    return render(request, "paginas_admin/registrar_usuario.html")

def Lista_adoptantes(request):
    return render(request, "paginas_admin/lista_adoptantes.html")

def Lista_adopciones(request):
    return render(request, "paginas_admin/lista_adopciones.html")

def Registrar_adoptante(request):
    return render(request, "paginas_admin/registrar_adoptante.html")

def Registrar_adopcion(request):
    return render(request, "paginas_admin/registrar_adopcion.html")

def Lista_mascotas(request):
    return render(request, "paginas_admin/lista_mascotas.html")

def Lista_historial_medico(request):
    return render(request, "paginas_admin/lista_historial_medico.html")

def Lista_solicitudes_adopcion(request):
    return render(request, "paginas_admin/lista_solicitudes_adopcion.html")

def Lista_seguimientos_proceso(request):
    return render(request, "paginas_admin/lista_seguimientos_proceso.html")

def Lista_donaciones(request):
    return render(request, "paginas_admin/lista_donaciones.html")

def Lista_inventario(request):
    return render(request, "paginas_admin/lista_inventario.html")

def Lista_articulos(request):
    return render(request, "paginas_admin/lista_articulos.html")

def Lista_entradas(request):
    return render(request, "paginas_admin/lista_entradas.html")

def Lista_salidas(request):
    return render(request, "paginas_admin/lista_salidas.html")

def Donaciones(request):
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