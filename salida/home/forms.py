from django import forms
from .models import *


#//____________segir con el formulario..... no se olvide bitch :P jajajaj______

class agregar_producto_form(forms.ModelForm):
	class Meta:
		model = Producto
		fields = '__all__'


