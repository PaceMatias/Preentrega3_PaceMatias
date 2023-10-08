from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from AppLogin.forms import RegistroUsuario
from django.contrib.auth import login, authenticate


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
          return render(request,"AppLogin/login.html" ,  {"info_registro":"Usuario creado"})

    else:
        form = RegistroUsuario()     

    return render(request,"AppLogin/registro.html" ,  {"form":form})
