from django import forms
from donaciones.models import Donaciones

class DonacionForms(forms.ModelForm):

    class Meta:
        model = Donaciones
        fields = ['tipo_donacion', 'cantidad_donacion', 'Articulos', 'entregado', 'usuario']
        exclude = []
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['tipo_donacion'].widget.attrs.update({
            'class': 'form-control',
            'required': 'required',
        })
        self.fields['Articulos'].widget.attrs.update({
            'class': 'form-control',
            'required': 'required',
        })
        self.fields['cantidad_donacion'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['usuario'].widget.attrs.update({
            'class': 'form-control',
            'required': 'required',
        })


