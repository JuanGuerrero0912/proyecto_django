from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from homePage import views

urlpatterns = [
    path('', views.Inicio_Admin, name="Inicio_Admin"),

]