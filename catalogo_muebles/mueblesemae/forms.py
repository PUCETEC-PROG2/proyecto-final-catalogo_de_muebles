from django import forms
from .models import Mueble

class MuebleForm(forms.ModelForm):
    class Meta:
        model = Mueble
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'type': 'Tipo',
            'material': 'Material',
            'style': 'Estilo',
            'picture': 'Imagen'
            
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'material': forms.Select(attrs={'class': 'form-control'}),
            'style': forms.Select(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }