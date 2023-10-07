from django.urls import path
from AppLogin.views import *


urlpatterns = [

    path("login/", inicio_sesion, name = "Login"),

]