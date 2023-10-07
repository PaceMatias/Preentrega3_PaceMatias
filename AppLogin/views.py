from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate


def inicio_sesion(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid(): 
            
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contra)

            if user is not None:
                login(request, user)

                return render(request, "AppBalti/inicio.html", {"mensaje":f"Hola, {usuario}!"})
            else:
                form = AuthenticationForm()
                return render(request, "AppLogin/login.html", {"mensaje":"Contraseña incorrecta.","form": form})
           
        else:
            form = AuthenticationForm()    
            return render(request, "AppLogin/login.html", {"mensaje":"No existe el usuario","form": form})

    form = AuthenticationForm()

    return render(request, "AppLogin/login.html", {"form": form})
