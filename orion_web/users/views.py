from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import get_user_model,login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserForm

# Create your views here.

def prueba(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        print("----Aqui llega-----")
        print(request.POST)
        User = get_user_model()
        
        if not email or not password1 or not password2:
            messages.error(request,"Todos los campos son obligatorios.")
        else:
            error = False
            if password1 != password2:
                messages.error(request,"Las contraseñas no coinciden.")
                error = True
            if User.objects.filter(username=username).exists():    
                messages.error(request,"El usuario ya esta en uso.")
                error = True
            if User.objects.filter(email=email).exists():
                messages.error(request,"El correo ya esta en uso.")
                error = True
            if not error:
                create_user = User.objects.create_user(username,email,password2)
                create_user.save()

                user = authenticate(request,username=username,password=password1)
                login(request, user)
                return redirect("home")
          
    return render(request,'prueba.html',{'form':UserForm})

def index(request):
    return render(request,'index.html')
@login_required
def home(request):
    return render(request,"home.html")

def login(request):
    return render(request, "login.html")

# def register(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         email = request.POST["email"]
#         password1 = request.POST["password1"]
#         password2 = request.POST["password2"]
#         print("----Aqui llega-----")
#         print(request.POST)
#         User = get_user_model()
        
#         if not email or not password1 or not password2:
#             messages.error(request,"Todos los campos son obligatorios.")
#         else:
#             error = False
#             if password1 != password2:
#                 messages.error(request,"Las contraseñas no coinciden.")
#                 error = True
#             if User.objects.filter(username=username).exists():    
#                 messages.error(request,"El usuario ya esta en uso.")
#                 error = True
#             if User.objects.filter(email=email).exists():
#                 messages.error(request,"El correo ya esta en uso.")
#                 error = True
#             if not error:
#                 create_user = User.objects.create_user(username,email,password2)
#                 create_user.save()
#                 login(request,create_user)
#                 return redirect("home")
       
        
#     return render(request, "register.html")



def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            # Los errores se enviarán automáticamente a la plantilla
            return render(request, "register.html", {"form": form})

    form = UserForm()
    return render(request, "register.html", {"form": form})




