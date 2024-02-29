from django.shortcuts import render
from .forms import FormularioContacto
from django.core.mail import EmailMessage
from django.contrib import messages
from mascota.models import Mascota, Adopcion
from django.core.paginator import Paginator

# Create your views here.
def inicio(request):
    if request.method == "POST":
        nombre= request.POST.get("nombre")
        email= request.POST.get("email")
        contenido= request.POST.get("contenido")

        email = EmailMessage("Doggy at Home",
                                 "El usuario con nombre {} con la dirección de correo {} escribe lo siguiente: \n\n {}".format(nombre,email,contenido),
                                 "", ["doggyathomecp@gmail.com"], reply_to=[email])

        try:
            email.send()
            messages.success(request, 'Correo enviado con exito.')
            return render(request, "paginas/mensaje.html", {'miFormulario': FormularioContacto})
        except Exception as e:
            messages.error(request, f"Ocurrio un error al enviar el correo: {e}")
            return render(request, "paginas/inicio.html")
    
    mascotas = Mascota.objects.all()
    mascotas_rescatadas = Mascota.objects.filter(estadoRegistro = 1).count()
    mascotas_adoptadas = Adopcion.objects.filter(estado_adopcion = 1).count()
    mascotas_por_adoptar = Mascota.objects.filter(estadoMascota = 1).count()
    mascotas_tratamiento = Mascota.objects.filter(estadoMascota = 2).count()
    total_por_adoptar = mascotas_por_adoptar + mascotas_tratamiento
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(mascotas, 3)
        mascotas =  paginator.page(page)
    except:
        pass
    return render(request, "paginas/inicio.html", 
                  {"entity": mascotas, "paginator": paginator,
                    "mascotas_rescatadas": mascotas_rescatadas,
                    "mascotas_adoptadas": mascotas_adoptadas,
                    "total_por_adoptar": total_por_adoptar})

def nosotros(request):
    return render(request, "paginas/nosotros.html")

def perritos(request):

    mascotas = Mascota.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(mascotas, 3)
        mascotas =  paginator.page(page)
    except:
        pass

    return render(request, "paginas/perritos.html", {"entity": mascotas, "paginator": paginator})

def noticias(request):
    return render(request, "paginas/noticias.html")

def donaciones(request):
    return render(request, "paginas/donaciones.html")

def trabaja_con_nosotros(request):

    if request.method == "POST":
        nombre= request.POST.get("nombre")
        email= request.POST.get("email")
        asunto = request.POST.get("asunto")
        contenido= request.POST.get("contenido")

        email = EmailMessage(f"Doggy at Home - {asunto}",
                                 "El usuario con nombre {} con la dirección de correo {} escribe lo siguiente: \n\n {}".format(nombre,email,contenido),
                                 "", ["doggyathomecp@gmail.com"], reply_to=[email])

        try:
            email.send()
            messages.success(request, 'Correo enviado con exito.')
            return render(request, "paginas/mensaje.html", {'miFormulario': FormularioContacto})
        except Exception as e:
            messages.error(request, f"Ocurrio un error al enviar el correo: {e}")
            return render(request, "paginas/trabajaconnosotros.html")
    return render(request, "paginas/trabajaconnosotros.html")
