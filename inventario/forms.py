from django import forms
from inventario.models import Articulos, Entradas, Salidas

class ArticulosForm(forms.ModelForm):

    class Meta:
        model = Articulos
        fields = ['nombre', 'descripcion', 'referencia', 'estado_articulo']
        exclude = ['usuario']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['estado_articulo'].widget.attrs.update({
            'class': 'form-control',
        })

class EntradasForm(forms.ModelForm):

    class Meta:
        model = Entradas
        filds = '__all__'
        exclude = ()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['articulo'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['estado_entrada'].widget.attrs.update({
            'class': 'form-control',
        })

class SalidasForm(forms.ModelForm):

    class Meta:
        model = Salidas
        filds = '__all__'
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['articulo'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['estado_salida'].widget.attrs.update({
            'class': 'form-control',
        })