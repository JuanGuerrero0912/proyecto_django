from django.urls import path
from django.conf import settings
from Inicio import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('nosotros', views.nosotros, name="Nosotros"),
    path('perritos', views.perritos, name="Perritos"),
    path('noticias', views.noticias, name="Noticias"),
    path('donaciones', views.donaciones, name="Interfaz_Donaciones"),
    path('trabaja_con_nosotros', views.trabaja_con_nosotros, name="Trabaja"),

]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)