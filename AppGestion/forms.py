
from django import forms
from .models import Producto

class editarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'imagen1', 'precio']

