from django.urls import path
from AppBalti.views import *


urlpatterns = [
    #iniciales
    path('',inicio, name= "Inicio"),
    path('bombachas/',bombachas, name= "Bombachas"),
    path('conjuntos/',conjunto, name= "Conjunto"),
    path('dormir/',dormir, name= "Dormir"),
    path('puntos_de_venta/',puntos_de_venta, name= "Puntos_De_Venta"),

    #Vistas de Create
    path('bombachas/nuevo_ingreso',bombacha_formulario, name= "Ingreso_bombacha"),
    path('conjuntos/nuevo_ingreso',conjunto_formulario, name = "Ingreso_conjunto" ),
    path('dormir/nuevo_ingreso',dormir_formulario, name = "Ingreso_dormir"),
    path('puntos_de_venta/nuevo_ingreso', puntoventa_formulario, name = "Ingreso_puntoventa"),
    
    #Vistas busqueda
    path('bombachas/busqueda',buscar_bombacha, name = "Buscar_bombacha"),
    path('conjuntos/busqueda',buscar_conjunto, name = "Buscar_conjunto"),
    path('dormir/busqueda',buscar_dormir, name = "Buscar_dormir"),
    path('puntos_de_venta/busqueda',buscar_punto, name = "Buscar_punto"),

    #Vistas de Read
    path('bombachas/todos',leer_bombacha, name = "Todos_bombacha"),
    path('conjuntos/todos',leer_conjunto, name = "Todos_conjunto"),
    path('dormir/todos',leer_dormir, name = "Todos_dormir"),
    path('puntos_de_venta/todos',leer_punto_venta, name = "Todos_punto"),

    #Vistas de detalles
    path("bombachas/<int:pk>",Detalle_Bombacha.as_view(), name = "Detalle_bombacha"),
    path('conjuntos/<int:pk>',Detalle_Conjunto.as_view(), name = "Detalle_conjunto"),
    path('dormir/<int:pk>',Detalle_Dormir.as_view(), name = "Detalle_dormir"),
    path('puntos_de_venta/<int:pk>',Detalle_Punto.as_view(), name = "Detalle_punto"),

    #Vistas de updates
    path('bombachas/actualizar/<int:pk>',Actualiza_Bombacha.as_view(), name = "Actualiza_bombacha"),
    path('conjuntos/actualizar/<int:pk>',Actualiza_Conjunto.as_view(), name = "Actualiza_conjunto"),
    path('dormir/actualizar/<int:pk>',Actualiza_Dormir.as_view(), name = "Actualiza_dormir"),
    path('puntos_de_venta/actualizar/<int:pk>',Actualiza_Punto.as_view(), name = "Actualiza_punto"),

    #Vistas de delete
    path('bombachas/borrar/<int:pk>',Borra_Bombacha.as_view(), name = "Borra_bombacha"),
    path('conjuntos/borrar/<int:pk>',Borra_Conjunto.as_view(), name = "Borra_conjunto"),
    path('dormir/borrar/<int:pk>',Borra_Dormir.as_view(), name = "Borra_dormir"),
    path('puntos_de_venta/borrar/<int:pk>',Borra_Punto.as_view(), name = "Borra_punto"),
    
]