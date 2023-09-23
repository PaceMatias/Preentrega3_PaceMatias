from django.db import models

# Create your models here.

class Puntos_De_Venta(models.Model):
    comercio = models.CharField(max_length=40)
    provincia = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=70)
    domicilio = models.CharField(max_length=70)
    red_social = models.CharField(max_length=60)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

class Conjunto (models.Model):
    nombre = models.CharField(max_length=20)
    articulo =  models.IntegerField()
    talle = models.CharField(max_length=10) #si bien muchos talles son por numeros otros pueden ser large medium etc..
    color = models.CharField(max_length=40)
    tipo_taza = models.CharField(max_length=20)
    tipo_bombacha = models.CharField(max_length=20)

class Bombacha (models.Model):
    nombre = models.CharField(max_length=20)
    articulo =  models.IntegerField()
    talle = models.CharField(max_length=10) #si bien muchos talles son por numeros otros pueden ser large medium etc..
    color = models.CharField(max_length=40)
    tipo_bombacha = models.CharField(max_length=20)

class Dormir (models.Model):
    nombre = models.CharField(max_length=20)
    articulo =  models.IntegerField()
    talle = models.CharField(max_length=10) #si bien muchos talles son por numeros otros pueden ser large medium etc..
    color = models.CharField(max_length=40)
    tipo_prenda = models.CharField(max_length=20)