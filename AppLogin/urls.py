from django.urls import path
from AppLogin.views import *



urlpatterns = [

    path("login/", inicio_sesion, name = "Login"),
    path("register/", registro_usuario, name = "Register"),
    path("logout/", LogoutView.as_view(template_name='AppLogin/logout.html'),name="Logout"),
    path("edit/", editar_perfil, name = "Editar Usuario"),
]