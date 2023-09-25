from django.urls import path
from AppBalti import views

urlpatterns = [
    #iniciales
    path('',views.inicio, name= "Inicio"),
    path('conjuntos/',views.conjunto, name= "Conjunto"),
    path('puntos_de_venta/',views.puntos_de_venta, name= "Puntos_De_Venta"),
    path('bombachas/',views.bombachas, name= "Bombachas"),
    path('dormir/',views.dormir, name= "Dormir"),
    
    #formularios de Create
    path('puntos_de_venta/nuevo_ingreso', views.puntoventa_formulario, name = "Ingreso_puntoventa"),
    path('conjuntos/nuevo_ingreso',views.conjunto_formulario, name = "Ingreso_conjunto" ),
    path('bombachas/nuevo_ingreso',views.bombacha_formulario, name= "Ingreso_bombacha"),
    path('dormir/nuevo_ingreso',views.dormir_formulario, name = "Ingreso_dormir"),

    #formularios busqueda
    path('bombachas/busqueda',views.buscar_bombacha, name = "Buscar_bombacha"),
    path('conjuntos/busqueda',views.buscar_conjunto, name = "Buscar_conjunto"),
    path('dormir/busqueda',views.buscar_dormir, name = "Buscar_dormir"),
    path('puntos_de_venta/busqueda',views.buscar_punto, name = "Buscar_punto"),

    
]