from django import forms
from donaciones.models import Donaciones

class DonacionForms(forms.ModelForm):

    class Meta:
        model = Donaciones
        filds = '__all__'
        exclude = ()