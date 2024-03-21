from django import forms
from inventario.models import Articulos, Entradas, Salidas

class ArticulosForm(forms.ModelForm):

    class Meta:
        model = Articulos
        fields = ['nombre', 'descripcion', 'referencia', 'imagen']
        exclude = ['usuario']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nombre'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['descripcion'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['referencia'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['imagen'].widget.attrs.update({
            'class': 'form-control',
        })



class EntradasForm(forms.ModelForm):

    class Meta:
        model = Entradas
        fields = ['articulo', 'cantidad_entrada']
        exclude = ['administrador']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['articulo'].widget.attrs.update({
            'class': 'form-control',
            'required': 'required',
        })
        self.fields['cantidad_entrada'].widget.attrs.update({
            'class': 'form-control',
            'required': 'required',
        })

class SalidasForm(forms.ModelForm):

    class Meta:
        model = Salidas
        fields = ['articulo', 'cantidad_salida']
        exclude = ['administrativo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['articulo'].widget.attrs.update({
            'class': 'form-control',
            'required': 'required',
        })
        self.fields['cantidad_salida'].widget.attrs.update({
            'class': 'form-control',
            'required': 'required',
        })