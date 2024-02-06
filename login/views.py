from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, "paginas_login/login.html")

def registro(request):
    return render(request, "paginas_login/registro.html")