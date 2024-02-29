from django.shortcuts import render
from mascota.models import Mascota, Adopcion,  HistorialMedico, SolicitudAdopcion, SeguimientoAdopcion
from inventario.models import Articulos, Entradas, Salidas
from donaciones.models import Donaciones
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
    adopciones = Adopcion.objects.all()
    return render(request, "paginas_admin/lista_adopciones.html", {"entity": adopciones})

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

def Inicio_Veterinario(request):
    return render(request, "paginas_veter/inicio_veter.html")

def Inicio_Adoptante(request):
    return render(request, "paginas_adoptante/inicio_adoptante.html")

#-------------------------------------------------------------------------------------

        #VETERINARIO: 

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