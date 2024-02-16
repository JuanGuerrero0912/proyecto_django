from django import forms
from inventario.models import Articulos, Entradas, Salidas

class ArticulosForm(forms.ModelForm):
    class Meta:
        model = Articulos
        fields = '__all__'