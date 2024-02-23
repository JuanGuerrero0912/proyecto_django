from django import forms
from inventario.models import Articulos, Entradas, Salidas

class ArticulosForm(forms.ModelForm):

    class Meta:
        model = Articulos
        filds = '__all__'
        exclude = ()

class EntradasForm(forms.ModelForm):

    class Meta:
        model = Entradas
        filds = '__all__'
        exclude = ()

class SalidasForm(forms.ModelForm):

    class Meta:
        model = Salidas
        filds = '__all__'
        exclude = ()