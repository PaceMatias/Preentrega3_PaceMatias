from django import forms
#formularios de ingreso
class Ingreso_PuntoVenta_Form(forms.Form):
    comercio = forms.CharField(max_length=40)
    provincia = forms.CharField(max_length=40)
    ciudad = forms.CharField(max_length=70)
    domicilio = forms.CharField(max_length=70)
    red_social = forms.CharField(max_length=60)
    telefono = forms.CharField(max_length=20)
    email = forms.EmailField()

class Ingreso_Bombacha_Form(forms.Form):
    nombre = forms.CharField(max_length=20)
    articulo =  forms.IntegerField()
    talle = forms.CharField(max_length=10) 
    color = forms.CharField(max_length=40)
    tipo_bombacha = forms.CharField(max_length=20)

class Ingreso_Conjunto_Form(forms.Form):
    nombre = forms.CharField(max_length=20)
    articulo =  forms.IntegerField()
    talle = forms.CharField(max_length=10) 
    color = forms.CharField(max_length=40)
    tipo_taza = forms.CharField(max_length=20)
    tipo_bombacha = forms.CharField(max_length=20)

class Ingreso_Dormir_Form(forms.Form):
    nombre = forms.CharField(max_length=20)
    articulo =  forms.IntegerField()
    talle = forms.CharField(max_length=10) 
    color = forms.CharField(max_length=40)
    tipo_prenda = forms.CharField(max_length=20)

#formularios de busqueda
class Buscar_Bombacha(forms.Form):
    tipo_bombacha = forms.CharField(max_length=20)
    