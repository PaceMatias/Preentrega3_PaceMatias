from django.shortcuts import render
from django.http import HttpResponse
from AppBalti.forms import *
from AppBalti.models import *
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

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

#Vistas para leer

def leer_bombacha(request):
    bombachas = Bombacha.objects.all()
    contexto = {"productos": bombachas}

    return render(request, "AppBalti/VerBombachas.html" ,contexto)

def leer_conjunto(request):
    conjuntos = Conjunto.objects.all()
    contexto = {"productos": conjuntos}

    return render(request, "AppBalti/VerConjuntos.html" ,contexto)

def leer_dormir(request):
    pijamas = Dormir.objects.all()
    contexto = {"productos": pijamas}

    return render(request, "AppBalti/VerDormir.html" ,contexto)

def leer_punto_venta(request):
    locales = Puntos_De_Venta.objects.all()
    contexto = {"puntos": locales}

    return render(request, "AppBalti/VerPuntos.html" ,contexto)

#Vistas de Formulario para buscar

def buscar_bombacha(request):
    if request.method == "GET":
        form = Buscar_Bombacha(request.GET)
        if form.is_valid():
            datos = form.cleaned_data
            filtro = Bombacha.objects.filter(tipo_bombacha__icontains = datos["tipo_bombacha"])
            mensaje = f"Resultados para: {datos['tipo_bombacha']}"
            form = Buscar_Bombacha()
            return render(request,"AppBalti/buscaBombacha.html",{"mensaje":mensaje,"form":form,"filtro":filtro})
        else:
            mensaje ="Ingrese un tipo de bombacha para buscar."
            form = Buscar_Bombacha()
            return render(request,"AppBalti/buscaBombacha.html",{"mensaje":mensaje,"form":form})
    else:
        form = Buscar_Bombacha()
        mensaje = "No se enviaron datos."
    return render(request,"AppBalti/buscaBombacha.html",{"mensaje":mensaje,"form":form})

def buscar_conjunto(request):
    if request.method == "GET":
        form = Buscar_Conjunto(request.GET)
        if form.is_valid():
            datos = form.cleaned_data
            filtro = Conjunto.objects.filter(tipo_taza__icontains = datos["tipo_taza"])
            mensaje = f"Resultados para: {datos['tipo_taza']}"
            form = Buscar_Conjunto()
            return render(request,"AppBalti/buscaConjunto.html",{"mensaje":mensaje,"form":form,"filtro":filtro})
        else:
            mensaje ="Ingrese un tipo de taza para buscar."
            form = Buscar_Conjunto()
            return render(request,"AppBalti/buscaConjunto.html",{"mensaje":mensaje,"form":form})
    else:
        form = Buscar_Conjunto()
        mensaje = "No se enviaron datos."
    return render(request,"AppBalti/buscaConjunto.html",{"mensaje":mensaje,"form":form})

def buscar_dormir(request):
    if request.method == "GET":
        form = Buscar_Dormir(request.GET)
        if form.is_valid():
            datos = form.cleaned_data
            filtro = Dormir.objects.filter(tipo_prenda__icontains = datos["tipo_prenda"])
            mensaje = f"Resultados para: {datos['tipo_prenda']}"
            form = Buscar_Dormir()
            return render(request,"AppBalti/buscaDormir.html",{"mensaje":mensaje,"form":form,"filtro":filtro})
        else:
            mensaje ="Ingrese un tipo de prenda para buscar."
            form = Buscar_Dormir()
            return render(request,"AppBalti/buscaDormir.html",{"mensaje":mensaje,"form":form})
    else:
        form = Buscar_Dormir()
        mensaje = "No se enviaron datos."
    return render(request,"AppBalti/buscaDormir.html",{"mensaje":mensaje,"form":form})     
    
def buscar_punto (request):
    if request.method == "GET":
        form = Buscar_Punto(request.GET)
        if form.is_valid():
            datos = form.cleaned_data
            filtro = Puntos_De_Venta.objects.filter(provincia__icontains = datos["provincia"])
            mensaje = f"Resultados para: {datos['provincia']}"
            form = Buscar_Punto()
            return render(request,"AppBalti/buscaPunto.html",{"mensaje":mensaje,"form":form,"filtro":filtro})
        else:
            mensaje ="Ingrese una provincia para buscar."
            form = Buscar_Punto()
            return render(request,"AppBalti/buscaPunto.html",{"mensaje":mensaje,"form":form})
    else:
        form = Buscar_Punto()
        mensaje = "No se enviaron datos."
    return render(request,"AppBalti/buscaPunto.html",{"mensaje":mensaje,"form":form})       

#Vistas Detalladas

class Detalle_Bombacha (DetailView):

    model = Bombacha
    template_name = "AppBalti/DetalleBombacha.html"

class Detalle_Conjunto (DetailView):

    model = Conjunto
    template_name = "AppBalti/DetalleConjunto.html"

class Detalle_Dormir (DetailView):

    model = Dormir
    template_name = "AppBalti/DetalleDormir.html"

class Detalle_Punto (DetailView):

    model = Puntos_De_Venta
    template_name = "AppBalti/DetallePuntos.html"

#Vistas para modificar

class Actualiza_Bombacha (UpdateView):
    
    model = Bombacha
    template_name = "AppBalti/Formbombacha.html"
    success_url = "/bombachas/todos"
    fields = ["nombre","articulo","talle","color","tipo_bombacha"]

class Actualiza_Conjunto (UpdateView):
    
    model = Conjunto
    template_name = "AppBalti/Formconjunto.html"
    success_url = "/conjuntos/todos"
    fields = ["nombre","articulo","talle","color","tipo_taza","tipo_bombacha"]

class Actualiza_Dormir (UpdateView):
    
    model = Dormir
    template_name = "AppBalti/Formdormir.html"
    success_url = "/dormir/todos"
    fields = ["nombre","articulo","talle","color","tipo_prenda"]

class Actualiza_Punto (UpdateView):
    model = Puntos_De_Venta
    template_name = "AppBalti/Formpuntoventa.html"
    success_url = "/puntos_de_venta/todos"
    fields = ["comercio","provincia","ciudad","domicilio","red_social","telefono","email"]

#Vistas para borrar

class Borra_Bombacha (DeleteView):
    
    model = Bombacha
    template_name = "AppBalti/BorraBombacha.html"
    success_url = "/bombachas/todos"

class Borra_Conjunto (DeleteView):
    
    model = Conjunto
    template_name = "AppBalti/BorraConjunto.html"
    success_url = "/conjuntos/todos"

class Borra_Dormir (DeleteView):
    
    model = Dormir
    template_name = "AppBalti/BorraDormir.html"
    success_url = "/dormir/todos"

class Borra_Punto (DeleteView):
    model = Puntos_De_Venta
    template_name = "AppBalti/BorraPunto.html"
    success_url = "/puntos_de_venta/todos"
