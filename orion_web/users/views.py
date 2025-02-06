from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import login

# Create your views here.

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,"home.html")

def login(request):
    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        print("----Aqui llega-----")
        print(request.POST)
        User = get_user_model()
        
        if not first_name or not last_name or not username or not email or not password1 or not password2:
            messages.error(request,"Todos los campos son obligatorios.")
        else:
            error = False
            if password1 != password2:
                messages.error(request,"Las contraseñas no coinciden")
                error = True
            if User.objects.filter(username=username).exists():    
                messages.error(request,"El usuario ya esta en uso.")
                error = True
            if User.objects.filter(email=email).exists():
                messages.error(request,"El correo ya esta en uso.")
                error = True
            if not error:
                messages.error(request,"Esta todo correcto.")
                create_user = User.objects.create_user(first_name=first_name, last_name=last_name,username=username,email=email,password=password1)
                create_user.save()
                #login(request,create_user) Si lo activo no funciona da un error

                return redirect("home")
        """
        if password1 != password2:
            messages.error(request,"Las contraseñas no coinciden")
            return redirect("register")
        elif User.objects.filter(username=username).exists():
            messages.error(request,"El usuario ya esta en uso.")
            return redirect("register")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "El correo ya esta en uso.")
            return redirect("register")
        else:
            print("----Creacion de usuario---")
            print(request.POST)
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username ,email=email ,password=password1)
            user.save()

            login(request,user)
        
            return redirect("home")
            """
        
    return render(request, "register.html")



