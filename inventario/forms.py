from django import forms
from inventario.models import Articulos

class ArticulosForm(forms.ModelForm):

    class Meta:
        model = Articulos
        filds = '__all__'
        exclude = ()