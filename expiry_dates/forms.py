from django.forms import ModelForm
from django import forms
from .models import Producto
from django.contrib.auth.forms import AuthenticationForm

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'fecha_vencimiento')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-control', 'id': 'nombre_producto'})
        self.fields['fecha_vencimiento'].widget.attrs.update({'class': 'form-control', 'id': 'fecha_venci', 'type': 'date', 'placeholder':'mm/dd/aaaa'})
    
class ExtendedAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({"id":"login", "class":"fadeIn second", "name":"login", "placeholder":"Usuario"})
        self.fields['password'].widget.attrs.update({"id":"password", "class":"fadeIn third", "name":"login", "placeholder":"Clave"})

class SearchForm(forms.Form):
    search_word = forms.CharField(max_length=30, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['search_word'].widget.attrs.update({"class":"form-control","placeholder":"Nombre del producto"})