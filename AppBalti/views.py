from django.shortcuts import render
from django.http import HttpResponse
from AppBalti.forms import *
from AppBalti.models import *

# Create your views here.

#vistas de portada
def inicio(request):
    return render(request, "AppBalti/inicio.html")

def puntos_de_venta(request):
     return render(request, "AppBalti/puntos_de_venta.html")

def bombachas(request):
    return render(request, "AppBalti/bombachas.html")

def conjunto(request):
    return render(request, "AppBalti/conjunto.html")

def dormir(request):
    return render(request, "AppBalti/dormir.html")

#Vistas de Formulario para crear

def puntoventa_formulario(request):
    if request.method == "POST":
        form = Ingreso_PuntoVenta_Form(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            puntoventa = Puntos_De_Venta(comercio = datos["comercio"],
                                        provincia = datos["provincia"],
                                        ciudad = datos["ciudad"],
                                        domicilio = datos["domicilio"],
                                        red_social = datos["red_social"],
                                        telefono = datos["telefono"],
                                        email = datos["email"])
            puntoventa.save()
            mensaje = f"Se creo el punto de venta {datos['comercio']}"
            form = Ingreso_PuntoVenta_Form()
            return render(request,"AppBalti/Formpuntoventa.html",{"mensaje":mensaje,"form":form})
        else:
            mensaje = "No se creo el punto de venta, algún dato es incorrecto o incompleto"
            form = Ingreso_PuntoVenta_Form()
            return render(request,"AppBalti/Formpuntoventa.html",{"mensaje":mensaje,"form":form})
                
    else:
        form = Ingreso_PuntoVenta_Form()

    return render(request,"AppBalti/Formpuntoventa.html",{"form":form})



def conjunto_formulario(request):
    if request.method == "POST":
        form = Ingreso_Conjunto_Form(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            conjuntonuevo = Conjunto (
                                        nombre = datos["nombre"],
                                        articulo =  datos["articulo"],
                                        talle = datos["talle"], 
                                        color = datos["color"],
                                        tipo_taza = datos["tipo_taza"],
                                        tipo_bombacha = datos["tipo_bombacha"]
                                    )
            conjuntonuevo.save()
            mensaje = f"Se creo el conjunto {datos['nombre']}"
            form = Ingreso_Conjunto_Form()
            return render(request,"AppBalti/Formconjunto.html",{"mensaje":mensaje,"form":form})
        else:
            mensaje = "No se creo el conjunto, algún dato es incorrecto o incompleto"
            form = Ingreso_Conjunto_Form()
            return render(request,"AppBalti/Formconjunto.html",{"mensaje":mensaje,"form":form})
                
    else:
        form = Ingreso_Conjunto_Form()

    return render(request,"AppBalti/Formconjunto.html",{"form":form})



def bombacha_formulario(request):
    if request.method == "POST":
        form = Ingreso_Bombacha_Form(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            bombachanueva = Bombacha (
                                        nombre = datos["nombre"],
                                        articulo =  datos["articulo"],
                                        talle = datos["talle"], 
                                        color = datos["color"],
                                        tipo_bombacha = datos["tipo_bombacha"]
                                    )
            bombachanueva.save()
            mensaje = f"Se creo la bombacha {datos['nombre']}"
            form = Ingreso_Bombacha_Form()
            return render(request,"AppBalti/Formbombacha.html",{"mensaje":mensaje,"form":form})
        else:
            mensaje = "No se creo la bombacha, algún dato es incorrecto o incompleto"
            form = Ingreso_Bombacha_Form()
            return render(request,"AppBalti/Formbombacha.html",{"mensaje":mensaje,"form":form})
                
    else:
        form = Ingreso_Bombacha_Form()

    return render(request,"AppBalti/Formbombacha.html",{"form":form})


def dormir_formulario(request):
    if request.method == "POST":
        form = Ingreso_Dormir_Form(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            prendanueva = Dormir (
                                        nombre = datos["nombre"],
                                        articulo =  datos["articulo"],
                                        talle = datos["talle"], 
                                        color = datos["color"],
                                        tipo_prenda = datos["tipo_prenda"]
                                    )
            prendanueva.save()
            mensaje = f"Se creo {datos['nombre']}"
            form = Ingreso_Dormir_Form()
            return render(request,"AppBalti/Formdormir.html",{"mensaje":mensaje,"form":form})
        else:
            mensaje = "No se creo la prenda, algún dato es incorrecto o incompleto"
            form = Ingreso_Dormir_Form()
            return render(request,"AppBalti/Formdormir.html",{"mensaje":mensaje,"form":form})
                
    else:
        form = Ingreso_Dormir_Form()

    return render(request,"AppBalti/Formdormir.html",{"form":form})