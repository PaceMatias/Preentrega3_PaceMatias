from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from AppLogin.forms import RegistroUsuario, UserEditForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio_sesion(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid(): 
            
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contra)

            if user:
                login(request, user)

                return render(request, "AppBalti/inicio.html", {"mensaje":f"Hola, {usuario}!"})
                     
        else:
            form = AuthenticationForm()    
            return render(request, "AppLogin/login.html", {"mensaje":"Usuario o contraseña incorrectos","form": form})

    form = AuthenticationForm()

    return render(request, "AppLogin/login.html", {"form": form})


def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuario(request.POST)
        if form.is_valid():
          usuario = form.cleaned_data['username']
          form.save()
          return render(request, "AppBalti/inicio.html", {"mensaje":f"Se creo el usuario: {usuario}"})

    else:
        form = RegistroUsuario()     

    return render(request,"AppLogin/registro.html" ,  {"form":form})

@login_required
def editar_perfil(request):
    usuario = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
          info = form.cleaned_data

          usuario.email = info['email']
          usuario.password1 = info['password1']
          usuario.password2 = info['password2']
          usuario.first_name = info['first_name']

          usuario.save()
          return render(request, "AppBalti/inicio.html", {"mensaje":f"Se modifico el usuario: {usuario}"})

    else:
        form = UserEditForm(initial={'email': usuario.email,'first_name': usuario.first_name})
    
    return render(request, "AppLogin/editar_usuario.html", {"form":form, "usuario": usuario})
